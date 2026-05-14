# PRD: ai internal app guardrails

## Contexto

Descreva o problema real e por que ele importa para SRE/SWE.

## Tese

Escreva uma frase opinativa que o lab vai testar.

Exemplo: "O problema nao e falta de ferramenta, e falta de padronizacao entre sinais."

## Objetivo

Construir um laboratorio pratico e reproduzivel sobre `ai-internal-app-guardrails`.

## Escopo

- Criar implementacao minima funcional;
- gerar evidencia observavel, mesmo pequena;
- documentar comandos de execucao;
- explicar tradeoffs e limites;
- registrar aprendizados em `post.md`.

## Fora de Escopo

- Deploy em producao;
- uso de servicos pagos;
- automacoes que exijam credenciais sensiveis sem necessidade.

## Requisitos

- Rodar localmente;
- depender de ferramentas open source ou free tier;
- manter comandos documentados;
- preservar isolamento do ambiente local.

## Entregaveis

- `README.md`;
- codigo ou configuracao em `src/` e/ou `infra/`;
- validacoes em `tests/` quando aplicavel;
- `post.md` como rascunho de artigo;
- `lab-checklist.md` preenchido.

## Criterios de Aceite

- O laboratorio pode ser executado a partir do README;
- os comandos principais foram validados;
- o post tem tese clara;
- o post mostra pelo menos 3 insights;
- o post separa evidencia, interpretacao e limites.
