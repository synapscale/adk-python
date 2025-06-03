#!/usr/bin/env python3
"""
Exemplos Práticos: ADK + LiteLLM
Este arquivo contém exemplos funcionais do guia ADK_LITELLM_GUIDE.md
"""

import os
import asyncio
import warnings
import logging
from typing import List, Dict, Any

# Configuração inicial
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

# Importações do ADK
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# Carregar variáveis de ambiente (opcional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("💡 Dica: Instale python-dotenv para carregar .env automaticamente")


class MultiModelExamples:
    """Classe com exemplos práticos de uso do ADK com LiteLLM"""
    
    def __init__(self):
        """Inicializa os exemplos"""
        self.session_service = InMemorySessionService()
    
    def create_openai_agent(self) -> Agent:
        """Exemplo 1: Agente com OpenAI GPT-4"""
        return Agent(
            model=LiteLlm(model="openai/gpt-4o"),
            name="openai_assistant",
            description="Assistente inteligente usando GPT-4",
            instruction="""
            Você é um assistente útil e inteligente. 
            Responda às perguntas de forma clara e precisa.
            Mantenha suas respostas concisas mas informativas.
            """
        )
    
    def create_claude_agent(self) -> Agent:
        """Exemplo 2: Agente com Anthropic Claude"""
        return Agent(
            model=LiteLlm(model="anthropic/claude-3-sonnet-20240229"),
            name="claude_assistant", 
            description="Assistente usando Claude da Anthropic",
            instruction="""
            Você é um assistente analítico e detalhado.
            Forneça respostas bem estruturadas e fundamentadas.
            Use raciocínio passo a passo quando apropriado.
            """
        )
    
    def create_gemini_agent(self) -> Agent:
        """Exemplo 3: Agente com Gemini"""
        return Agent(
            model=LiteLlm(model="gemini/gemini-2.0-flash-exp"),
            name="gemini_assistant",
            description="Assistente usando Gemini do Google",
            instruction="""
            Você é um assistente criativo e versátil.
            Use suas capacidades multimodais quando apropriado.
            Seja inovador nas suas abordagens.
            """
        )
    
    def create_tool_agent(self) -> Agent:
        """Exemplo 4: Agente com ferramentas personalizadas"""
        
        def calcular_fibonacci(n: int) -> List[int]:
            """Calcula a sequência de Fibonacci até n termos."""
            if n <= 0:
                return []
            elif n == 1:
                return [0]
            elif n == 2:
                return [0, 1]
            
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[i-1] + fib[i-2])
            return fib
        
        def analisar_numeros(numeros: List[int]) -> Dict[str, Any]:
            """Analisa uma lista de números e retorna estatísticas."""
            if not numeros:
                return {"erro": "Lista vazia"}
            
            return {
                "quantidade": len(numeros),
                "soma": sum(numeros),
                "média": sum(numeros) / len(numeros),
                "mínimo": min(numeros),
                "máximo": max(numeros),
                "pares": len([n for n in numeros if n % 2 == 0]),
                "ímpares": len([n for n in numeros if n % 2 == 1])
            }
        
        return Agent(
            model=LiteLlm(model="openai/gpt-4o"),
            name="math_assistant",
            description="Assistente matemático com ferramentas especializadas",
            instruction="""
            Você é um assistente especializado em matemática.
            Use as ferramentas disponíveis para realizar cálculos.
            Explique os resultados de forma educativa e interessante.
            """,
            tools=[calcular_fibonacci, analisar_numeros]
        )
    
    async def run_agent_conversation(self, agent: Agent, message: str) -> str:
        """Executa uma conversa com um agente"""
        
        # Configurar runner
        runner = Runner(
            app_name="exemplo_multi_modelo",
            agent=agent,
            session_service=self.session_service
        )
        
        # Criar sessão
        session = await runner.session_service.create_session(
            app_name="exemplo_multi_modelo",
            user_id="usuario_teste"
        )
        
        # Criar mensagem
        user_message = types.Content(
            role="user",
            parts=[types.Part.from_text(message)]
        )
        
        # Executar agente e coletar resposta
        response_text = ""
        async for event in runner.run_async(
            user_id=session.user_id,
            session_id=session.id,
            new_message=user_message
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        response_text += part.text
        
        return response_text
    
    async def compare_models(self, prompt: str):
        """Exemplo 5: Comparar respostas de diferentes modelos"""
        
        agents = [
            ("OpenAI GPT-4", self.create_openai_agent()),
            ("Anthropic Claude", self.create_claude_agent()),
            ("Google Gemini", self.create_gemini_agent())
        ]
        
        print(f"🤖 Comparando modelos com o prompt: '{prompt}'\n")
        print("=" * 80)
        
        for name, agent in agents:
            print(f"\n🔸 {name}")
            print("-" * 40)
            
            try:
                response = await self.run_agent_conversation(agent, prompt)
                print(f"Resposta: {response[:200]}...")
                if len(response) > 200:
                    print("(resposta truncada)")
                    
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        print("\n" + "=" * 80)
    
    def test_model_connectivity(self):
        """Exemplo 6: Teste de conectividade com diferentes modelos"""
        
        models_to_test = [
            ("OpenAI GPT-4", "openai/gpt-4o"),
            ("OpenAI GPT-4 Mini", "openai/gpt-4o-mini"), 
            ("Anthropic Claude Sonnet", "anthropic/claude-3-sonnet-20240229"),
            ("Anthropic Claude Haiku", "anthropic/claude-3-haiku-20240307"),
            ("Google Gemini Flash", "gemini/gemini-2.0-flash-exp"),
            ("Google Gemini Pro", "gemini/gemini-1.5-pro")
        ]
        
        print("🔍 Testando conectividade com modelos...")
        print("=" * 60)
        
        for name, model_id in models_to_test:
            try:
                agent = Agent(
                    model=LiteLlm(model=model_id),
                    name=f"test_{name.lower().replace(' ', '_')}",
                    description=f"Teste para {name}"
                )
                print(f"✅ {name}: Modelo inicializado com sucesso")
                
            except Exception as e:
                print(f"❌ {name}: Erro - {str(e)[:60]}...")
        
        print("=" * 60)
    
    def check_api_keys(self):
        """Exemplo 7: Verificar configuração de chaves de API"""
        
        required_keys = {
            "OPENAI_API_KEY": "OpenAI (GPT-4, GPT-3.5)",
            "ANTHROPIC_API_KEY": "Anthropic (Claude)", 
            "GOOGLE_API_KEY": "Google AI (Gemini)",
            "GOOGLE_CLOUD_PROJECT": "Google Cloud (Vertex AI)",
            "COHERE_API_KEY": "Cohere",
            "MISTRAL_API_KEY": "Mistral AI"
        }
        
        print("🔑 Verificando configuração de chaves de API...")
        print("=" * 60)
        
        configured_count = 0
        for key, service in required_keys.items():
            value = os.getenv(key)
            if value:
                print(f"✅ {service}: Configurada")
                configured_count += 1
            else:
                print(f"⚠️  {service}: Não configurada ({key})")
        
        print("=" * 60)
        print(f"📊 {configured_count}/{len(required_keys)} serviços configurados")
        
        if configured_count == 0:
            print("\n💡 Dica: Configure pelo menos uma chave de API para usar os exemplos")
            print("   Você pode criar um arquivo .env na raiz do projeto:")
            print("   ")
            print("   OPENAI_API_KEY=sua_chave_aqui")
            print("   ANTHROPIC_API_KEY=sua_chave_aqui")
            print("   GOOGLE_API_KEY=sua_chave_aqui")


async def run_examples():
    """Função principal para executar os exemplos"""
    
    examples = MultiModelExamples()
    
    print("🚀 Exemplos Práticos: ADK + LiteLLM")
    print("=" * 80)
    
    # Verificar chaves de API
    examples.check_api_keys()
    print()
    
    # Testar conectividade
    examples.test_model_connectivity()
    print()
    
    # Exemplo de conversa (apenas se houver chaves configuradas)
    if os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY") or os.getenv("GOOGLE_API_KEY"):
        print("💬 Exemplo de conversa com agente...")
        print("=" * 60)
        
        # Usar o primeiro modelo disponível
        agent = None
        if os.getenv("OPENAI_API_KEY"):
            agent = examples.create_openai_agent()
            model_name = "OpenAI GPT-4"
        elif os.getenv("ANTHROPIC_API_KEY"):
            agent = examples.create_claude_agent()
            model_name = "Anthropic Claude"
        elif os.getenv("GOOGLE_API_KEY"):
            agent = examples.create_gemini_agent()
            model_name = "Google Gemini"
        
        if agent:
            try:
                response = await examples.run_agent_conversation(
                    agent, 
                    "Olá! Você pode me explicar brevemente o que é inteligência artificial?"
                )
                print(f"🤖 {model_name}: {response}")
            except Exception as e:
                print(f"❌ Erro na conversa: {e}")
    else:
        print("⚠️  Nenhuma chave de API configurada - pulando exemplo de conversa")
    
    print("\n✨ Exemplos concluídos!")
    print("📚 Consulte o arquivo ADK_LITELLM_GUIDE.md para mais detalhes")


if __name__ == "__main__":
    # Executar exemplos
    asyncio.run(run_examples())
