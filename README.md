# Labs

Laboratórios automatizados de SRE/Plataforma — curadoria via n8n + IA (do repositório [lab-constructo](https://github.com/santos-edu/lab-constructo)), execução local segura com agentes, e publicação no Dev.to.

## Estrutura

```
├── labs/
│   └── YYYY-MM-tema/    # Cada laboratório semanal em seu diretório
│       ├── PRD.md        # Documento de requisitos gerado pela IA
│       ├── post.md       # Rascunho do artigo Dev.to (gerado após execução)
│       └── ...           # Manifestos, código, testes
├── templates/
│   └── PRD.md           # Template para PRD
├── .gitignore
└── README.md
```

## Fluxo

1. **n8n na nuvem** — busca Reddit, IA escolhe o tema, abre PR com PRD.md
2. **Máquina local** — `ralph-tui run` lê o PRD, executa o laboratório em sandbox
3. **Publicação** — agente local gera `post.md` e envia rascunho para Dev.to
4. **Segundo cérebro** — Obsidian Git sincroniza aprendizado a cada 10min

## Repositórios

| Repositório | Visibilidade | Finalidade |
|---|---|---|
| [lab-constructo](https://github.com/santos-edu/lab-constructo) | Privado | Infraestrutura, Docker Compose, scripts, configs |
| labs | Público | Código e documentação dos laboratórios |
