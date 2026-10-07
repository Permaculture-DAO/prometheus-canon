"""Fail-closed candidate Source-Root integrity, graph and boundary validation.

This is not runtime admission, scientific certification or a deployment tool.
CLI verifies the existing signed Canon tag; no private key or network is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import jsonschema
import yaml

BASE = "governance/sources/"
RELEASE = BASE + "releases/PROMETHEUS_SOURCE_ROOT_v2_0_1_RELEASE_MANIFEST.json"
SUMS = BASE + "releases/PROMETHEUS_SOURCE_ROOT_v2_0_1_SHA256SUMS.txt"
ROOT = BASE + "PROMETHEUS_ROOT_SOURCE_MANIFEST_v1_0_1.yaml"
FINGERPRINT = "D20DFF6CBE331B3A4109DF848C8CB0D48C7F60DA"
CANON_KEY = "PRM-CANON-SIGNED@v1.1.2-genesis"
CANON_SHA = "f3862005bc4d6e8e4cba0f2a7646e67dff758fcd28c8411046eb5d04875f9540"
CANON_TAG_OBJECT = "e72c753ba7d916cc406b53d0840ca4c45ca345e4"
CANON_COMMIT = "dcafb0c850029629634ee974b4a8126481a4f9fd"
HIERARCHY = ["living_system_reality", "governing_prose_canon", "derived_canonicals",
             "methodologies_api_contracts", "ordinary_governance", "technical_implementation",
             "ai_context", "market_pressure"]
ROLES = {"signed_canon": "PRM-CANON-SIGNED", "global_architecture": "PRM-ARCH-DET-002",
         "aeterna_method": "PRM-RISK-AETERNA-001", "ravel_operational": "PRM-RISK-RAVEL-OP-002",
         "civilization_application": "PRM-CIV-APP-006"}
CLASSES = {"signed_canon": "CANON_SOURCE", "global_architecture": "CONTROLLED_GLOBAL_ARCHITECTURE_SOURCE",
           "aeterna_method": "CONTROLLED_METHODOLOGICAL_SOURCE",
           "ravel_operational": "CONTROLLED_OPERATIONAL_METHODOLOGY_SOURCE",
           "civilization_application": "CONTROLLED_APPLICATION_SPECIFICATION"}
HEX = re.compile(r"[a-f0-9]{64}\Z")


class InvalidRoot(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise InvalidRoot(message)


class UniqueLoader(yaml.SafeLoader):
    """Safe YAML with duplicate/non-string mapping keys rejected."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        require(isinstance(key, str) and key not in result, f"duplicate/invalid YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_json(text):
    return json.loads(text, object_pairs_hook=unique_json,
                      parse_constant=lambda x: (_ for _ in ()).throw(InvalidRoot(f"invalid number {x}")))


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(repo: Path, name: str) -> Path:
    require(isinstance(name, str) and name and "\\" not in name, "invalid portable path")
    path = Path(name)
    require(not path.is_absolute() and ".." not in path.parts and ":" not in name, f"unsafe path: {name}")
    resolved = (repo / path).resolve()
    require(resolved.is_relative_to(repo.resolve()), f"path escapes repository: {name}")
    return resolved


def acyclic(graph: dict[str, list[str]], label: str) -> None:
    visited, stack = set(), set()

    def visit(key):
        require(key not in stack, f"{label} cycle at {key}")
        if key in visited:
            return
        stack.add(key)
        for target in graph[key]:
            require(target in graph, f"{label} missing target: {target}")
            visit(target)
        stack.remove(key)
        visited.add(key)

    for key in graph:
        visit(key)


def validate_compute(schema: dict, record: dict) -> None:
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(record)


