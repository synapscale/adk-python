# Google ADK + LiteLLM: Guia Rápido de Uso

Este repositório contém um guia completo e exemplos práticos para usar o **Google Agent Development Kit (ADK)** com **LiteLLM** para suporte a múltiplos modelos de linguagem.

## 🚀 Início Rápido

### 1. Instalação

```bash
pip install google-adk litellm python-dotenv
```

### 2. Configuração das Chaves de API

Crie um arquivo `.env` na raiz do projeto:

```bash
# OpenAI
OPENAI_API_KEY=sua_chave_openai_aqui

# Anthropic
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui

# Google AI
GOOGLE_API_KEY=sua_chave_google_aqui
```

### 3. Teste de Funcionamento

Execute os exemplos para verificar se tudo está funcionando:

```bash
python examples/multi_model_examples.py
```

## 📚 Documentação

### [📖 Guia Completo](docs/ADK_LITELLM_GUIDE.md)

O guia principal contém:
- **Instalação passo a passo**
- **Configuração de múltiplos modelos**
- **Exemplos práticos detalhados**
- **Configurações avançadas**
- **Troubleshooting**
- **Best practices**

### [💻 Exemplos Práticos](examples/multi_model_examples.py)

O arquivo de exemplos inclui:
- Agentes com diferentes modelos (OpenAI, Anthropic, Gemini)
- Agentes com ferramentas personalizadas
- Sistema multi-agente
- Comparação entre modelos
- Testes de conectividade
- Verificação de chaves de API

## 🤖 Modelos Suportados

| Provedor | Modelos Disponíveis | Chave de API |
|----------|-------------------|--------------|
| **OpenAI** | GPT-4o, GPT-4o-mini, GPT-4-turbo, GPT-3.5-turbo | `OPENAI_API_KEY` |
| **Anthropic** | Claude 3 Opus/Sonnet/Haiku, Claude 3.5 Sonnet/Haiku | `ANTHROPIC_API_KEY` |
| **Google** | Gemini 2.0 Flash, Gemini 1.5 Pro/Flash | `GOOGLE_API_KEY` |
| **Cohere** | Command R+, Command | `COHERE_API_KEY` |
| **Mistral** | Mistral Large, Medium, Small | `MISTRAL_API_KEY` |

## 🛠️ Exemplo Básico

```python
import asyncio
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types

async def exemplo_basico():
    # Criar agente
    agent = Agent(
        model=LiteLlm(model="openai/gpt-4o"),
        name="meu_assistente",
        description="Assistente inteligente",
        instruction="Seja útil e preciso nas respostas."
    )
    
    # Configurar runner
    runner = Runner(
        app_name="meu_app",
        agent=agent,
        session_service=InMemorySessionService()
    )
    
    # Criar sessão
    session = await runner.session_service.create_session(
        app_name="meu_app",
        user_id="usuario_teste"
    )
    
    # Enviar mensagem
    message = types.Content(
        role="user",
        parts=[types.Part.from_text("Olá! Como você pode me ajudar?")]
    )
    
    # Obter resposta
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=message
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(f"Agente: {part.text}")

# Executar
asyncio.run(exemplo_basico())
```

## 🔧 Estrutura do Projeto

```
adk-python/
├── docs/
│   └── ADK_LITELLM_GUIDE.md     # Guia completo
├── examples/
│   └── multi_model_examples.py   # Exemplos práticos
├── .env                          # Chaves de API (você cria)
├── README_ADK_LITELLM.md        # Este arquivo
└── requirements.txt             # Dependências
```

## 🚨 Troubleshooting

### Erro de Importação
```python
# ❌ Errado
from google.adk.agents import Agent

# ✅ Correto  
from google.adk import Agent
```

### Verificar Chaves de API
```bash
python -c "import os; print('OpenAI:', '✅' if os.getenv('OPENAI_API_KEY') else '❌')"
```

### Logs Detalhados
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Casos de Uso

- **Chatbots inteligentes** com múltiplos modelos
- **Sistemas de análise** com especialização por modelo
- **Assistentes de código** com fallback automático
- **Pipelines de processamento** multi-agente
- **Comparação de modelos** para pesquisa
- **Prototipagem rápida** com diferentes LLMs

## 🔗 Links Úteis

- [Documentação Oficial do ADK](https://google.github.io/adk-docs/)
- [Documentação do LiteLLM](https://docs.litellm.ai/)
- [Exemplos Oficiais ADK](https://github.com/google/adk-python/tree/main/contributing/samples)
- [ADK Samples Repository](https://github.com/google/adk-samples)

## 📞 Suporte

- **Problemas com ADK**: [Issues no GitHub](https://github.com/google/adk-python/issues)
- **Problemas com LiteLLM**: [Documentação LiteLLM](https://docs.litellm.ai/docs/troubleshooting)
- **Este guia**: Consulte o arquivo [`docs/ADK_LITELLM_GUIDE.md`](docs/ADK_LITELLM_GUIDE.md)

---

**🎯 Dica**: Comece executando `python examples/multi_model_examples.py` para verificar se tudo está configurado corretamente!
