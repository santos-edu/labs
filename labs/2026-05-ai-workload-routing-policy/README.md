# Roteamento de workloads de IA por SLO e custo

## Rodar

```bash
docker compose run --rm router
```

## Testar

```bash
tests/smoke.sh
```

## O Que Observar

- Requisicao interativa prefere backend que cabe em latencia e custo.
- Batch pode ir para backend mais barato.
- Contexto grande elimina backends pequenos.
- A decisao fica explicavel, nao magica.