def validate(repo: Path, verify_signature: bool = True, gpg: str = "gpg") -> dict:
    repo = repo.resolve()
    release = parse_json(safe_path(repo, RELEASE).read_text(encoding="utf-8"))
    require(release["deployment_authority"] is False and release["authority_adopted"] is False,
            "candidate cannot grant adoption/deployment")
    require(release["release_id"] == "PROMETHEUS-SOURCE-ROOT-v2.0.1-candidate", "wrong candidate release")
    files = {}
    for entry in release["files"]:
        name, expected = entry["path"], entry["sha256"]
        require(name not in files and HEX.fullmatch(expected), f"duplicate/invalid file pin: {name}")
        require(name not in (RELEASE, SUMS), "circular release hash")
        require(sha(safe_path(repo, name).read_bytes()) == expected, f"hash mismatch: {name}")
        files[name] = expected
    sums = {}
    for line in safe_path(repo, SUMS).read_text(encoding="utf-8").splitlines():
        require(bool(re.fullmatch(r"[a-f0-9]{64}  .+", line)), "invalid SHA256SUMS line")
        expected, name = line.split("  ", 1)
        require(name not in sums and name != SUMS, f"duplicate/self checksum: {name}")
        require(sha(safe_path(repo, name).read_bytes()) == expected, f"checksum mismatch: {name}")
        sums[name] = expected
    require(sums == files | {RELEASE: sha(safe_path(repo, RELEASE).read_bytes())}, "checksum/release coverage mismatch")
    old_sums = BASE + "releases/PROMETHEUS_SOURCE_ROOT_v2_0_SHA256SUMS.txt"
    require(files.get(old_sums) == "06375bb7ebc09a5b514386b6d434be45f8abd5d62040c8f360f790cec8f53fb7",
            "original checksum set changed")
    for line in safe_path(repo, old_sums).read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        paths = [p for p in files if Path(p).name == name]
        require(len(paths) == 1 and files[paths[0]] == expected, f"original payload changed: {name}")

    def load_yaml(name):
        require(name in files, f"unhashed YAML: {name}")
        value = yaml.load(safe_path(repo, name).read_text(encoding="utf-8"), Loader=UniqueLoader)
        require(isinstance(value, dict), f"not a YAML mapping: {name}")
        return value

    root = load_yaml(ROOT)
    require(root["active_selection_scope"] == "CANDIDATE_DESIGN_ONLY", "authority selection scope changed")
    require(root["authority_adopted"] is False and root["deployment_authority"] is False,
            "root authority/deploy escalation")
    require(root["production_admission"] == "HOLD" and root["meta_layer_adoption"] == "PROPOSED_NOT_ADOPTED",
            "admission/hierarchy escalation")
    require(root["compute_policy"] == {"modes": ["D", "P", "H", "Q"],
            "material_gate_effects_implemented": False, "d_verified_is_not_admission": True}, "compute authority escalation")
    binding = root["governing_canon"]
    require((binding["record_key"], binding["sha256"], binding["tag_object"], binding["commit"],
             binding["signer_fingerprint"]) == (CANON_KEY, CANON_SHA, CANON_TAG_OBJECT, CANON_COMMIT, FINGERPRINT),
            "signed Canon binding changed")
    require(binding["tag"] == "v1.1.2-genesis" and files[binding["path"]] == CANON_SHA, "unsigned Canon substitution")
    lattice = load_yaml(root["machine_readable"]["authority_lattice"])
    require(lattice["authority_adopted"] is False and lattice["governing_canon"] == CANON_KEY,
            "lattice adoption escalation")
    require(lattice["governing_hierarchy"] == HIERARCHY and lattice["meta_layer_adoption"] == "PROPOSED_NOT_ADOPTED",
            "governing hierarchy changed")
    registry = load_yaml(root["machine_readable"]["registry"])
    require(registry["active_selection_scope"] == "CANDIDATE_DESIGN_ONLY" and
            registry["supersession_scope"] == "CANDIDATE_GRAPH_ONLY_NOT_GOVERNANCE_ADOPTION" and
            registry["historical_inventory_is_resolvable"] is False, "registry authority escalation")
    require(registry["historical_inventory_reference"] in files, "unhashed historical inventory")
    policy = registry["default_retrieval_policy"]
    require(policy["prefer_status"] == ["ACTIVE"] and policy["unknown_status"] == "REJECT" and
            set(policy["exclude_by_default"]) == {"PROPOSED", "SUPERSEDED", "HISTORICAL", "RETIRED",
                                                 "ACTIVE_SUPPORTING", "HISTORICAL_EVIDENCE_SNAPSHOT"}, "unsafe retrieval policy")
    schemas = {}
    for kind, name in root["schema_paths"].items():
        require(name in files, f"unhashed schema: {name}")
        schema = parse_json(safe_path(repo, name).read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(schema)
        schemas[kind] = schema
    require(set(schemas) == {"source_record", "controlled_source_release", "compute_provenance"}, "schema set incomplete")
    require(schemas["compute_provenance"]["properties"]["gate_effect_allowed"] == {
        "const": False, "description": "No authority/effect path exists in Source-Root intake; true is rejected for ALL modes."},
        "material gate effects cannot be enabled in intake")
    records, roles = {}, {}
    for record in registry["sources"]:
        jsonschema.Draft202012Validator(schemas["source_record"]).validate(record)
        key = record["record_key"]
        require(key == record["source_id"] + "@" + record["version"] and key not in records, f"duplicate/invalid identity: {key}")
        require(files.get(record["path"]) == record["sha256"] and Path(record["path"]).name == record["name"],
                f"record file/hash mismatch: {key}")
        require(record["source_id"] == ROLES[record["selection_role"]], f"source role mismatch: {key}")
        require(record["authority_class"] == CLASSES[record["selection_role"]], f"source authority class mismatch: {key}")
        if record["selection_role"] == "signed_canon":
            require(key == CANON_KEY and record["canonical"] is True and record["adoption_state"] == "RATIFIED_SIGNED_CANON"
                    and record["authority_class"] == "CANON_SOURCE", "false canon authority")
        else:
            require(record["canonical"] is False and record["adoption_state"] == "DESIGN_CANDIDATE", "candidate authority escalation")
        if record["status"] == "ACTIVE":
            require(record["selection_role"] not in roles, f"duplicate ACTIVE role: {record['selection_role']}")
            roles[record["selection_role"]] = key
            text = safe_path(repo, record["path"]).read_text(encoding="utf-8")
            if text.startswith("---\n"):
                front = yaml.load(text.split("---", 2)[1], Loader=UniqueLoader)
                require(front["source_id"] == record["source_id"] and str(front["release"]).removeprefix("v") == record["version"],
                        f"source header drift: {key}")
                require(front.get("authorises_capital", False) is False and front.get("canonical", False) is False,
                        f"source authority flag: {key}")
                if "primary_method_dependency" in front:
                    require(front["primary_method_dependency"] in record["upstream"], "RAVEL dependency drift")
            if record["selection_role"] == "aeterna_method":
                require(f"**Release:** v{record['version']}" in text and f"- `version`: `{record['version']}`" in text,
                        "AETERNA registration drift")
        records[key] = record
    require(set(roles) == set(ROLES), "active role set incomplete")
    expected_active = {r["record_key"]: r["sha256"] for r in root["active_records"]}
    require(len(expected_active) == len(root["active_records"]) and expected_active == {
        key: r["sha256"] for key, r in records.items() if r["status"] == "ACTIVE"}, "root/registry active set mismatch")
    for key, record in records.items():
        require(set(record["upstream"]) == set(record["upstream_hashes"]), f"dependency hash coverage: {key}")
        for target in record["upstream"]:
            require(target in records and records[target]["sha256"] == record["upstream_hashes"][target], f"dependency closure: {target}")
            require(record["status"] != "ACTIVE" or records[target]["status"] == "ACTIVE", f"ACTIVE historical dependency: {target}")
        if record["status"] == "ACTIVE" and key != CANON_KEY:
            require(CANON_KEY in record["upstream"], f"missing Canon dependency: {key}")
        if record["status"] == "ACTIVE" and record["selection_role"] in ("aeterna_method", "ravel_operational", "civilization_application"):
            require(roles["global_architecture"] in record["upstream"], f"missing architecture dependency: {key}")
        for previous in record.get("supersedes", []):
            require(previous in records and records[previous]["status"] == "SUPERSEDED" and
                    records[previous].get("superseded_by") == key, f"supersession inconsistency: {previous}")
        if record["status"] == "SUPERSEDED":
            require(record.get("superseded_by") in records and key in records[record["superseded_by"]].get("supersedes", []),
                    f"orphan superseded record: {key}")
    acyclic({k: v["upstream"] for k, v in records.items()}, "dependency")
    acyclic({k: v.get("supersedes", []) for k, v in records.items()}, "supersession")
    if verify_signature:
        def git(*args):
            return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()
        require(git("rev-parse", binding["tag"]) == CANON_TAG_OBJECT and
                git("rev-parse", binding["tag"] + "^{}") == CANON_COMMIT, "signed tag identity mismatch")
        proc = subprocess.run(["git", "-C", str(repo), "-c", f"gpg.program={gpg}", "-c", "gpg.format=openpgp",
                               "verify-tag", "--raw", binding["tag"]], capture_output=True, text=True)
        require(proc.returncode == 0 and f"[GNUPG:] VALIDSIG {FINGERPRINT} " in proc.stderr, "Canon signature verification failed")
    return {"state": "SOURCE_ROOT_VALID", "scope": "CANDIDATE_DESIGN_INTEGRITY_ONLY", "files_verified": len(files),
            "records_verified": len(records), "active_keys": sorted(expected_active),
            "canon_signature_verified": verify_signature, "authority_adopted": False, "production_admission": "HOLD",
            "material_gate_effects_implemented": False, "deployment_performed": False,
            "manifest_sha256": sha(safe_path(repo, RELEASE).read_bytes()),
            "checksums_sha256": sha(safe_path(repo, SUMS).read_bytes())}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--gpg", default="gpg")
    args = parser.parse_args()
    try:
        report = validate(args.repo, gpg=args.gpg)
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError, jsonschema.ValidationError,
            jsonschema.SchemaError, subprocess.SubprocessError) as exc:
        print(json.dumps({"state": "SOURCE_ROOT_INVALID", "scope": "CANDIDATE_DESIGN_INTEGRITY_ONLY", "error": str(exc),
                          "production_admission": "HOLD", "deployment_performed": False}, sort_keys=True))
        return 1
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
