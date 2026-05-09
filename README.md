# Labs Monorepo

Laboratórios automatizados de SRE/Plataforma — curadoria via n8n + IA, execução local segura com agentes, e publicação no Dev.to.

## Estrutura

```
├── n8n-server/          # Docker Compose do orquestrador (n8n + PostgreSQL)
├── labs/
│   └── YYYY-MM-tema/    # Cada laboratório semanal em seu diretório
│       ├── PRD.md        # Documento de requisitos gerado pela IA
│       ├── post.md       # Rascunho do artigo Dev.to (gerado após execução)
│       └── ...           # Manifestos, código, testes
├── .gitignore
└── README.md
```

## Fluxo

1. **n8n na nuvem** — busca Reddit, IA escolhe o tema, abre PR com PRD.md
2. **Máquina local** — `ralph-tui run` lê o PRD, executa o laboratório em sandbox
3. **Publicação** — agente local gera `post.md` e envia rascunho para Dev.to
4. **Segundo cérebro** — Obsidian Git sincroniza aprendizado a cada 10min

## Subindo o n8n (Oracle Cloud Free Tier)

```bash
# Na VM da Oracle com Docker instalado:
docker compose -f n8n-server/docker-compose.yml up -d
```

Acessar: `http://<IP-PUBLICO>:5678`
