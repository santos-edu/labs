# Labs

Repositório público de laboratórios SRE/Plataforma. Cada laboratório contém requisitos, código, testes e o rascunho de publicação.

## Objetivo

Este repositório centraliza os resultados dos laboratórios criados pelo fluxo de `lab-constructo`:

- `lab-constructo` gera e gerencia a criação de novos laboratórios.
- `labs` mantém os artefatos finais: `PRD.md`, `README.md`, `post.md`, testes e evidências.
- O objetivo é documentar experimentos semanais e permitir revisão humana antes de publicar.

## Estrutura do repositório

```
├── labs/
│   └── YYYY-MM-tema/          # Cada laboratório semanal
│       ├── PRD.md             # Documento de requisitos do laboratório
│       ├── README.md          # Execução e validação do laboratório
│       ├── lab-checklist.md   # Checklist de entrega
│       ├── insight-checklist.md # Insights e aprendizados
│       ├── post.md            # Rascunho do artigo Dev.to
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

1. Crie o laboratório com `lab-constructo`:
   - `cd ../lab-constructo`
   - `make lab NAME=tema-curto`
2. Preencha `PRD.md` com o problema, tarefas, critérios de sucesso e limites.
3. Atualize `README.md` com execução, dependências e validação.
4. Faça testes em `tests/` e documente-os.
5. Preencha `insight-checklist.md` com aprendizados.
6. Edite `post.md` como rascunho humano para o Dev.to.
7. Commit e push no repositório `labs`.

## Observação sobre `post.md`

Os arquivos `post.md` são parte do fluxo e devem ser versionados. A configuração em `.gitignore` foi ajustada para preservar esses rascunhos.

## Boas práticas

- Mantenha cada laboratório autocontido.
- Use nomes de diretório `YYYY-MM-tema` para facilitar ordenação cronológica.
- Documente causas, decisões e limitações em `PRD.md` e `README.md`.
- Valorize o histórico: cada commit deve refletir progresso claro.

## Repositórios relacionados

- `lab-constructo` — control plane de criação de laboratórios
- `labs` — resultados dos laboratórios e rascunhos de publicação
