# Diagnostico barato de incidentes repetidos

## Tema

SRE: reduzir o custo de diagnosticar incidentes repetidos usando fingerprints e breadcrumbs.

## Rodar

```bash
docker compose run --rm diagnose
```

## Testar

```bash
tests/smoke.sh
```

## O Que Observar

- Incidentes parecidos recebem o mesmo fingerprint.
- O fingerprint aponta para um runbook conhecido.
- Incidente com `deploy_sha` ausente fica mais caro de diagnosticar.
