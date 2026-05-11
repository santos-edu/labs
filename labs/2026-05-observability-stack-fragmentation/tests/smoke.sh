#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${BASE_URL:-http://127.0.0.1:8080}"

curl -fsS "$BASE_URL/health" | grep -q '"ok": true'
curl -fsS "$BASE_URL/work" | grep -q 'trace_id'
curl -fsS "$BASE_URL/metrics" | grep -q 'lab_requests_total'

echo "smoke ok"
