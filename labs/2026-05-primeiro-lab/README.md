# Bootstrap do control plane com n8n e Docker Compose

## Tema

Control plane local para automatizar a criacao e execucao de laboratorios SRE/SWE.

## Objetivo

Validar que o control plane sobe localmente.

## Comandos

```bash
make validate
make up
make ps
curl -I http://localhost:5678
```

## Resultado

- n8n rodando em `http://localhost:5678`;
- PostgreSQL healthy;
- HTTP respondeu `200 OK`.

## Proximo Passo

Verificar o ambiente local e documentar o comportamento observado.
