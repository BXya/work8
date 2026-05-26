import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifest.json"


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    required_top = ["name", "release", "status", "product", "components", "accepted_gates"]
    missing = [key for key in required_top if key not in data]
    if missing:
        print(json.dumps({"ok": False, "error": "missing_top_level_keys", "missing": missing}, indent=2))
        return 1

    if data["release"] != "workbuddy-agent-os-v1.0.0-alpha.1":
        print(json.dumps({"ok": False, "error": "unexpected_release", "release": data["release"]}, indent=2))
        return 1

    components = data["components"]
    for name in ["workbuddy-native-ingress", "goclaw-stack", "openclaw-substrate"]:
        item = components.get(name)
        if not item:
            print(json.dumps({"ok": False, "error": "missing_component", "component": name}, indent=2))
            return 1
        for key in ["repository", "commit", "tag"]:
            if not item.get(key):
                print(json.dumps({"ok": False, "error": "missing_component_key", "component": name, "key": key}, indent=2))
                return 1

    failed_gates = [name for name, ok in data["accepted_gates"].items() if ok is not True]
    if failed_gates:
        print(json.dumps({"ok": False, "error": "gate_not_accepted", "gates": failed_gates}, indent=2))
        return 1

    docs = ["README.md", "docs/ARCHITECTURE.md", "docs/ALPHA_ACCEPTANCE.md", "docs/QUICKSTART.md", "site/index.html"]
    missing_docs = [path for path in docs if not (ROOT / path).exists()]
    if missing_docs:
        print(json.dumps({"ok": False, "error": "missing_docs", "paths": missing_docs}, indent=2))
        return 1

    print(json.dumps({
        "ok": True,
        "release": data["release"],
        "components": {name: item["commit"][:7] for name, item in components.items()},
        "docs": docs
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
