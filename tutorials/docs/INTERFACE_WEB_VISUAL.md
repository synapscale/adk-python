# 🌐 Interface Web Visual do Google ADK

## 📖 Visão Geral

O Google ADK possui uma **interface web visual moderna e completa** integrada! Não é necessário instalar ferramentas externas. A interface inclui:

- 🎨 **Interface Angular moderna** com Material Design
- 💬 **Chat interativo** em tempo real
- 🎤 **Processamento de áudio** e voz
- 🔧 **Debug avançado** de agentes
- 📊 **Visualização de conversas**
- 🌍 **WebSocket** para comunicação em tempo real

## 🚀 Como Usar

### 1. Configurar Variáveis de Ambiente

```bash
# Para OpenAI
export OPENAI_API_KEY="sua_chave_aqui"

# Para Anthropic
export ANTHROPIC_API_KEY="sua_chave_aqui"

# Para Google Gemini
export GOOGLE_API_KEY="sua_chave_aqui"
```

### 2. Iniciar a Interface Web

```bash
# Comando básico
adk web .

# Com porta personalizada
adk web --port 3000 .

# Permitir acesso externo
adk web --host 0.0.0.0 --port 8000 .

# Com reload automático (desenvolvimento)
adk web --reload .
```

### 3. Acessar a Interface

Abra seu navegador em: **http://localhost:8000**

## 🎯 Recursos da Interface Web

### 💻 Interface Principal
- **Chat moderno**: Interface limpa e responsiva
- **Histórico**: Visualize conversas anteriores
- **Multi-sessão**: Gerencie múltiplas conversas
- **Temas**: Suporte a modo claro/escuro

### 🔧 Funcionalidades Avançadas
- **Debug visual**: Veja como o agente processa as requests
- **Monitoramento**: Acompanhe performance e tempo de resposta
- **Teste de ferramentas**: Teste diferentes tools e capabilities
- **Configuração dinâmica**: Ajuste parâmetros em tempo real

### 🎤 Recursos de Áudio
- **Processamento de voz**: Fale diretamente com o agente
- **Síntese de fala**: Ouça as respostas do agente
- **Audio worklets**: Processamento avançado de áudio

### 📡 Comunicação
- **WebSocket**: Comunicação em tempo real
- **REST API**: Interface completa para integração
- **CORS configurável**: Para desenvolvimento e produção

## 🛠️ Estrutura de Arquivos

O ADK espera esta estrutura:

```
projeto/
├── agent.py          # Agente principal (obrigatório)
├── __init__.py       # Módulo Python (obrigatório)
└── requirements.txt  # Dependências (opcional)
```

## 📝 Exemplo de Uso Avançado

### Interface com Múltiplos Agentes

```python
# agent.py
from google.adk import Agent
from google.adk.models import LiteLlm

# Agente coordenador
coordinator = Agent(
    name="coordinator",
    model=LiteLlm(model="gpt-4"),
    instruction="Eu coordeno tarefas entre especialistas.",
    sub_agents=[
        Agent(
            name="code_expert",
            model=LiteLlm(model="gpt-4"),
            instruction="Especialista em programação."
        ),
        Agent(
            name="design_expert", 
            model=LiteLlm(model="claude-3-sonnet"),
            instruction="Especialista em design e UX."
        )
    ]
)

root_agent = coordinator
```

### Com Ferramentas Personalizadas

```python
# agent.py
from google.adk import Agent
from google.adk.models import LiteLlm
from google.adk.tools import google_search

def calculadora(a: float, b: float, operacao: str) -> float:
    """Realiza operações matemáticas básicas."""
    if operacao == "soma":
        return a + b
    elif operacao == "subtracao":
        return a - b
    elif operacao == "multiplicacao":
        return a * b
    elif operacao == "divisao":
        return a / b if b != 0 else "Erro: divisão por zero"

root_agent = Agent(
    name="assistente_completo",
    model=LiteLlm(model="gpt-4"),
    instruction="Assistente com capacidades de busca e cálculo.",
    tools=[google_search, calculadora]
)
```

## 🌟 Funcionalidades Especiais

### 1. **Dev UI Angular**
- Interface construída em Angular
- Componentes Material Design
- Responsiva e moderna
- Suporte a PWA

### 2. **Audio Processor**
- WebAudio API integrada
- Processamento em tempo real
- Suporte a múltiplos formatos
- Audio worklets customizados

### 3. **FastAPI Backend**
- API REST completa
- Documentação automática em `/docs`
- WebSocket para tempo real
- CORS configurável

### 4. **Sessões Persistentes**
- Banco de dados SQLite integrado
- Histórico de conversas
- Estado de sessão mantido
- Backup automático

## 🔍 URLs Importantes

Quando a interface estiver rodando:

- **Interface Principal**: `http://localhost:8000`
- **API Docs**: `http://localhost:8000/docs`
- **Health Check**: `http://localhost:8000/health`
- **WebSocket**: `ws://localhost:8000/ws`

## 🎨 Customização

### Temas e Estilos
A interface suporta personalização através de CSS e temas Material Design.

### Configuração Avançada
```bash
# Configuração completa
adk web \
  --host 0.0.0.0 \
  --port 8000 \
  --session_db_url "sqlite:///sessions.db" \
  --allow_origins "http://localhost:3000,https://meuapp.com" \
  --log_level info \
  --reload \
  .
```

## 🚀 Próximos Passos

1. **Execute**: `adk web .`
2. **Acesse**: `http://localhost:8000`
3. **Experimente**: Chat, áudio, ferramentas
4. **Customize**: Adicione seus próprios agentes e tools
5. **Deploy**: Use em produção com Docker/Cloud Run

## 💡 Dicas

- Use `--reload` durante desenvolvimento
- Configure `--host 0.0.0.0` para acesso remoto
- Monitore logs com `--log_level debug`
- Use SQLite para persistência local
- Configure CORS para integração com outros apps

---

**A interface web do ADK é uma solução completa e moderna para desenvolvimento e teste de agentes AI!** 🎉
