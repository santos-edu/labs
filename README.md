# Labs

Repositório público de laboratórios SRE/Plataforma. Cada laboratório contém requisitos, código, testes e resultados documentados.

## Objetivo

Centralizar artefatos de experimentos técnicos e documentar aprendizados, validações e decisões.

## Estrutura do repositório

```
├── labs/
│   └── YYYY-MM-tema/          # Cada laboratório semanal
│       ├── PRD.md             # Documento de requisitos do laboratório
│       ├── README.md          # Execução e validação do laboratório
│       ├── lab-checklist.md   # Checklist de entrega
│       ├── insight-checklist.md # Insights e aprendizados
│       ├── post.md            # Resumo de resultados
│       ├── infra/             # Infraestrutura do laboratório
│       ├── src/               # Código do laboratório
│       └── tests/             # Scripts e validações
├── templates/
│   ├── PRD.md                 # Template base de PRD
│   └── README.md              # Instruções de uso do template
├── .gitignore
└── README.md
```

## Como evoluir um laboratório

1. Crie um novo diretório `labs/YYYY-MM-tema/` para o laboratório.
2. Preencha `PRD.md` com o problema, tarefas, critérios de sucesso e limites.
3. Atualize `README.md` com execução, dependências e validação.
4. Faça testes em `tests/` e documente-os.
5. Preencha `insight-checklist.md` com aprendizados.
6. Use `post.md` para consolidar resultados e conclusões.
7. Commit e push das alterações no repositório.

## Boas práticas

- Mantenha cada laboratório autocontido.
- Use nomes de diretório `YYYY-MM-tema` para facilitar ordenação cronológica.
- Documente causas, decisões e limitações em `PRD.md` e `README.md`.
- Valorize o histórico: cada commit deve refletir progresso claro.
