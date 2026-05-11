# Bootstrap do control plane com n8n e Docker Compose

## Contexto

Tema do laboratorio: criar a base local do control plane para automatizar laboratorios SRE/SWE.

Primeiro passo do projeto: provar que n8n e PostgreSQL sobem com Docker Compose antes de automatizar workflows.

## Execucao

```bash
make validate
make up
make ps
curl -I http://localhost:5678
```

## Resultado

O n8n subiu com PostgreSQL via Docker Compose. O endpoint local respondeu `200 OK`.

## Aprendizado

Antes de criar workflows e automacoes, o ambiente base precisa estar simples e reproduzivel.
