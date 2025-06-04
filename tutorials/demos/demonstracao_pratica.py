#!/usr/bin/env python3
"""
🎯 DEMONSTRAÇÃO PRÁTICA: Como Usar o ADK a Seu Favor
Este script mostra na prática como você pode usar todos os recursos disponíveis.
"""

import os
import asyncio
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

def verificar_setup():
    """Verifica se o ambiente está configurado"""
    print("🔍 VERIFICANDO SEU SETUP...")
    print("=" * 50)
    
    # Verificar APIs
    apis_disponiveis = []
    
    if os.getenv("OPENAI_API_KEY"):
        apis_disponiveis.append("✅ OpenAI")
    else:
        print("⚠️  OpenAI API key não configurada")
    
    if os.getenv("GOOGLE_API_KEY"):
        apis_disponiveis.append("✅ Google Gemini")
    else:
        print("⚠️  Google API key não configurada")
    
    if os.getenv("ANTHROPIC_API_KEY"):
        apis_disponiveis.append("✅ Anthropic Claude")
    else:
        print("⚠️  Anthropic API key não configurada")
    
    print(f"\n📊 APIs Configuradas: {len(apis_disponiveis)}/3")
    for api in apis_disponiveis:
        print(f"   {api}")
    
    if len(apis_disponiveis) == 0:
        print("\n💡 SOLUÇÃO RÁPIDA:")
        print("   Configure pelo menos uma API:")
        print("   export OPENAI_API_KEY='sua_chave'")
        print("   export GOOGLE_API_KEY='sua_chave'")
        return False
    
    return True

def mostrar_opcoes_uso():
    """Mostra as principais formas de usar o ADK"""
    print("\n🎯 PRINCIPAIS FORMAS DE USAR O ADK:")
    print("=" * 50)
    
    opcoes = [
        {
            "numero": "1",
            "titulo": "🌐 Interface Web Visual",
            "descricao": "Já está rodando em http://localhost:8000",
            "comando": "# Já ativo! Só acessar o navegador",
            "tempo": "0 minutos",
            "nivel": "Iniciante"
        },
        {
            "numero": "2", 
            "titulo": "🌦️ Tutorial Weather Bot",
            "descricao": "6 passos progressivos de aprendizado",
            "comando": "python contributing/samples/weather_bot_tutorial/step_1_basic_weather_agent.py",
            "tempo": "5-30 minutos",
            "nivel": "Iniciante → Avançado"
        },
        {
            "numero": "3",
            "titulo": "🔧 Agentes Especializados",
            "descricao": "30+ exemplos prontos para usar",
            "comando": "python contributing/samples/google_search_agent/agent.py",
            "tempo": "5-15 minutos cada",
            "nivel": "Intermediário"
        },
        {
            "numero": "4",
            "titulo": "🏗️ Criar Seu Próprio Agente",
            "descricao": "Template personalizado para suas necessidades",
            "comando": "# Use o template que vou mostrar abaixo",
            "tempo": "30-60 minutos",
            "nivel": "Intermediário → Avançado"
        }
    ]
    
    for opcao in opcoes:
        print(f"\n{opcao['numero']}. {opcao['titulo']}")
        print(f"   📝 {opcao['descricao']}")
        print(f"   ⏱️  Tempo: {opcao['tempo']}")
        print(f"   📊 Nível: {opcao['nivel']}")
        print(f"   💻 Comando: {opcao['comando']}")

def criar_agente_exemplo():
    """Cria um agente personalizado como exemplo"""
    print("\n🏗️ CRIANDO AGENTE PERSONALIZADO:")
    print("=" * 50)
    
    # Escolher modelo baseado em APIs disponíveis
    modelo = "gpt-3.5-turbo"
    if os.getenv("GOOGLE_API_KEY"):
        modelo = "gemini/gemini-2.0-flash-exp"
    elif os.getenv("ANTHROPIC_API_KEY"):
        modelo = "anthropic/claude-3-haiku-20240307"
    
    print(f"🤖 Usando modelo: {modelo}")
    
    # Ferramenta personalizada
    def calculadora_avancada(operacao: str, numero1: float, numero2: float) -> str:
        """Calculadora com operações matemáticas básicas"""
        try:
            if operacao == "soma":
                resultado = numero1 + numero2
            elif operacao == "subtracao":
                resultado = numero1 - numero2
            elif operacao == "multiplicacao":
                resultado = numero1 * numero2
            elif operacao == "divisao":
                if numero2 == 0:
                    return "Erro: Divisão por zero não é permitida!"
                resultado = numero1 / numero2
            elif operacao == "potencia":
                resultado = numero1 ** numero2
            else:
                return f"Operação '{operacao}' não suportada. Use: soma, subtracao, multiplicacao, divisao, potencia"
            
            return f"Resultado: {numero1} {operacao} {numero2} = {resultado}"
        except Exception as e:
            return f"Erro no cálculo: {e}"
    
    # Criar agente
    agente_personalizado = Agent(
        name="assistente_matematico",
        model=LiteLlm(model=modelo),
        instruction="""
        Você é um assistente matemático especializado e amigável.
        
        🎯 Suas especialidades:
        - Realizar cálculos precisos usando a ferramenta calculadora
        - Explicar conceitos matemáticos de forma simples
        - Resolver problemas passo a passo
        - Verificar resultados e mostrar o raciocínio
        
        💡 Sempre:
        - Use a calculadora para operações numéricas
        - Explique o raciocínio por trás dos cálculos
        - Seja preciso e didático
        - Ofereça exemplos quando apropriado
        """,
        tools=[calculadora_avancada],
        description="Assistente matemático com calculadora integrada"
    )
    
    print("✅ Agente criado com sucesso!")
    print(f"   Nome: {agente_personalizado.name}")
    print(f"   Modelo: {modelo}")
    print(f"   Ferramentas: calculadora_avancada")
    
    return agente_personalizado

