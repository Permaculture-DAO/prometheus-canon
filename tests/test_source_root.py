"""Synthetic negatives; no live runtime, secret material or business records."""
import copy
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import jsonschema
import yaml

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("source_root", REPO / "scripts/validate_source_root.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class RootTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="prometheus-source-root-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        release = json.loads((REPO / v.RELEASE).read_text(encoding="utf-8"))
        for name in [r["path"] for r in release["files"]] + [v.RELEASE, v.SUMS]:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPO / name, target)

    def load(self, name):
        return yaml.safe_load((self.root / name).read_text(encoding="utf-8"))

    def write(self, name, value):
        (self.root / name).write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def reseal(self):
        release = self.load(v.RELEASE)
        for entry in release["files"]:
            entry["sha256"] = v.sha((self.root / entry["path"]).read_bytes())
        self.write(v.RELEASE, release)
        entries = [(r["path"], r["sha256"]) for r in release["files"]]
        entries.append((v.RELEASE, v.sha((self.root / v.RELEASE).read_bytes())))
        (self.root / v.SUMS).write_text("".join(f"{h}  {p}\n" for p, h in sorted(entries)), encoding="utf-8")

    def registry(self):
        name = self.load(v.ROOT)["machine_readable"]["registry"]
        return name, self.load(name)

    def invalid(self):
        with self.assertRaises((ValueError, jsonschema.ValidationError)):
            v.validate(self.root, verify_signature=False)

    def test_valid_candidate_not_admission(self):
        report = v.validate(self.root, verify_signature=False)
        self.assertEqual(report["state"], "SOURCE_ROOT_VALID")
        self.assertFalse(report["authority_adopted"])
        self.assertFalse(report["canon_signature_verified"])
        self.assertEqual(report["production_admission"], "HOLD")

    def test_one_byte_hash_mismatch_and_cli_exit(self):
        path = self.root / v.ROOT
        path.write_bytes(path.read_bytes() + b" ")
        self.invalid()
        proc = subprocess.run([sys.executable, str(REPO / "scripts/validate_source_root.py"), "--repo", str(self.root)],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 1)
        self.assertEqual(json.loads(proc.stdout)["state"], "SOURCE_ROOT_INVALID")

    def test_missing_file(self):
        (self.root / v.ROOT).unlink()
        with self.assertRaises(FileNotFoundError):
            v.validate(self.root, verify_signature=False)

    def test_original_cannot_be_rehashed_into_acceptance(self):
        path = self.root / v.BASE / "architecture/PROMETHEUS_DETERMINISTIC_ARCHITECTURE_v2_0_DEFINITIVE_SOURCE.md"
        path.write_bytes(path.read_bytes() + b"\n")
        self.reseal()
        self.invalid()

    def test_duplicate_active_identity(self):
        name, registry = self.registry()
        registry["sources"].append(copy.deepcopy(registry["sources"][1]))
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_duplicate_active_version_for_role(self):
        name, registry = self.registry()
        registry["sources"][2]["status"] = "ACTIVE"
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_missing_scope(self):
        name, registry = self.registry()
        del registry["sources"][1]["scope"]
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_missing_dependency(self):
        name, registry = self.registry()
        record = registry["sources"][1]
        record["upstream"].append("MISSING@1.0")
        record["upstream_hashes"]["MISSING@1.0"] = "a" * 64
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_dependency_hash_mismatch(self):
        name, registry = self.registry()
        registry["sources"][1]["upstream_hashes"][v.CANON_KEY] = "a" * 64
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_active_historical_dependency(self):
        name, registry = self.registry()
        active, historical = registry["sources"][3], registry["sources"][2]
        active["upstream"].append(historical["record_key"])
        active["upstream_hashes"][historical["record_key"]] = historical["sha256"]
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_dependency_and_supersession_cycle_detection(self):
        for label in ("dependency", "supersession"):
            with self.subTest(label=label), self.assertRaises(v.InvalidRoot):
                v.acyclic({"A@1": ["B@1"], "B@1": ["A@1"]}, label)

    def test_inconsistent_supersession(self):
        name, registry = self.registry()
        registry["sources"][2]["superseded_by"] = "MISSING@1"
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_capital_and_authority_escalation(self):
        name, registry = self.registry()
        registry["sources"][-1]["authorises_capital"] = True
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_candidate_cannot_become_canon(self):
        name, registry = self.registry()
        registry["sources"][-1]["authority_class"] = "CANON_SOURCE"
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_legacy_architecture_cannot_be_active(self):
        name, registry = self.registry()
        registry["sources"][1]["source_id"] = "PRM-ARCH-DET-001"
        registry["sources"][1]["record_key"] = "PRM-ARCH-DET-001@2.0"
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_adoption_flag(self):
        root = self.load(v.ROOT)
        root["authority_adopted"] = True
        self.write(v.ROOT, root)
        self.reseal()
        self.invalid()

    def test_hierarchy_change(self):
        path = self.load(v.ROOT)["machine_readable"]["authority_lattice"]
        lattice = self.load(path)
        lattice["governing_hierarchy"].insert(2, "meta_layer")
        self.write(path, lattice)
        self.reseal()
        self.invalid()

    def test_signed_canon_binding_changed(self):
        root = self.load(v.ROOT)
        root["governing_canon"]["tag_object"] = "a" * 40
        self.write(v.ROOT, root)
        self.reseal()
        self.invalid()

    def test_unknown_status_cannot_resolve(self):
        name, registry = self.registry()
        registry["sources"][1]["status"] = "UNKNOWN"
        self.write(name, registry)
        self.reseal()
        self.invalid()

    def test_unsafe_release_path(self):
        release = self.load(v.RELEASE)
        release["files"][0]["path"] = "../outside"
        self.write(v.RELEASE, release)
        self.invalid()

    def test_yaml_duplicate_key(self):
        with self.assertRaises(v.InvalidRoot):
            yaml.load("status: ACTIVE\nstatus: HISTORICAL\n", Loader=v.UniqueLoader)

    def test_json_duplicate_key_and_nan(self):
        for text in ('{"x":1,"x":2}', '{"x":NaN}'):
            with self.subTest(text=text), self.assertRaises(v.InvalidRoot):
                v.parse_json(text)

    def test_ravel_cannot_reference_aeterna_document(self):
        name, registry = self.registry()
        aeterna, ravel = registry["sources"][3], registry["sources"][5]
        ravel.update(path=aeterna["path"], name=aeterna["name"], sha256=aeterna["sha256"])
        for record in registry["sources"]:
            if ravel["record_key"] in record["upstream_hashes"]:
                record["upstream_hashes"][ravel["record_key"]] = ravel["sha256"]
        self.write(name, registry)
        root = self.load(v.ROOT)
        for record in root["active_records"]:
            if record["record_key"] == ravel["record_key"]:
                record["sha256"] = ravel["sha256"]
        self.write(v.ROOT, root)
        self.reseal()
        with self.assertRaisesRegex(v.InvalidRoot, "prose source identity"):
            v.validate(self.root, verify_signature=False)

    def test_missing_prose_identity_rejected(self):
        name, registry = self.registry()
        aeterna = registry["sources"][3]
        path = self.root / aeterna["path"]
        path.write_text(path.read_text(encoding="utf-8").replace("**Source ID:** PRM-RISK-AETERNA-001", "Identity missing"), encoding="utf-8")
        aeterna["sha256"] = v.sha(path.read_bytes())
        for record in registry["sources"]:
            if aeterna["record_key"] in record["upstream_hashes"]:
                record["upstream_hashes"][aeterna["record_key"]] = aeterna["sha256"]
        self.write(name, registry)
        root = self.load(v.ROOT)
        for record in root["active_records"]:
            if record["record_key"] == aeterna["record_key"]:
                record["sha256"] = aeterna["sha256"]
        self.write(v.ROOT, root)
        self.reseal()
        with self.assertRaisesRegex(v.InvalidRoot, "prose source identity"):
            v.validate(self.root, verify_signature=False)

    def test_release_cannot_declare_admission_passed(self):
        release = self.load(v.RELEASE)
        release["production_admission"] = "PASSED"
        self.write(v.RELEASE, release)
        self.reseal()
        with self.assertRaisesRegex(v.InvalidRoot, "release admission/scope"):
            v.validate(self.root, verify_signature=False)

    def test_release_scope_cannot_claim_production(self):
        release = self.load(v.RELEASE)
        release["scope"] = "PRODUCTION"
        self.write(v.RELEASE, release)
        self.reseal()
        self.invalid()

    def test_application_cannot_omit_methods(self):
        name, registry = self.registry()
        civ = registry["sources"][-1]
        civ["upstream"] = [key for key in civ["upstream"] if not key.startswith("PRM-RISK-")]
        civ["upstream_hashes"] = {key: sha for key, sha in civ["upstream_hashes"].items() if key in civ["upstream"]}
        self.write(name, registry)
        self.reseal()
        with self.assertRaisesRegex(v.InvalidRoot, "required method dependency"):
            v.validate(self.root, verify_signature=False)

    def test_change_ledger_hash_must_match_registry(self):
        name = v.BASE + "releases/PROMETHEUS_SOURCE_ROOT_v2_0_1_CHANGE_LEDGER.json"
        ledger = self.load(name)
        ledger["patches"][0]["new_sha256"] = "a" * 64
        self.write(name, ledger)
        self.reseal()
        with self.assertRaisesRegex(v.InvalidRoot, "ledger hash"):
            v.validate(self.root, verify_signature=False)

    def test_change_ledger_patch_coverage_required(self):
        name = v.BASE + "releases/PROMETHEUS_SOURCE_ROOT_v2_0_1_CHANGE_LEDGER.json"
        ledger = self.load(name)
        ledger["patches"].pop()
        self.write(name, ledger)
        self.reseal()
        with self.assertRaisesRegex(v.InvalidRoot, "ledger patch coverage"):
            v.validate(self.root, verify_signature=False)


