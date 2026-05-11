# Fragmentacao de observabilidade cloud native

## Contexto

Tema escolhido a partir de pesquisa semanal: fragmentacao de stacks de observabilidade em ambientes cloud native.

## Hipotese

Mesmo com ferramentas maduras, times SRE ainda sofrem quando metricas, logs e traces ficam espalhados.

## Lab

Foi criado um app HTTP minimo:

- `/work` gera log JSON e trace;
- `/metrics` expoe metricas Prometheus;
- `traces.jsonl` armazena spans locais.
- `docker compose` roda o lab de forma isolada.

## Resultado

O lab mostra que os tres sinais existem, mas ficam em lugares diferentes: stdout, endpoint Prometheus e arquivo local. Isso cria friccao para correlacionar incidentes.

## Proximo Passo

Adicionar OpenTelemetry SDK e Collector para unificar a coleta.
