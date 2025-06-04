#!/usr/bin/env python3
"""
Demonstração Simples: ADK + LiteLLM
Script simplificado para demonstrar o funcionamento básico
"""

import os
import warnings
import sys

# Suprimir warnings
warnings.filterwarnings("ignore")

def main():
    print("🚀 Demonstração: ADK + LiteLLM")
    print("=" * 60)
    
    # 1. Teste de importações
    print("\n📦 Testando importações...")
    try:
        from google.adk import Agent
        from google.adk.models.lite_llm import LiteLlm
        from google.adk.sessions.in_memory_session_service import InMemorySessionService
        from google.adk.runners import Runner
        from google.genai import types
        import litellm
        print("✅ Todas as importações funcionaram!")
    except ImportError as e:
        print(f"❌ Erro na importação: {e}")
        return
    
    # 2. Verificar chaves de API
    print("\n🔑 Verificando chaves de API...")
    api_keys = {
        "OPENAI_API_KEY": "OpenAI",
        "ANTHROPIC_API_KEY": "Anthropic", 
        "GOOGLE_API_KEY": "Google AI"
    }
    
    configured_apis = []
    for key, service in api_keys.items():
        if os.getenv(key):
            print(f"✅ {service}: Configurada")
            configured_apis.append((key, service))
        else:
            print(f"⚠️  {service}: Não configurada")
    
    # 3. Demonstrar criação de agentes
    print("\n🤖 Criando agentes de exemplo...")
    
    agents_examples = [
        ("OpenAI GPT-4", "openai/gpt-4o"),
        ("OpenAI GPT-4 Mini", "openai/gpt-4o-mini"),
        ("Anthropic Claude Sonnet", "anthropic/claude-3-sonnet-20240229"),
        ("Anthropic Claude Haiku", "anthropic/claude-3-haiku-20240307"),
        ("Google Gemini Flash", "gemini/gemini-2.0-flash-exp"),
        ("Google Gemini Pro", "gemini/gemini-1.5-pro")
    ]
    
    created_agents = []
    for name, model_id in agents_examples:
        try:
            agent = Agent(
                model=LiteLlm(model=model_id),
                name=f"demo_{name.lower().replace(' ', '_').replace('-', '_')}",
                description=f"Agente de demonstração usando {name}",
                instruction=f"Você é um assistente inteligente usando {name}."
            )
            print(f"✅ {name}: Agente criado com sucesso")
            created_agents.append((name, agent))
        except Exception as e:
            print(f"❌ {name}: Erro - {str(e)[:50]}...")
    
    # 4. Exemplo de agente com ferramentas
    print("\n🛠️  Criando agente com ferramentas...")
    try:
        def calcular_quadrado(numero: int) -> int:
            """Calcula o quadrado de um número."""
            return numero ** 2
        
        def listar_numeros_pares(limite: int) -> list:
            """Lista números pares até um limite."""
            return [n for n in range(2, limite + 1, 2)]
        
        tool_agent = Agent(
            model=LiteLlm(model="openai/gpt-4o"),
            name="matematico",
            description="Assistente matemático com ferramentas",
            instruction="""
            Você é um assistente matemático especializado.
            Use as ferramentas disponíveis para realizar cálculos.
            Explique seus resultados de forma clara.
            """,
            tools=[calcular_quadrado, listar_numeros_pares]
        )
        print("✅ Agente com ferramentas criado com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao criar agente com ferramentas: {e}")
    
    # 5. Resumo final
    print("\n" + "=" * 60)
    print("📊 RESUMO DA DEMONSTRAÇÃO")
    print("=" * 60)
    print(f"✅ Bibliotecas: ADK e LiteLLM importadas com sucesso")
    print(f"🔑 APIs configuradas: {len(configured_apis)}/3")
    print(f"🤖 Agentes criados: {len(created_agents)}/{len(agents_examples)}")
    
    if len(configured_apis) == 0:
        print("\n💡 PRÓXIMO PASSO:")
        print("   Configure pelo menos uma chave de API para testar conversas:")
        print("   ")
        print("   # Crie um arquivo .env com:")
        print("   OPENAI_API_KEY=sua_chave_openai")
        print("   ANTHROPIC_API_KEY=sua_chave_anthropic")
        print("   GOOGLE_API_KEY=sua_chave_google")
        print("   ")
        print("   # Depois execute os exemplos completos:")
        print("   python examples/multi_model_examples.py")
    else:
        print("\n🎉 TUDO CONFIGURADO!")
        print("   Você pode agora:")
        print("   📚 Consultar: docs/ADK_LITELLM_GUIDE.md")
        print("   💻 Executar: python examples/multi_model_examples.py")
        print("   🔧 Criar seus próprios agentes!")
    
    print("\n🔗 RECURSOS:")
    print("   📖 Guia completo: docs/ADK_LITELLM_GUIDE.md")
    print("   💻 Exemplos práticos: examples/multi_model_examples.py")
    print("   🧪 Teste de validação: python test_installation.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
