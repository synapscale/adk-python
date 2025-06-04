# ADK Python - Configuração de Desenvolvimento

# Adicionar src ao PYTHONPATH para imports funcionarem
export PYTHONPATH="${PYTHONPATH}:/workspaces/adk-python/src"

# Variáveis de ambiente para desenvolvimento
export ADK_DEV_MODE=true
export ADK_LOG_LEVEL=DEBUG

# Aliases úteis para desenvolvimento
alias adk-test="python -m pytest tests/"
alias adk-format="./scripts/autoformat.sh"
alias adk-demo="cd tutorials/demos && python demonstracao_pratica.py"
alias adk-check="python scripts/verificar_reorganizacao.py"

echo "🚀 Ambiente ADK configurado!"
echo "📁 PYTHONPATH: $PYTHONPATH"
echo "💡 Use 'adk-demo' para executar demonstrações"
echo "🔧 Use 'adk-test' para executar testes"
echo "✨ Use 'adk-format' para formatar código"
