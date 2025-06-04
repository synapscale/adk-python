#!/usr/bin/env python3
"""
Teste Rápido: Validação da Instalação ADK + LiteLLM
Execute este script para verificar se tudo está configurado corretamente.
"""

import sys
import os
from typing import Dict, List

def test_imports() -> Dict[str, bool]:
    """Testa as importações necessárias"""
    results = {}
    
    # Testar importações básicas
    try:
        from google.adk import Agent
        results["google.adk.Agent"] = True
    except ImportError as e:
        results["google.adk.Agent"] = False
        print(f"❌ Erro ao importar Agent: {e}")
    
    try:
        from google.adk.models.lite_llm import LiteLlm
        results["google.adk.models.lite_llm.LiteLlm"] = True
    except ImportError as e:
        results["google.adk.models.lite_llm.LiteLlm"] = False
        print(f"❌ Erro ao importar LiteLlm: {e}")
    
    try:
        from google.adk.sessions.in_memory_session_service import InMemorySessionService
        results["InMemorySessionService"] = True
    except ImportError as e:
        results["InMemorySessionService"] = False
        print(f"❌ Erro ao importar InMemorySessionService: {e}")
    
    try:
        from google.adk.runners import Runner
        results["google.adk.runners.Runner"] = True
    except ImportError as e:
        results["google.adk.runners.Runner"] = False
        print(f"❌ Erro ao importar Runner: {e}")
    
    try:
        from google.genai import types
        results["google.genai.types"] = True
    except ImportError as e:
        results["google.genai.types"] = False
        print(f"❌ Erro ao importar types: {e}")
    
    try:
        import litellm
        results["litellm"] = True
    except ImportError as e:
        results["litellm"] = False
        print(f"❌ Erro ao importar litellm: {e}")
    
    return results

def check_api_keys() -> Dict[str, bool]:
    """Verifica se as chaves de API estão configuradas"""
    keys_to_check = {
        "OPENAI_API_KEY": "OpenAI",
        "ANTHROPIC_API_KEY": "Anthropic", 
        "GOOGLE_API_KEY": "Google AI",
        "GOOGLE_CLOUD_PROJECT": "Google Cloud",
        "COHERE_API_KEY": "Cohere",
        "MISTRAL_API_KEY": "Mistral AI"
    }
    
    results = {}
    for key, service in keys_to_check.items():
        results[service] = bool(os.getenv(key))
    
    return results

def test_agent_creation() -> Dict[str, bool]:
    """Testa a criação de agentes básicos"""
    results = {}
    
    try:
        from google.adk import Agent
        from google.adk.models.lite_llm import LiteLlm
        
        # Teste com modelo OpenAI (mesmo sem chave, deve criar o objeto)
        agent = Agent(
            model=LiteLlm(model="openai/gpt-4o"),
            name="test_agent",
            description="Agente de teste"
        )
        results["Criação de Agente OpenAI"] = True
        
    except Exception as e:
        results["Criação de Agente OpenAI"] = False
        print(f"❌ Erro ao criar agente OpenAI: {e}")
    
    try:
        from google.adk import Agent
        from google.adk.models.lite_llm import LiteLlm
        
        # Teste com modelo Anthropic
        agent = Agent(
            model=LiteLlm(model="anthropic/claude-3-sonnet-20240229"),
            name="test_claude",
            description="Agente Claude de teste"
        )
        results["Criação de Agente Claude"] = True
        
    except Exception as e:
        results["Criação de Agente Claude"] = False
        print(f"❌ Erro ao criar agente Claude: {e}")
    
    return results

def print_results(title: str, results: Dict[str, bool]):
    """Imprime os resultados de forma organizada"""
    print(f"\n📋 {title}")
    print("=" * 60)
    
    success_count = 0
    for item, success in results.items():
        status = "✅" if success else "❌"
        print(f"{status} {item}")
        if success:
            success_count += 1
    
    print("-" * 60)
    print(f"✅ {success_count}/{len(results)} itens passaram no teste")
    
    return success_count == len(results)

def main():
    """Função principal do teste"""
    print("🔍 Teste de Validação: ADK + LiteLLM")
    print("=" * 80)
    print("Este script verifica se a instalação está funcionando corretamente.")
    print()
    
    # Informações do Python
    print(f"🐍 Python: {sys.version}")
    print(f"📁 Diretório atual: {os.getcwd()}")
    print()
    
    # Teste de importações
    import_results = test_imports()
    imports_ok = print_results("Importações", import_results)
    
    # Verificação de chaves de API
    api_results = check_api_keys()
    apis_ok = print_results("Chaves de API Configuradas", api_results)
    
    # Teste de criação de agentes
    if imports_ok:
        agent_results = test_agent_creation()
        agents_ok = print_results("Criação de Agentes", agent_results)
    else:
        agents_ok = False
        print("\n⚠️  Pulando teste de criação de agentes devido a erros de importação")
    
    # Resumo final
    print("\n" + "=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    
    if imports_ok:
        print("✅ Importações: SUCESSO - Todas as bibliotecas estão funcionando")
    else:
        print("❌ Importações: FALHA - Problemas com bibliotecas")
    
    api_count = sum(api_results.values())
    if api_count > 0:
        print(f"✅ APIs: {api_count} serviços configurados")
    else:
        print("⚠️  APIs: Nenhuma chave configurada (opcional para testes)")
    
    if agents_ok:
        print("✅ Agentes: SUCESSO - Criação de agentes funcionando")
    else:
        print("❌ Agentes: FALHA - Problemas na criação de agentes")
    
    # Recomendações
    print("\n💡 PRÓXIMOS PASSOS:")
    if not imports_ok:
        print("   1. Reinstale as dependências: pip install google-adk litellm")
        print("   2. Verifique se está no ambiente Python correto")
    elif api_count == 0:
        print("   1. Configure pelo menos uma chave de API no arquivo .env")
        print("   2. Execute: python examples/multi_model_examples.py")
    else:
        print("   ✨ Tudo configurado! Execute os exemplos:")
        print("   📚 python examples/multi_model_examples.py")
        print("   📖 Consulte: docs/ADK_LITELLM_GUIDE.md")
    
    print("\n🎯 Status geral:", "PRONTO PARA USO" if (imports_ok and agents_ok) else "PRECISA DE AJUSTES")
    print("=" * 80)

if __name__ == "__main__":
    main()