class ComputeTests(unittest.TestCase):
    def setUp(self):
        root = yaml.safe_load((REPO / v.ROOT).read_text(encoding="utf-8"))
        self.schema = json.loads((REPO / root["schema_paths"]["compute_provenance"]).read_text())
        self.base = {"compute_id": "synthetic", "model_or_algorithm_id": "test", "version": "1",
                     "input_hashes": ["a" * 64], "output_hash": "b" * 64,
                     "verification_state": "UNVERIFIED", "gate_effect_allowed": False}

    def test_all_modes_cannot_affect_gate(self):
        for mode in "DPHQ":
            for state in ("UNVERIFIED", "REJECTED", "D_VERIFIED", "HUMAN_REVIEW_REQUIRED"):
                with self.subTest(mode=mode, state=state), self.assertRaises(jsonschema.ValidationError):
                    v.validate_compute(self.schema, self.base | {"mode": mode, "verification_state": state,
                        "gate_effect_allowed": True, "verification_receipt_sha256": "c" * 64, "reviewer": "test"})

    def test_unverified_no_effect_structurally_valid(self):
        for mode in "DPHQ":
            v.validate_compute(self.schema, self.base | {"mode": mode})

    def test_missing_effect_flag_rejected(self):
        record = self.base | {"mode": "D"}
        del record["gate_effect_allowed"]
        with self.assertRaises(jsonschema.ValidationError):
            v.validate_compute(self.schema, record)

    def test_verified_requires_structural_receipt_not_admission(self):
        record = self.base | {"mode": "P", "verification_state": "D_VERIFIED"}
        with self.assertRaises(jsonschema.ValidationError):
            v.validate_compute(self.schema, record)
        v.validate_compute(self.schema, record | {"verification_receipt_sha256": "c" * 64, "reviewer": "synthetic"})


if __name__ == "__main__":
    unittest.main()
