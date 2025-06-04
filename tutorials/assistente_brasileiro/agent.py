# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent

def get_current_time() -> str:
    """Retorna a data e hora atual do Brasil."""
    import datetime
    from zoneinfo import ZoneInfo
    
    tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.datetime.now(tz)
    return f'Agora são {now.strftime("%d/%m/%Y às %H:%M:%S")} (horário de Brasília)'

def calculadora(a: float, b: float, operacao: str) -> str:
    """Realiza operações matemáticas básicas.
    
    Args:
        a: Primeiro número
        b: Segundo número  
        operacao: Tipo de operação (soma, subtracao, multiplicacao, divisao)
    
    Returns:
        O resultado da operação matemática
    """
    if operacao == "soma":
        return f"{a} + {b} = {a + b}"
    elif operacao == "subtracao":
        return f"{a} - {b} = {a - b}"
    elif operacao == "multiplicacao":
        return f"{a} × {b} = {a * b}"
    elif operacao == "divisao":
        if b != 0:
            return f"{a} ÷ {b} = {a / b}"
        else:
            return "Erro: Não é possível dividir por zero!"
    else:
        return "Operação não suportada. Use: soma, subtracao, multiplicacao ou divisao"

root_agent = Agent(
    name="assistente_brasileiro",
    model="gemini-2.0-flash-exp",
    description=(
        "Assistente brasileiro amigável que pode conversar, "
        "informar horários e fazer cálculos matemáticos."
    ),
    instruction="""
    Você é um assistente brasileiro super amigável e prestativo! 🇧🇷
    
    Suas características:
    - Sempre responda em português brasileiro
    - Use emojis quando apropriado para ser mais expressivo
    - Seja educado, simpático e use gírias brasileiras quando natural
    - Ajude com qualquer pergunta ou tarefa que o usuário tiver
    - Quando perguntarem sobre horário, use a ferramenta get_current_time
    - Para cálculos matemáticos, use a ferramenta calculadora
    - Seja criativo e útil nas suas respostas
    - Mostre interesse genuíno pelas perguntas do usuário
    
    Exemplos de como se comportar:
    - "Oi! Tudo bem? Como posso te ajudar hoje? 😊"
    - "Que legal! Vou calcular isso para você!"
    - "Opa, deixa eu ver que horas são aí no Brasil!"
    """,
    tools=[get_current_time, calculadora],
)
