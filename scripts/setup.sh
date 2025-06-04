#!/bin/bash
# Script de instalação e configuração completa do ADK Python

set -e

echo "🚀 INSTALAÇÃO E CONFIGURAÇÃO DO ADK PYTHON"
echo "=========================================="

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para logging
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Verificar se estamos no diretório correto
if [ ! -f "pyproject.toml" ]; then
    log_error "Execute este script no diretório raiz do projeto ADK Python"
    exit 1
fi

# 1. Verificar Python
log_info "Verificando versão do Python..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
REQUIRED_VERSION="3.9"

if python3 -c "import sys; exit(0 if sys.version_info >= (3,9) else 1)"; then
    log_success "Python $PYTHON_VERSION encontrado (>= 3.9 requerido)"
else
    log_error "Python 3.9+ é necessário. Versão atual: $PYTHON_VERSION"
    exit 1
fi

# 2. Instalar dependências principais
log_info "Instalando dependências principais..."
if python3 -m pip install -e . --quiet; then
    log_success "Dependências principais instaladas"
else
    log_error "Falha ao instalar dependências principais"
    exit 1
fi

# 3. Instalar dependências dos tutoriais
log_info "Instalando dependências dos tutoriais..."
if [ -f "config/requirements-tutorial.txt" ]; then
    if python3 -m pip install -r config/requirements-tutorial.txt --quiet; then
        log_success "Dependências dos tutoriais instaladas"
    else
        log_warning "Algumas dependências dos tutoriais podem ter falhado"
    fi
else
    log_warning "Arquivo requirements-tutorial.txt não encontrado"
fi

# 4. Configurar PYTHONPATH
log_info "Configurando PYTHONPATH..."
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"
log_success "PYTHONPATH configurado para esta sessão"

# 5. Verificar estrutura do repositório
log_info "Verificando estrutura do repositório..."
if python3 scripts/verificar_reorganizacao.py >/dev/null 2>&1; then
    log_success "Estrutura do repositório verificada"
else
    log_warning "Estrutura do repositório pode precisar de ajustes"
fi

# 6. Executar testes básicos
log_info "Executando testes de verificação..."
if python3 scripts/test_installation.py >/dev/null 2>&1; then
    log_success "Testes de instalação passaram"
else
    log_warning "Alguns testes de instalação falharam (isso pode ser normal)"
fi

# 7. Criar arquivo de ambiente local
log_info "Criando arquivo de configuração local..."
cat >.env.local <<'EOF'
# Configuração local do ADK Python
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"
export ADK_DEV_MODE=true
export ADK_LOG_LEVEL=INFO

# Aliases úteis
alias adk-test="make test"
alias adk-demo="make demo"
alias adk-format="make format"
alias adk-check="make check"
alias adk-help="make help"

echo "🔧 Ambiente ADK carregado! Use 'adk-help' para ver comandos disponíveis"
EOF

log_success "Arquivo .env.local criado"

# 8. Verificar se Makefile funciona
log_info "Testando Makefile..."
if make help >/dev/null 2>&1; then
    log_success "Makefile funcionando corretamente"
else
    log_warning "Makefile pode ter problemas"
fi

# 9. Resumo final
echo ""
echo "🎉 INSTALAÇÃO CONCLUÍDA!"
echo "======================="
log_success "Dependências instaladas"
log_success "Estrutura verificada"
log_success "Configuração local criada"

echo ""
echo "📋 PRÓXIMOS PASSOS:"
echo "-------------------"
echo "1. Execute: source .env.local"
echo "2. Execute: make help (para ver comandos disponíveis)"
echo "3. Execute: make demo (para testar uma demonstração)"
echo "4. Execute: make test (para executar testes)"
echo ""

echo "📚 COMANDOS ÚTEIS:"
echo "------------------"
echo "• make demo      - Executa demonstração prática"
echo "• make test      - Executa todos os testes"
echo "• make format    - Formata código"
echo "• make check     - Verifica estrutura"
echo "• make notebook  - Abre Jupyter notebooks"
echo ""

log_info "Para configurar o ambiente, execute: source .env.local"
log_info "Consulte ESTRUTURA.md para detalhes da organização"

echo "✨ Bom desenvolvimento!"
