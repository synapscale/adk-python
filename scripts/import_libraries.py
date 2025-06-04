# @title Import necessary libraries
import os
import asyncio
from google.adk import Agent  # Importação correta do Agent
from google.adk.models.lite_llm import LiteLlm  # For multi-model support
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types  # For creating message Content/Parts

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")
