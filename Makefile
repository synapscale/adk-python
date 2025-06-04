# Makefile para ADK Python
.PHONY: help install dev-setup test format lint clean demo docs

# Configuração
PYTHON := python3
SRC_DIR := src
TESTS_DIR := tests
TUTORIALS_DIR := tutorials

help: ## Mostra esta ajuda
	@echo "🚀 ADK Python - Comandos Disponíveis"
	@echo "=================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Instala dependências do projeto
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install -r config/requirements-tutorial.txt

dev-setup: ## Configura ambiente de desenvolvimento
	@echo "🔧 Configurando ambiente de desenvolvimento..."
	@export PYTHONPATH="$(PWD)/src:$$PYTHONPATH"
	@echo "✅ PYTHONPATH configurado"

test: ## Executa todos os testes
	@echo "🧪 Executando testes..."
	PYTHONPATH=$(PWD)/src $(PYTHON) -m pytest $(TESTS_DIR)/ -v

test-unit: ## Executa apenas testes unitários
	@echo "🧪 Executando testes unitários..."
	PYTHONPATH=$(PWD)/src $(PYTHON) -m pytest $(TESTS_DIR)/unittests/ -v

test-integration: ## Executa apenas testes de integração
	@echo "🧪 Executando testes de integração..."
	PYTHONPATH=$(PWD)/src $(PYTHON) -m pytest $(TESTS_DIR)/integration/ -v

format: ## Formata código usando autoformat
	@echo "✨ Formatando código..."
	@./scripts/autoformat.sh

lint: ## Executa linting do código
	@echo "🔍 Executando linting..."
	@pylint --rcfile=config/pylintrc $(SRC_DIR)/

clean: ## Remove arquivos temporários
	@echo "🧹 Limpando arquivos temporários..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type d -name "*.egg-info" -exec rm -rf {} +

demo: ## Executa demonstração prática
	@echo "🎯 Executando demonstração prática..."
	@cd $(TUTORIALS_DIR)/demos && PYTHONPATH=$(PWD)/src $(PYTHON) demonstracao_pratica.py

demo-web: ## Executa demonstração web UI
	@echo "🌐 Executando demonstração web..."
	@cd $(TUTORIALS_DIR)/demos && PYTHONPATH=$(PWD)/src $(PYTHON) demo_web_ui.py

check: ## Verifica estrutura do repositório
	@echo "🔍 Verificando estrutura..."
	@PYTHONPATH=$(PWD)/src $(PYTHON) scripts/verificar_reorganizacao.py

docs: ## Gera documentação
	@echo "📚 Gerando documentação..."
	@echo "Estrutura atual salva em ESTRUTURA.md"

notebook: ## Abre Jupyter notebook dos tutoriais
	@echo "📓 Abrindo notebooks..."
	@cd $(TUTORIALS_DIR)/notebooks && jupyter notebook

build: ## Constrói o pacote
	@echo "🔨 Construindo pacote..."
	$(PYTHON) -m build

install-dev: install dev-setup ## Instalação completa para desenvolvimento
	@echo "🎉 Ambiente de desenvolvimento configurado!"

# Comandos combinados
all: clean format lint test ## Executa limpeza, formatação, lint e testes
ci: format lint test ## Pipeline de CI (formatação, lint, testes)

# Informações do projeto
info: ## Mostra informações do projeto
	@echo "📊 Informações do Projeto ADK Python"
	@echo "===================================="
	@echo "📁 Código fonte: $(SRC_DIR)/"
	@echo "🧪 Testes: $(TESTS_DIR)/"
	@echo "🎓 Tutoriais: $(TUTORIALS_DIR)/"
	@echo "⚙️  Configuração: config/"
	@echo "🛠️  Scripts: scripts/"
	@echo ""
	@echo "📈 Estatísticas:"
	@find $(SRC_DIR) -name "*.py" | wc -l | xargs echo "Arquivos Python no src:"
	@find $(TESTS_DIR) -name "*.py" | wc -l | xargs echo "Arquivos de teste:"
	@find $(TUTORIALS_DIR) -name "*.py" | wc -l | xargs echo "Arquivos de tutorial:"
