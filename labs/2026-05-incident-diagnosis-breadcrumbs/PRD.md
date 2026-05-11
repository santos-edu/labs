# PRD: Diagnostico barato de incidentes repetidos

## Tema

Como reduzir o custo de diagnostico quando incidentes parecidos voltam a acontecer.

## Tese

Incidente repetido fica caro quando o time nao preserva breadcrumbs suficientes para transformar sintomas em fingerprints e runbooks.

## Objetivo

Criar um lab pequeno que converte eventos de incidente em fingerprints operacionais e recomenda runbooks.

## Escopo

- Rodar em container;
- ler eventos JSON;
- gerar fingerprint por servico, sintoma, dependencia e regiao;
- apontar breadcrumbs ausentes;
- recomendar runbook quando houver correspondencia.

## Fora de Escopo

- Integracao real com PagerDuty, Slack ou Grafana;
- ML;
- banco de dados;
- automacao de remediacao.

## Criterios de Aceite

- [x] README explica como rodar;
- [x] lab roda em container;
- [x] smoke test valida fingerprint, runbook e breadcrumb ausente;
- [x] post traz tese, evidencias, insights e limites.
