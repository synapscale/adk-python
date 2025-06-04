from google.adk.agents import Agent
from google.adk.models import LiteLlm

root_agent = Agent(
    name="assistente_brasileiro", 
    model=LiteLlm(model="gpt-4o-mini"),
    instruction="Você é um assistente brasileiro amigável. Responda sempre em português brasileiro com emojis! 😊",
    description="Assistente brasileiro para conversas gerais"
)
