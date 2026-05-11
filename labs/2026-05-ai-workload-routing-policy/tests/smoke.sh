#!/usr/bin/env bash
set -euo pipefail

output="$(docker compose run --rm router)"

printf '%s\n' "$output" | grep -q 'request=req-001'
printf '%s\n' "$output" | grep -q 'selected=balanced-gpu'
printf '%s\n' "$output" | grep -q 'request=req-002'
printf '%s\n' "$output" | grep -q 'selected=cheap-cpu'
printf '%s\n' "$output" | grep -q 'request=req-003'
printf '%s\n' "$output" | grep -q 'reason=within_slo_and_budget'

echo "smoke ok"
