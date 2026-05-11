# Fragmentacao de observabilidade cloud native

## Tese

O problema central da observabilidade cloud native nao e falta de ferramentas; e a falta de um contrato comum entre metricas, logs e traces.

## Por Que Isso Importa

Em incidentes reais, o custo nao esta apenas em coletar sinais. O custo aparece quando o SRE precisa alternar entre dashboards, logs e traces sem um identificador comum, sem semantica consistente e sem caminho claro para correlacao.

Essa fragmentacao aumenta MTTR porque transforma diagnostico em trabalho manual de busca.

## O Lab

O lab cria um app HTTP minimo com tres sinais separados:

```bash
touch traces.jsonl
docker compose up --build -d
tests/smoke.sh
docker compose down
```

Endpoints:

- `/work`: executa trabalho falso, gera log e trace;
- `/metrics`: expoe metricas em formato Prometheus;
- `traces.jsonl`: guarda spans em arquivo local.

## Evidencias

- O endpoint `/work` retorna um `trace_id`.
- O log JSON no stdout tambem inclui `trace_id`.
- As metricas em `/metrics` mostram contadores e latencia media, mas nao carregam o mesmo contexto do trace.

## Insights

1. Ter os tres sinais nao significa ter observabilidade integrada.
2. O `trace_id` ja mostra o valor de um contrato comum, mesmo em um lab pequeno.
3. Prometheus resolve bem serie temporal, mas nao resolve sozinho narrativa de incidente.
4. Logs sao ricos em contexto, mas viram busca manual quando nao seguem padrao.
5. OpenTelemetry entra como camada de padronizacao antes de ser uma ferramenta de coleta.

## Limites

Este lab nao prova escala, custo operacional nem qualidade de dashboards. Ele mostra apenas o ponto de friccao: sinais separados exigem correlacao manual.

## Proximo Passo

Adicionar OpenTelemetry SDK e Collector para enviar traces e metricas por um caminho comum.
