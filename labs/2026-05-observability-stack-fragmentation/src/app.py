#!/usr/bin/env python3
import json
import os
import random
import time
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer

REQUESTS = 0
ERRORS = 0
LATENCIES = []


def log(event, **fields):
    payload = {"ts": time.time(), "event": event, **fields}
    print(json.dumps(payload), flush=True)


def span(name, duration_ms, **attrs):
    trace = {
        "trace_id": uuid.uuid4().hex,
        "span_id": uuid.uuid4().hex[:16],
        "name": name,
        "duration_ms": duration_ms,
        "attrs": attrs,
        "ts": time.time(),
    }
    with open("traces.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(trace) + "\n")
    return trace


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global REQUESTS, ERRORS

        start = time.time()
        REQUESTS += 1

        if self.path == "/metrics":
            self.metrics()
            return

        if self.path == "/health":
            self.send_json({"ok": True})
            return

        if self.path == "/work":
            delay = random.uniform(0.02, 0.12)
            time.sleep(delay)
            duration_ms = round((time.time() - start) * 1000, 2)
            LATENCIES.append(duration_ms)
            trace = span("GET /work", duration_ms, route="/work")
            log("request", path="/work", status=200, duration_ms=duration_ms, trace_id=trace["trace_id"])
            self.send_json({"message": "work done", "duration_ms": duration_ms, "trace_id": trace["trace_id"]})
            return

        ERRORS += 1
        duration_ms = round((time.time() - start) * 1000, 2)
        LATENCIES.append(duration_ms)
        log("request", path=self.path, status=404, duration_ms=duration_ms)
        self.send_json({"error": "not found"}, status=404)

    def metrics(self):
        avg = sum(LATENCIES) / len(LATENCIES) if LATENCIES else 0
        body = "\n".join(
            [
                "# HELP lab_requests_total Total HTTP requests.",
                "# TYPE lab_requests_total counter",
                f"lab_requests_total {REQUESTS}",
                "# HELP lab_errors_total Total HTTP errors.",
                "# TYPE lab_errors_total counter",
                f"lab_errors_total {ERRORS}",
                "# HELP lab_request_latency_ms_avg Average request latency in ms.",
                "# TYPE lab_request_latency_ms_avg gauge",
                f"lab_request_latency_ms_avg {avg:.2f}",
                "",
            ]
        )
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.end_headers()
        self.wfile.write(body.encode())

    def send_json(self, payload, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def log_message(self, *_args):
        return


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "8080"))
    log("server_start", addr=host, port=port)
    HTTPServer((host, port), Handler).serve_forever()
