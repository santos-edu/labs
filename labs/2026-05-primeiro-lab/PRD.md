# PRD: Bootstrap do control plane com n8n e Docker Compose

## Tema

Bootstrap de um control plane local para automacao de laboratorios SRE/SWE usando n8n, PostgreSQL e Docker Compose.

## Objetivo

Validar o MVP do control plane: subir n8n + PostgreSQL localmente e confirmar acesso HTTP.

## Escopo

- Rodar `make validate`;
- rodar `make up`;
- checar containers com `make ps`;
- testar `http://localhost:5678`.

## Resultado Esperado

- `n8n-postgres` healthy;
- `n8n` running;
- HTTP `200 OK` em `localhost:5678`.

## Fora de Escopo

- Integrações externas;
- Desenvolvimento de ferramentas de entrega.
