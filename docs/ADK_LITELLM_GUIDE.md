# Guia Completo: ADK + LiteLLM para Suporte Multi-Modelo

Este guia fornece um passo a passo completo para usar o Google Agent Development Kit (ADK) com LiteLLM, permitindo suporte a múltiplos modelos de linguagem como OpenAI, Anthropic, Gemini e outros.

## 📋 Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração Básica](#configuração-básica)
- [Exemplos Práticos](#exemplos-práticos)
- [Modelos Suportados](#modelos-suportados)
- [Configurações Avançadas](#configurações-avançadas)
- [Troubleshooting](#troubleshooting)
- [Recursos Adicionais](#recursos-adicionais)

## 🔧 Pré-requisitos

- Python 3.8 ou superior
- Acesso às APIs dos modelos que deseja usar (OpenAI, Anthropic, etc.)
- Chaves de API configuradas

## 📦 Instalação

### Passo 1: Instalação das Bibliotecas

```bash
# Instalar Google ADK
pip install google-adk

# Instalar LiteLLM para suporte multi-modelo
pip install litellm
```

### Passo 2: Verificação da Instalação

```python
# Teste de importação
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

print("✓ Todas as bibliotecas importadas com sucesso!")
```

## ⚙️ Configuração Básica

### Configuração de Variáveis de Ambiente

Crie um arquivo `.env` no seu projeto:

```bash
# OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui

# Anthropic
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui

# Google AI
GOOGLE_API_KEY=sua_chave_google_aqui

# Vertex AI (se usando Google Cloud)
GOOGLE_CLOUD_PROJECT=seu_projeto_gcp
GOOGLE_CLOUD_LOCATION=us-central1
```

### Script de Configuração Inicial

```python
import os
import asyncio
import warnings
import logging
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurar warnings e logging
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

# Importações do ADK
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
```

## 💡 Exemplos Práticos

### Exemplo 1: Agente Simples com OpenAI GPT-4

```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

# Criar agente com GPT-4
openai_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="openai_assistant",
    description="Assistente inteligente usando GPT-4",
    instruction="""
    Você é um assistente útil e inteligente. 
    Responda às perguntas de forma clara e precisa.
    """
)
```

### Exemplo 2: Agente com Anthropic Claude

```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

# Criar agente com Claude
claude_agent = Agent(
    model=LiteLlm(model="anthropic/claude-3-sonnet-20240229"),
    name="claude_assistant", 
    description="Assistente usando Claude da Anthropic",
    instruction="""
    Você é um assistente analítico e detalhado.
    Forneça respostas bem estruturadas e fundamentadas.
    """
)
```

### Exemplo 3: Agente com Gemini

```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

# Criar agente com Gemini
gemini_agent = Agent(
    model=LiteLlm(model="gemini/gemini-2.0-flash-exp"),
    name="gemini_assistant",
    description="Assistente usando Gemini do Google",
    instruction="""
    Você é um assistente criativo e versátil.
    Use suas capacidades multimodais quando apropriado.
    """
)
```

### Exemplo 4: Sistema Multi-Agente com Diferentes Modelos

```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.agents.sequential_agent import SequentialAgent

# Agente especialista em análise (Claude)
analyst_agent = Agent(
    model=LiteLlm(model="anthropic/claude-3-sonnet-20240229"),
    name="analyst",
    description="Especialista em análise de dados",
    instruction="Analise os dados fornecidos e identifique padrões importantes."
)

# Agente especialista em escrita (GPT-4)
writer_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="writer",
    description="Especialista em redação e comunicação",
    instruction="Transforme análises técnicas em texto claro e acessível."
)

# Agente coordenador (Gemini)
coordinator = SequentialAgent(
    model=LiteLlm(model="gemini/gemini-2.0-flash-exp"),
    name="coordinator",
    description="Coordena o trabalho entre especialistas",
    instruction="Coordene o trabalho entre os agentes especializados.",
    sub_agents=[analyst_agent, writer_agent]
)
```

### Exemplo 5: Agente com Ferramentas Personalizadas

```python
import random
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

def roll_dice(sides: int = 6) -> int:
    """Rola um dado com o número especificado de lados."""
    return random.randint(1, sides)

def calculate_stats(numbers: list[int]) -> dict:
    """Calcula estatísticas básicas de uma lista de números."""
    if not numbers:
        return {"error": "Lista vazia"}
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

# Agente com ferramentas
dice_agent = Agent(
    model=LiteLlm(model="openai/gpt-4o"),
    name="dice_master",
    description="Especialista em jogos de dados e estatísticas",
    instruction="""
    Você é um especialista em jogos de dados.
    Use as ferramentas disponíveis para rolar dados e calcular estatísticas.
    Sempre explique os resultados de forma interessante.
    """,
    tools=[roll_dice, calculate_stats]
)
```

### Exemplo 6: Executando um Agente

```python
import asyncio
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

async def run_agent_example():
    # Configurar runner
    runner = Runner(
        app_name="meu_app",
        agent=openai_agent,  # Use qualquer agente criado acima
        session_service=InMemorySessionService()
    )
    
    # Criar sessão
    session = await runner.session_service.create_session(
        app_name="meu_app",
        user_id="usuario_teste"
    )
    
    # Criar mensagem
    message = types.Content(
        role="user",
        parts=[types.Part.from_text("Olá! Como você pode me ajudar?")]
    )
    
    # Executar agente
    response_events = []
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=message
    ):
        response_events.append(event)
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(f"Agente: {part.text}")

# Executar o exemplo
asyncio.run(run_agent_example())
```

## 🌐 Modelos Suportados

### OpenAI

```python
# GPT-4 variants
LiteLlm(model="openai/gpt-4o")
LiteLlm(model="openai/gpt-4o-mini")
LiteLlm(model="openai/gpt-4-turbo")

# GPT-3.5
LiteLlm(model="openai/gpt-3.5-turbo")
```

### Anthropic

```python
# Claude 3 family
LiteLlm(model="anthropic/claude-3-opus-20240229")
LiteLlm(model="anthropic/claude-3-sonnet-20240229")
LiteLlm(model="anthropic/claude-3-haiku-20240307")

# Claude 3.5
LiteLlm(model="anthropic/claude-3-5-sonnet-20241022")
LiteLlm(model="anthropic/claude-3-5-haiku-20241022")
```

### Google Gemini

```python
# Gemini Pro
LiteLlm(model="gemini/gemini-2.0-flash-exp")
LiteLlm(model="gemini/gemini-1.5-pro")
LiteLlm(model="gemini/gemini-1.5-flash")

# Vertex AI
LiteLlm(model="vertex_ai/gemini-2.0-flash-exp")
LiteLlm(model="vertex_ai/claude-3-5-sonnet")
```

### Outros Modelos

```python
# Cohere
LiteLlm(model="cohere/command-r-plus")

# Mistral
LiteLlm(model="mistral/mistral-large-latest")

# Local/Ollama
LiteLlm(model="ollama/llama2")
```

## ⚡ Configurações Avançadas

### Configuração de Parâmetros do Modelo

```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

# Agente com configurações customizadas
advanced_agent = Agent(
    model=LiteLlm(
        model="openai/gpt-4o",
        temperature=0.7,
        max_tokens=2048,
        top_p=0.9
    ),
    name="advanced_assistant",
    description="Assistente com configurações avançadas",
    instruction="Seja criativo mas preciso nas respostas.",
    generate_content_config=types.GenerateContentConfig(
        temperature=0.7,
        candidate_count=1,
        max_output_tokens=2048
    )
)
```

### Fallback entre Modelos

```python
import asyncio
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

class MultiModelAgent:
    def __init__(self):
        self.primary_agent = Agent(
            model=LiteLlm(model="openai/gpt-4o"),
            name="primary",
            description="Agente principal"
        )
        
        self.fallback_agent = Agent(
            model=LiteLlm(model="anthropic/claude-3-sonnet-20240229"),
            name="fallback", 
            description="Agente de fallback"
        )
    
    async def get_response(self, message: str):
        try:
            # Tentar agente principal
            return await self._run_agent(self.primary_agent, message)
        except Exception as e:
            print(f"Erro no agente principal: {e}")
            # Usar fallback
            return await self._run_agent(self.fallback_agent, message)
    
    async def _run_agent(self, agent, message):
        # Implementar lógica de execução do agente
        pass
```

### Monitoramento e Métricas

```python
import time
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

class MonitoredAgent:
    def __init__(self, model_name: str):
        self.agent = Agent(
            model=LiteLlm(model=model_name),
            name=f"monitored_{model_name.replace('/', '_')}",
            description="Agente com monitoramento"
        )
        self.metrics = {
            "total_requests": 0,
            "total_time": 0,
            "errors": 0
        }
    
    async def run_with_metrics(self, message: str):
        start_time = time.time()
        self.metrics["total_requests"] += 1
        
        try:
            # Executar agente
            result = await self._execute_agent(message)
            elapsed_time = time.time() - start_time
            self.metrics["total_time"] += elapsed_time
            
            print(f"Request executada em {elapsed_time:.2f}s")
            return result
            
        except Exception as e:
            self.metrics["errors"] += 1
            print(f"Erro: {e}")
            raise
    
    def get_metrics(self):
        avg_time = (self.metrics["total_time"] / self.metrics["total_requests"] 
                   if self.metrics["total_requests"] > 0 else 0)
        
        return {
            **self.metrics,
            "average_time": avg_time,
            "error_rate": (self.metrics["errors"] / self.metrics["total_requests"] 
                          if self.metrics["total_requests"] > 0 else 0)
        }
```

## 🔧 Troubleshooting

### Problemas Comuns

#### 1. Erro de Importação

```python
# ❌ Importação incorreta
from google.adk.agents import Agent

# ✅ Importação correta
from google.adk import Agent
```

#### 2. Chaves de API não Configuradas

```python
import os
from dotenv import load_dotenv

# Verificar se as chaves estão configuradas
load_dotenv()

required_keys = {
    "OPENAI_API_KEY": "OpenAI",
    "ANTHROPIC_API_KEY": "Anthropic", 
    "GOOGLE_API_KEY": "Google AI"
}

for key, service in required_keys.items():
    if not os.getenv(key):
        print(f"⚠️  {service} API key não encontrada: {key}")
    else:
        print(f"✅ {service} API key configurada")
```

#### 3. Erro de Rate Limit

```python
import asyncio
from google.adk.models.lite_llm import LiteLlm

# Configurar retry e rate limiting
agent_with_retry = Agent(
    model=LiteLlm(
        model="openai/gpt-4o",
        # Configurações para lidar com rate limits
        rpm=60,  # Requests per minute
        tpm=40000  # Tokens per minute
    ),
    name="rate_limited_agent",
    description="Agente com controle de rate limit"
)
```

### Debugging

```python
import logging

# Habilitar logs detalhados para debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("google_adk")
logger.setLevel(logging.DEBUG)

# Logs do LiteLLM
import litellm
litellm.set_verbose = True
```

## 📚 Recursos Adicionais

### Scripts Úteis

#### Teste de Conectividade

```python
async def test_model_connectivity():
    """Testa conectividade com diferentes modelos"""
    models_to_test = [
        "openai/gpt-4o",
        "anthropic/claude-3-sonnet-20240229", 
        "gemini/gemini-2.0-flash-exp"
    ]
    
    for model_name in models_to_test:
        try:
            agent = Agent(
                model=LiteLlm(model=model_name),
                name=f"test_{model_name.replace('/', '_')}",
                description=f"Teste para {model_name}"
            )
            print(f"✅ {model_name}: Conectividade OK")
        except Exception as e:
            print(f"❌ {model_name}: Erro - {e}")

# Executar teste
asyncio.run(test_model_connectivity())
```

#### Comparação de Modelos

```python
async def compare_models(prompt: str):
    """Compara respostas de diferentes modelos"""
    models = [
        ("OpenAI GPT-4", "openai/gpt-4o"),
        ("Anthropic Claude", "anthropic/claude-3-sonnet-20240229"),
        ("Google Gemini", "gemini/gemini-2.0-flash-exp")
    ]
    
    for name, model_id in models:
        agent = Agent(
            model=LiteLlm(model=model_id),
            name=f"compare_{name.lower().replace(' ', '_')}",
            description=f"Agente de comparação usando {name}"
        )
        
        print(f"\n--- {name} ---")
        # Executar e mostrar resposta
        # (implementar lógica de execução)
```

### Templates de Projeto

#### Estrutura Recomendada

```
meu_projeto_adk/
├── .env                    # Variáveis de ambiente
├── requirements.txt        # Dependências
├── agents/                 # Definições de agentes
│   ├── __init__.py
│   ├── openai_agent.py
│   ├── claude_agent.py
│   └── gemini_agent.py
├── tools/                  # Ferramentas customizadas
│   ├── __init__.py
│   └── custom_tools.py
├── runners/                # Scripts de execução
│   ├── __init__.py
│   └── main.py
└── tests/                  # Testes
    ├── __init__.py
    └── test_agents.py
```

#### requirements.txt

```txt
google-adk>=1.0.0
litellm>=1.0.0
python-dotenv>=1.0.0
asyncio-mqtt>=0.11.0
pydantic>=2.0.0
```

### Links Úteis

- [Documentação Oficial do ADK](https://google.github.io/adk-docs/)
- [Documentação do LiteLLM](https://docs.litellm.ai/)
- [Exemplos no GitHub](https://github.com/google/adk-python/tree/main/contributing/samples)
- [ADK Samples Repository](https://github.com/google/adk-samples)

## 🎯 Próximos Passos

1. **Experimente os exemplos** fornecidos neste guia
2. **Configure suas chaves de API** para os modelos que deseja usar
3. **Crie seu primeiro agente** multi-modelo
4. **Explore ferramentas avançadas** como retrieval e code execution
5. **Deploy em produção** usando Cloud Run ou Vertex AI

---

*Este guia foi criado para ajudar desenvolvedores a aproveitar ao máximo o poder do ADK com LiteLLM. Para dúvidas ou sugestões, consulte a documentação oficial ou abra uma issue no repositório.*
