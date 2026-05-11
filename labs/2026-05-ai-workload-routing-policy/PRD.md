# PRD: Roteamento de workloads de IA por SLO e custo

## Tema

Plataformas de IA precisam rotear inferencia considerando tokens, latencia e custo, nao apenas CPU ou memoria.

## Tese

Quando IA vira workload de producao, roteamento passa a ser uma decisao de confiabilidade e FinOps.

## Objetivo

Criar um simulador local que escolhe backend de inferencia usando budget de latencia, budget de custo, tamanho de contexto e fila.

## Escopo

- Rodar em container;
- ler backends e requests em JSON;
- calcular custo estimado;
- validar limites;
- explicar decisao de roteamento.

## Fora de Escopo

- Kubernetes real;
- GPU real;
- modelo LLM real;
- autoscaling.

## Criterios de Aceite

- [x] lab roda em container;
- [x] smoke test valida decisoes esperadas;
- [x] post traz insights e limites.
