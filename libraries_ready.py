# @title Import necessary libraries
import os
import asyncio
import warnings
import logging

# Configure warnings and logging
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

# ADK and related imports
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm  # For multi-model support
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types  # For creating message Content/Parts

print("✓ Todas as bibliotecas foram importadas com sucesso!")
print()
print("Bibliotecas disponíveis:")
print("- google.adk.Agent: Para criar agentes")
print("- google.adk.models.lite_llm.LiteLlm: Para suporte a múltiplos modelos")
print("- google.adk.sessions.in_memory_session_service.InMemorySessionService: Para gerenciar sessões")
print("- google.adk.runners.Runner: Para executar agentes")
print("- google.genai.types: Para criar conteúdo de mensagens")
print()
print("Pronto para começar a desenvolver com ADK e LiteLLM!")
