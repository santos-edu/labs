#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    with open(ROOT / "data" / name, encoding="utf-8") as f:
        return json.load(f)


def fingerprint(event):
    parts = [event["service"], event["symptom"], event["dependency"], event["region"]]
    return ":".join(parts)


def missing_breadcrumbs(event):
    required = ["service", "symptom", "metric", "value", "deploy_sha", "dependency", "region"]
    return [key for key in required if event.get(key) in (None, "")]


def main():
    events = load("events.json")
    runbooks = load("runbooks.json")

    for event in events:
        fp = fingerprint(event)
        missing = missing_breadcrumbs(event)
        runbook = runbooks.get(fp)

        print(f"incident={event['id']}")
        print(f"fingerprint={fp}")
        print(f"missing_breadcrumbs={','.join(missing) if missing else 'none'}")

        if runbook:
            print(f"runbook={runbook['title']}")
            for check in runbook["checks"]:
                print(f"- {check}")
        else:
            print("runbook=none")

        print()


if __name__ == "__main__":
    main()
