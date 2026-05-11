# Roteamento de workloads de IA por SLO e custo

O pedido parece simples: "mande essa chamada para o melhor backend". Mas em IA, "melhor" muda rápido. Uma requisicao pequena e interativa pode precisar de latencia baixa. Um batch grande pode aceitar esperar, desde que custe pouco. Um prompt enorme nem cabe em qualquer backend.

Esse lab trata roteamento de inferencia como uma decisao de plataforma, nao como um detalhe de aplicacao.

O experimento e pequeno: tres backends falsos e tres requests. Cada backend tem p95, custo por mil tokens, limite de contexto e fila. Cada request traz tokens, budget de latencia e budget de custo.

```bash
docker compose run --rm router
tests/smoke.sh
```

A primeira evidencia aparece no `req-001`: ele escolhe `balanced-gpu`. O `fast-gpu` e mais rapido, mas a fila e o custo tornam a escolha menos atraente. Para `req-002`, o destino e `cheap-cpu`, porque o workload e batch e o budget favorece custo. No `req-003`, o tamanho do contexto elimina backends menores antes de qualquer discussao sobre preco.

O insight principal: infraestrutura de IA precisa expor sinais que aplicacoes tradicionais muitas vezes ignoram. Tokens viram unidade operacional. Custo entra no caminho critico. Latencia precisa ser lida junto com fila e tamanho de contexto.

Isso tambem muda a conversa de plataforma. Nao basta perguntar "tem GPU?". A pergunta melhor e: "qual backend atende este SLO pelo menor custo aceitavel, explicando a decisao?".

O lab nao prova comportamento real de modelos, nem cobre autoscaling ou Kubernetes. Ele mostra a forma do problema: quando IA entra em producao, roteamento vira politica.

Proximo passo: transformar essa politica em um recurso declarativo, como se fosse um pequeno Gateway para inferencia.
