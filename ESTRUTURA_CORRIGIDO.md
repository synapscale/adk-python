# 📁 Estrutura do Repositório ADK Python

Este documento descreve a organização do repositório após a reorganização.

## 🗂️ Estrutura de Diretórios

```text
adk-python/
├── 📁 src/                          # Código fonte principal do ADK
│   └── google/adk/                  # Pacote principal
├── 📁 tests/                        # Testes automatizados
│   ├── integration/                 # Testes de integração
│   └── unittests/                   # Testes unitários
├── 📁 examples/                     # Exemplos oficiais do ADK
├── 📁 contributing/                 # Guias para contribuidores
│   └── samples/                     # Amostras de código
├── 📁 docs/                         # Documentação oficial
├── 📁 assets/                       # Imagens e recursos
├── 📁 tutorials/                    # 🆕 Tutoriais e demonstrações
│   ├── demos/                       # Scripts de demonstração
│   │   ├── demonstracao_pratica.py
│   │   ├── demonstracao_final_completa.py
│   │   ├── demo_adk_litellm.py
│   │   ├── demo_web_ui.py
│   │   ├── final_demo.py
│   │   └── resumo_executivo.py
│   ├── notebooks/                   # Jupyter Notebooks
│   │   └── ADK_LiteLLM_Tutorial.ipynb
│   └── docs/                        # Documentação em português
│       ├── GUIA_PRATICO_USO.md
│       ├── INDICE_ADK_LITELLM.md
│       ├── INTERFACE_WEB_VISUAL.md
│       ├── PROJETO_COMPLETO.md
│       ├── README_ADK_LITELLM.md
│       ├── RESUMO_FINAL_COMPLETO.md
│       └── adk-docs-tutorials-agent-team.md
├── 📁 scripts/                      # 🆕 Scripts utilitários
│   ├── autoformat.sh               # Script de formatação
│   ├── test_imports.py              # Teste de importações
│   ├── test_installation.py         # Teste de instalação
│   ├── import_libraries.py          # Importação de bibliotecas
│   ├── libraries_ready.py           # Verificação de bibliotecas
│   ├── mostrar_interface.py         # Interface de demonstração
│   └── agent.py                     # Script de agente
├── 📁 config/                       # 🆕 Arquivos de configuração
│   ├── requirements-tutorial.txt    # Dependências dos tutoriais
│   └── pylintrc                     # Configuração do pylint
├── pyproject.toml                   # Configuração do projeto
├── README.md                        # Documentação principal
├── CHANGELOG.md                     # Registro de mudanças
├── CONTRIBUTING.md                  # Guia de contribuição
├── LICENSE                          # Licença do projeto
├── ESTRUTURA.md                     # 🆕 Este arquivo
└── __init__.py                      # Inicialização do pacote
```

## 🎯 Benefícios da Nova Organização

### ✅ Separação Clara de Responsabilidades

- **`src/`**: Código fonte principal do ADK
- **`tutorials/`**: Todo material educativo em um lugar
- **`scripts/`**: Utilitários e ferramentas auxiliares
- **`config/`**: Configurações centralizadas

### ✅ Facilita a Navegação

- Desenvolvedores encontram rapidamente o código principal
- Usuários iniciantes localizam facilmente os tutoriais
- Scripts de manutenção ficam organizados

### ✅ Melhora a Manutenção

- Testes organizados por tipo
- Configurações centralizadas
- Documentação estruturada por idioma/propósito

## 🚀 Como Usar

### Para Desenvolvedores

```bash
# Código principal
cd src/google/adk/

# Executar testes
python -m pytest tests/

# Scripts utilitários
cd scripts/
```

### Para Usuários/Estudantes

```bash
# Tutoriais práticos
cd tutorials/demos/
python demonstracao_pratica.py

# Notebooks interativos
cd tutorials/notebooks/
jupyter notebook ADK_LiteLLM_Tutorial.ipynb

# Documentação em português
cd tutorials/docs/
```

### Para Contribuidores

```bash
# Formatação de código
./scripts/autoformat.sh

# Verificar instalação
python scripts/test_installation.py

# Seguir guias
cat CONTRIBUTING.md
```

## 📋 Próximos Passos Sugeridos

1. **Atualizar imports**: Verificar se os scripts movidos precisam de ajustes nos imports
2. **Atualizar documentação**: Revisar links nos arquivos README
3. **Configurar CI/CD**: Ajustar workflows para nova estrutura
4. **Criar aliases**: Scripts de conveniência para tarefas comuns
5. **Documentar APIs**: Melhorar documentação do código fonte

---

Estrutura reorganizada em: $(date)
