#!/usr/bin/env python3
"""
Demo: Google ADK com Interface Web Visual
Demonstra como criar um agente e utilizar a interface web do ADK para interação visual.
"""

import os
from google.adk import Agent
from google.adk.models import LiteLlm

def create_demo_agent():
    """Cria um agente de demonstração para a interface web."""
    
    # Configurar modelo com LiteLLM
    model = LiteLlm(
        model="gpt-3.5-turbo",  # Você pode usar qualquer modelo compatível
        temperature=0.7,
        max_tokens=1000
    )
    
    # Criar agente
    agent = Agent(
        name="assistente_web",
        model=model,
        instruction="""
        Você é um assistente inteligente e prestativo que pode responder perguntas sobre diversos tópicos.
        
        Suas capacidades incluem:
        - Responder perguntas gerais
        - Explicar conceitos técnicos
        - Fornecer exemplos práticos
        - Ajudar com programação e desenvolvimento
        - Criar conteúdo e textos
        
        Sempre seja útil, preciso e forneça respostas detalhadas quando apropriado.
        """,
        description="Assistente virtual com múltiplas capacidades para demonstração da interface web do ADK"
    )
    
    return agent

if __name__ == "__main__":
    print("🚀 Configurando Agente para Interface Web ADK...")
    
    # Verificar se as variáveis de ambiente estão configuradas
    print("\n📋 Verificando configuração:")
    
    # Exemplo de configuração para OpenAI
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  OPENAI_API_KEY não encontrada. Configure sua chave de API:")
        print("   export OPENAI_API_KEY='sua_chave_aqui'")
        print("\n💡 Ou use outro modelo como Gemini, Anthropic, etc.")
    else:
        print("✅ OPENAI_API_KEY configurada")
    
    # Criar agente
    try:
        agent = create_demo_agent()
        print("✅ Agente criado com sucesso!")
        
        print(f"""
🌐 Para usar a Interface Web Visual do ADK:

1. Abra o terminal
2. Execute o comando:
   adk web .

3. Acesse: http://localhost:8000

📱 Recursos da Interface Web:
- Chat interativo com o agente
- Visualização de conversas
- Debug de respostas
- Teste de diferentes prompts
- Interface moderna e responsiva
- Suporte a áudio (processamento de voz)

💡 Comandos úteis:
- adk web --help          (ver opções)
- adk web --port 3000     (usar porta personalizada)
- adk web --host 0.0.0.0  (permitir acesso externo)

🎯 Funcionalidades da UI:
- Interface Angular moderna
- Suporte a Material Design
- Processamento de áudio
- WebSocket para tempo real
- Visualização de ferramentas
- Debug avançado

        """)
        
    except Exception as e:
        print(f"❌ Erro ao criar agente: {e}")
        print("\n💡 Verifique:")
        print("- Se as dependências estão instaladas")
        print("- Se as chaves de API estão configuradas")
        print("- Se o modelo especificado está disponível")
