# PRD: Fragmentacao de observabilidade cloud native

## Tema

Por que times SRE ainda rodam multiplas stacks de observabilidade e como reduzir isso com um caminho simples baseado em OpenTelemetry.

## Objetivo

Montar um lab local minimo que mostre metricas, logs e traces separados, documentando o problema de fragmentacao.

## Escopo MVP

- Criar um app pequeno que exponha endpoint HTTP;
- rodar preferencialmente via container;
- gerar log estruturado;
- expor metrica simples;
- preparar instrumentacao basica com OpenTelemetry;
- documentar o que fica fragmentado e o que pode ser padronizado.

## Fora de Escopo

- Kubernetes;
- ambiente cloud;
- stack completa de producao;
- dashboards sofisticados.

## Aceite

- [x] README explica como rodar;
- [x] app local funciona;
- [x] evidencias de log/metrica/trace ficam documentadas;
- [x] `post.md` resume aprendizados.
