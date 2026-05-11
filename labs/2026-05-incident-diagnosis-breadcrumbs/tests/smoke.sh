#!/usr/bin/env bash
set -euo pipefail

output="$(docker compose run --rm diagnose)"

printf '%s\n' "$output" | grep -q 'fingerprint=checkout:http_5xx_spike:payments:us-east-1'
printf '%s\n' "$output" | grep -q 'runbook=Checkout 5xx caused by payments dependency'
printf '%s\n' "$output" | grep -q 'missing_breadcrumbs=deploy_sha'

echo "smoke ok"
