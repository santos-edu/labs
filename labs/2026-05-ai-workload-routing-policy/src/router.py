#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    with open(ROOT / "data" / name, encoding="utf-8") as f:
        return json.load(f)


def estimate_cost(request, backend):
    return round((request["tokens"] / 1000) * backend["cost_per_1k_tokens"], 4)


def score(request, backend):
    cost = estimate_cost(request, backend)
    violations = []

    if request["tokens"] > backend["max_tokens"]:
        violations.append("context_too_large")
    if backend["p95_ms"] > request["latency_budget_ms"]:
        violations.append("latency_budget")
    if cost > request["max_cost"]:
        violations.append("cost_budget")

    queue_penalty = backend["queue_depth"] * 20
    priority_penalty = 0 if request["priority"] == "batch" or backend["type"] == "gpu" else 300
    value = backend["p95_ms"] + queue_penalty + priority_penalty + (cost * 1000)

    return {
        "backend": backend["name"],
        "cost": cost,
        "violations": violations,
        "score": round(value, 2),
    }


def route(request, backends):
    candidates = [score(request, backend) for backend in backends]
    valid = [candidate for candidate in candidates if not candidate["violations"]]

    if valid:
        winner = min(valid, key=lambda item: item["score"])
        reason = "within_slo_and_budget"
    else:
        winner = min(candidates, key=lambda item: len(item["violations"]))
        reason = "least_bad_fallback"

    return winner, candidates, reason


def main():
    backends = load("backends.json")
    requests = load("requests.json")

    for request in requests:
        winner, candidates, reason = route(request, backends)
        print(f"request={request['id']}")
        print(f"selected={winner['backend']}")
        print(f"reason={reason}")
        print(f"estimated_cost={winner['cost']}")
        print("candidates=" + json.dumps(candidates, separators=(",", ":")))
        print()


if __name__ == "__main__":
    main()
