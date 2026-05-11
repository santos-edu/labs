# Fragmentacao de observabilidade cloud native

## Tema

Observabilidade SRE: metricas, logs e traces ainda aparecem em ferramentas separadas.

## Rodar com Container

```bash
cd labs/2026-05-observability-stack-fragmentation
touch traces.jsonl
docker compose up --build
```

Em outro terminal:

```bash
curl http://127.0.0.1:8080/work
curl http://127.0.0.1:8080/metrics
tail -f traces.jsonl
```

## Rodar sem Container

```bash
cd labs/2026-05-observability-stack-fragmentation
python3 src/app.py
```

## Teste

```bash
cd labs/2026-05-observability-stack-fragmentation
touch traces.jsonl
docker compose up --build -d
sleep 2
tests/smoke.sh
docker compose down
```

Sem container:

```bash
python3 src/app.py &
APP_PID=$!
sleep 1
tests/smoke.sh
kill $APP_PID
```

## O Que O Lab Mostra

- Logs saem no stdout em JSON.
- Metricas saem em `/metrics` no formato Prometheus.
- Traces ficam em `traces.jsonl`.

Esse desenho funciona, mas fragmenta consulta, armazenamento e correlacao. O proximo passo natural e trocar o trace/log manual por OpenTelemetry SDK e Collector.
