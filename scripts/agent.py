#!/usr/bin/env python3
"""
Agente ADK para Interface Web Visual
Este arquivo é necessário para o comando 'adk web' funcionar corretamente.
"""

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

# Configurar modelo (ajuste conforme suas necessidades)
model = LiteLlm(
    model="gpt-3.5-turbo",  # ou qualquer modelo compatível
    temperature=0.7,
    max_tokens=1500,
    api_key=None  # Será lido da variável de ambiente
)

# Criar agente principal
root_agent = Agent(
    name="assistente_web_visual",
    model=model,
    instruction="""
    Você é um assistente AI avançado com interface web visual integrada.
    
    🎯 Suas capacidades incluem:
    - Responder perguntas complexas sobre qualquer tópico
    - Explicar conceitos técnicos de forma clara
    - Ajudar com programação em Python, JavaScript, etc.
    - Criar documentação e tutoriais
    - Resolver problemas de desenvolvimento
    - Fornecer exemplos práticos e código
    
    🌟 Características especiais:
    - Interface web moderna e responsiva
    - Suporte a conversas em tempo real
    - Processamento de múltiplos formatos de entrada
    - Capacidade de debug e análise detalhada
    
    💡 Sempre forneça respostas úteis, precisas e bem estruturadas.
    Use formatação Markdown quando apropriado para melhor legibilidade.
    """,
    description="Assistente AI com interface web visual para demonstração completa do ADK"
)

# Este agente será automaticamente descoberto pelo comando 'adk web'
__all__ = ['root_agent']
