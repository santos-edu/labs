# Diagnostico barato de incidentes repetidos

## Tese

Incidente repetido nao deveria exigir investigacao do zero. O que falta muitas vezes nao e mais alerta, mas breadcrumbs bons o suficiente para reconhecer o padrao.

## Por Que Isso Importa

SREs gastam tempo demais reconstruindo contexto: qual servico mudou, qual dependencia degradou, qual regiao foi afetada e se isso ja aconteceu antes. Quando esses dados nao viram um fingerprint, o time reaprende a mesma causa raiz.

## O Lab

O lab recebe eventos JSON e gera:

- fingerprint operacional;
- breadcrumbs ausentes;
- runbook recomendado.

```bash
docker compose run --rm diagnose
tests/smoke.sh
```

## Evidencias

- `inc-001` e `inc-002` viram o mesmo fingerprint: `checkout:http_5xx_spike:payments:us-east-1`.
- O fingerprint encontra o runbook `Checkout 5xx caused by payments dependency`.
- `inc-003` aponta `missing_breadcrumbs=deploy_sha`, mostrando perda de contexto.

## Insights

1. O fingerprint e mais util quando nasce de campos operacionais, nao de texto livre.
2. Breadcrumb ausente nao impede resposta, mas aumenta o custo cognitivo do diagnostico.
3. Runbook bom nao substitui investigacao; ele reduz o espaco inicial de busca.
4. Repeticao de incidente sem fingerprint vira memoria tribal.
5. Antes de automatizar remediacao, vale automatizar reconhecimento.

## Limites

O lab usa dados estaticos e nao mede MTTR real. Ele mostra o mecanismo: contexto estruturado reduz trabalho repetitivo.

## Proximo Passo

Gerar fingerprints a partir de logs reais de uma aplicacao e anexar links para dashboards.
