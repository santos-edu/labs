# PRD: 2026-05-hello-sre

## Objetivo
Validar o fluxo completo de laboratório: estrutura, execução local em container, e geração de resultado em Markdown.

## Tarefas
- [ ] Criar um `docker-compose.yml` com nginx e uma página HTML simples
- [ ] Subir o ambiente e verificar que o nginx responde na porta 8080
- [ ] Adicionar healthcheck e dependência entre serviços
- [ ] Gerar `result.md` documentando o que foi feito, problemas encontrados e aprendizados

## Critérios de Sucesso
- `curl localhost:8080` retorna HTTP 200 com a página customizada
- Todos os contêineres sobem com saúde OK
- `result.md` é gerado na raiz do laboratório

## Recursos
- https://docs.docker.com/compose/