async def testar_agente(agente):
    """Testa o agente criado"""
    print("\n🧪 TESTANDO AGENTE:")
    print("=" * 50)
    
    try:
        # Configurar runner
        runner = Runner(
            app_name="demo_personalizado",
            agent=agente,
            session_service=InMemorySessionService()
        )
        
        # Criar sessão
        session = await runner.session_service.create_session(
            app_name="demo_personalizado",
            user_id="usuario_teste"
        )
        
        # Teste simples
        mensagem_teste = "Calcule 15 multiplicado por 7 e explique o resultado"
        
        print(f"📝 Enviando: '{mensagem_teste}'")
        print("⏳ Aguardando resposta...")
        
        user_message = types.Content(
            role="user",
            parts=[types.Part.from_text(mensagem_teste)]
        )
        
        resposta_completa = ""
        async for event in runner.run_async(
            user_id=session.user_id,
            session_id=session.id,
            new_message=user_message
        ):
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        resposta_completa += part.text
        
        print(f"\n🤖 Resposta do Agente:")
        print("-" * 30)
        print(resposta_completa)
        print("-" * 30)
        
        return True
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        print("💡 Verifique se suas APIs estão configuradas corretamente")
        return False

def mostrar_proximos_passos():
    """Mostra o que fazer a seguir"""
    print("\n🚀 PRÓXIMOS PASSOS RECOMENDADOS:")
    print("=" * 50)
    
    passos = [
        "1. 🌐 Acesse http://localhost:8000 e teste a interface web",
        "2. 🌦️ Execute o Weather Bot Tutorial (6 passos)",
        "3. 🔍 Explore os 30+ agentes de exemplo disponíveis",
        "4. 🏗️ Modifique o agente criado acima para suas necessidades",
        "5. 📚 Leia a documentação completa em docs/ADK_LITELLM_GUIDE.md",
        "6. 🎯 Defina seu caso de uso específico e implemente"
    ]
    
    for passo in passos:
        print(f"   {passo}")
    
    print(f"\n💡 COMANDOS ÚTEIS:")
    print(f"   adk web .                    # Interface web")
    print(f"   python GUIA_PRATICO_USO.py   # Este script")
    print(f"   ls contributing/samples/     # Ver todos os exemplos")

async def main():
    """Função principal da demonstração"""
    print("🎯 DEMONSTRAÇÃO PRÁTICA: ADK A SEU FAVOR")
    print("=" * 60)
    print("Este script mostra como usar todos os recursos disponíveis\n")
    
    # 1. Verificar setup
    setup_ok = verificar_setup()
    
    # 2. Mostrar opções
    mostrar_opcoes_uso()
    
    # 3. Criar agente exemplo
    if setup_ok:
        agente = criar_agente_exemplo()
        
        # 4. Testar agente
        teste_ok = await testar_agente(agente)
        
        if teste_ok:
            print("\n✅ SUCESSO! Seu agente personalizado está funcionando!")
        
    # 5. Próximos passos
    mostrar_proximos_passos()
    
    print(f"\n🎉 RESUMO:")
    print(f"   ✅ Você tem acesso a um ecossistema completo de IA")
    print(f"   ✅ Interface web rodando em http://localhost:8000")
    print(f"   ✅ 30+ agentes de exemplo prontos")
    print(f"   ✅ Tutorial completo em 6 passos")
    print(f"   ✅ Documentação abrangente")
    print(f"\n   🚀 COMECE AGORA: Acesse http://localhost:8000")

if __name__ == "__main__":
    asyncio.run(main())
