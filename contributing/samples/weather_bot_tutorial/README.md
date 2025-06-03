# Weather Bot Tutorial - Complete ADK Learning Path

Este tutorial demonstra como construir um sistema multi-agente robusto usando o Agent Development Kit (ADK) do Google, progredindo através de 6 passos incrementais que ensinam os conceitos fundamentais e avançados do ADK.

## 📋 Visão Geral

O tutorial Weather Bot é um guia prático completo que ensina como construir agentes inteligentes com ADK, começando de um agente básico de clima e evoluindo para um sistema multi-agente seguro com gerenciamento de estado e controles de segurança avançados.

### 🎯 O que você aprenderá

- **Conceitos básicos de agentes ADK**: Configuração, ferramentas e interação
- **Suporte a múltiplos modelos**: Integração com LiteLLM para usar diferentes LLMs
- **Sistemas multi-agente**: Delegação e coordenação entre agentes especializados
- **Gerenciamento de estado**: Manutenção de contexto entre interações
- **Segurança em camadas**: Validação de entrada e controle de execução de ferramentas

### 🗂️ Estrutura do Tutorial

```
weather_bot_tutorial/
├── README.md                                    # Este guia
├── step_1_basic_weather_agent.py              # Agente básico de clima
├── step_2_multi_model_support.py              # Suporte a múltiplos modelos
├── step_3_multi_agent_delegation.py           # Sistema multi-agente
├── step_4_session_state_management.py         # Gerenciamento de estado
├── step_5_security_before_model_callback.py   # Segurança de entrada
└── step_6_security_before_tool_callback.py    # Segurança de ferramentas
```

## 🚀 Início Rápido

### Pré-requisitos

1. **Python 3.8+** instalado
2. **ADK Python** configurado no seu ambiente
3. **Chaves de API** (opcional para alguns passos):
   - `OPENAI_API_KEY` para GPT-4 (Passo 2)
   - `ANTHROPIC_API_KEY` para Claude (Passo 2)

### Instalação

```bash
# Clone o repositório ADK (se ainda não tiver)
git clone https://github.com/google/adk-python.git
cd adk-python

# Navegue até o diretório do tutorial
cd contributing/samples/weather_bot_tutorial

# Execute qualquer passo do tutorial
python step_1_basic_weather_agent.py
```

## 📚 Passos do Tutorial

### 🌤️ Passo 1: Agente Básico de Clima

**Arquivo**: `step_1_basic_weather_agent.py`

**Conceitos ensinados**:
- Configuração básica de agente ADK
- Criação de ferramentas personalizadas
- Configuração de modelos (Gemini 2.0 Flash)
- Gerenciamento de sessão com `InMemorySessionService`
- Execução de agentes com `Runner`

**Características**:
- Ferramenta `get_weather` com dados simulados para 3 cidades
- Agente configurado com instruções claras
- Padrões de interação assíncrona
- Tratamento abrangente de erros

**Execute**:
```bash
python step_1_basic_weather_agent.py
```

### 🌐 Passo 2: Suporte a Múltiplos Modelos

**Arquivo**: `step_2_multi_model_support.py`

**Conceitos ensinados**:
- Integração com LiteLLM
- Abstração de modelos no ADK
- Comparação entre diferentes provedores de LLM
- Configuração de múltiplos modelos

**Modelos suportados**:
- **Gemini 2.0 Flash** (padrão ADK)
- **OpenAI GPT-4o** (via LiteLLM)
- **Anthropic Claude 3 Sonnet** (via LiteLLM)

**Execute**:
```bash
# Configure as chaves de API (opcional)
export OPENAI_API_KEY="sua-chave-openai"
export ANTHROPIC_API_KEY="sua-chave-anthropic"

python step_2_multi_model_support.py
```

### 🤖 Passo 3: Sistema Multi-Agente com Delegação

**Arquivo**: `step_3_multi_agent_delegation.py`

**Conceitos ensinados**:
- Arquitetura de sistema multi-agente
- Delegação através do parâmetro `sub_agents`
- Agentes especializados para tarefas específicas
- Coordenação entre agentes

**Agentes incluídos**:
- **Agente principal**: Coordena e delega tarefas
- **Agente de saudação**: Especializado em cumprimentos (`say_hello`)
- **Agente de clima**: Fornece informações meteorológicas (`get_weather`)
- **Agente de despedida**: Especializado em despedidas (`say_goodbye`)

**Execute**:
```bash
python step_3_multi_agent_delegation.py
```

### 💾 Passo 4: Gerenciamento de Estado de Sessão

**Arquivo**: `step_4_session_state_management.py`

**Conceitos ensinados**:
- Uso do `ToolContext` para acessar estado da sessão
- Salvamento automático de estado com `output_key`
- Personalização baseada em histórico do usuário
- Persistência de dados entre interações

**Características**:
- Ferramenta `get_weather_stateful` com capacidades de memória
- Rastreamento de consultas anteriores
- Insights personalizados baseados em histórico
- Gerenciamento de preferências do usuário

**Execute**:
```bash
python step_4_session_state_management.py
```

### 🔒 Passo 5: Segurança com Before Model Callback

**Arquivo**: `step_5_security_before_model_callback.py`

**Conceitos ensinados**:
- Validação de entrada usando `before_model_callback`
- Proteção contra conteúdo malicioso
- Políticas de segurança personalizadas
- Inspeção de entrada do usuário

**Características de segurança**:
- Bloqueio de palavra-chave "BLOCK"
- Detecção de padrões suspeitos
- Validação de conteúdo ofensivo
- Controle de acesso baseado em tópicos

**Execute**:
```bash
python step_5_security_before_model_callback.py
```

### 🔧 Passo 6: Segurança com Before Tool Callback

**Arquivo**: `step_6_security_before_tool_callback.py`

**Conceitos ensinados**:
- Segurança ao nível de ferramenta usando `before_tool_callback`
- Validação de argumentos de ferramentas
- Restrições geográficas e de acesso
- Arquitetura de segurança abrangente

**Características de segurança**:
- Bloqueio de consultas meteorológicas para Paris
- Validação de argumentos de ferramentas
- Proteção contra injeção maliciosa
- Controles de acesso em múltiplas camadas

**Execute**:
```bash
python step_6_security_before_tool_callback.py
```

## 🎨 Características dos Exemplos

### 🛠️ Ferramentas Implementadas

1. **`get_weather(city)`**: Ferramenta básica de clima com dados simulados
2. **`get_weather_stateful(city, context)`**: Versão com estado que lembra consultas anteriores
3. **`say_hello(name)`**: Ferramenta de saudação personalizada
4. **`say_goodbye(name)`**: Ferramenta de despedida personalizada
5. **`get_detailed_weather(city, include_forecast)`**: Informações meteorológicas detalhadas

### 🌍 Dados de Cidades Suportadas

Cada exemplo inclui dados meteorológicos simulados para:
- **New York, NY** - Parcialmente nublado, 22°C
- **London, UK** - Chuva leve, 15°C  
- **Tokyo, Japan** - Ensolarado, 26°C
- **Paris, France** - Nublado, 18°C (bloqueado no Passo 6)
- **Berlin, Germany** - Nublado, 16°C
- **Sydney, Australia** - Céu limpo, 25°C

### 🔐 Características de Segurança

- **Validação de entrada**: Bloqueia conteúdo malicioso antes do processamento do modelo
- **Segurança de ferramentas**: Valida argumentos de ferramentas antes da execução
- **Restrições geográficas**: Implementa controles de acesso baseados em localização
- **Proteção contra injeção**: Previne tentativas de injeção de código
- **Controle de taxa**: Limita consultas excessivas (simulado)

## 🧪 Executando os Testes

Cada passo inclui testes abrangentes demonstrando diferentes cenários:

### Testes Básicos
```bash
# Execute todos os passos em sequência
for i in {1..6}; do
    echo "=== Executando Passo $i ==="
    python step_${i}_*.py
    echo
done
```

### Testes de Componentes Individuais
```bash
# Teste apenas ferramentas (sem agente completo)
python -c "
from step_1_basic_weather_agent import get_weather
print(get_weather('Tokyo'))
"
```

### Testes de Segurança
```bash
# Teste cenários de segurança especificamente
python step_5_security_before_model_callback.py
python step_6_security_before_tool_callback.py
```

## 🔧 Personalização e Extensão

### Adicionando Novas Cidades

Para adicionar suporte a novas cidades, edite o dicionário `WEATHER_DATABASE`:

```python
WEATHER_DATABASE = {
    # ... cidades existentes ...
    "sao_paulo": {
        "temperature": "28°C (82°F)",
        "condition": "Ensolarado",
        "humidity": "60%",
        "wind_speed": "10 km/h",
        "location": "São Paulo, Brasil"
    }
}
```

### Criando Ferramentas Personalizadas

```python
def get_air_quality(city: str) -> Dict[str, Any]:
    """Exemplo de ferramenta personalizada para qualidade do ar"""
    # Implementar lógica da ferramenta
    return {"city": city, "aqi": 50, "status": "Good"}

# Adicionar ao agente
agent = Agent(
    name="enhanced_weather_agent",
    model=MODEL_GEMINI_2_0_FLASH,
    tools=[get_weather, get_air_quality],  # Incluir nova ferramenta
    instruction="Você pode fornecer clima e qualidade do ar..."
)
```

### Implementando Novos Callbacks de Segurança

```python
def custom_security_callback(context: ModelContext) -> Optional[str]:
    """Callback de segurança personalizado"""
    if "palavra_proibida" in context.user_message.lower():
        return "Conteúdo bloqueado por política personalizada"
    return None

agent = Agent(
    # ... configuração básica ...
    before_model_callback=custom_security_callback
)
```

## 🌟 Melhores Práticas Demonstradas

### 1. **Estrutura de Código**
- Separação clara entre lógica de ferramenta e agente
- Configuração centralizada de modelos e aplicação
- Tratamento consistente de erros
- Logging abrangente para debugging

### 2. **Gerenciamento de Sessão**
- Uso de IDs de sessão únicos para diferentes cenários de teste
- Reutilização de serviços de sessão entre agentes
- Estratégias de persistência de estado

### 3. **Segurança**
- Defesa em profundidade com múltiplas camadas de validação
- Separação entre validação de entrada e validação de ferramenta
- Políticas de segurança configuráveis e extensíveis

### 4. **Testabilidade**
- Cenários de teste abrangentes para cada característica
- Testes tanto positivos quanto negativos
- Casos extremos e validação de entrada

## 🚨 Solução de Problemas

### Problemas Comuns

1. **Erro de Chave de API**:
   ```
   ❌ API key not configured or invalid
   ```
   **Solução**: Configure as variáveis de ambiente necessárias:
   ```bash
   export OPENAI_API_KEY="sua-chave"
   export ANTHROPIC_API_KEY="sua-chave"
   ```

2. **Erro de Importação do ADK**:
   ```
   ModuleNotFoundError: No module named 'google.adk'
   ```
   **Solução**: Certifique-se de que o ADK está instalado e você está no diretório correto.

3. **Erro de Timeout de Sessão**:
   ```
   SessionTimeoutError
   ```
   **Solução**: Use IDs de sessão únicos para cada teste ou limpe o estado da sessão.

### Debugging

Ative o logging detalhado:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

Use o modo de teste direto de ferramentas:
```python
# Teste ferramentas diretamente sem agente
result = get_weather("Tokyo")
print(result)
```

## 📖 Recursos Adicionais

### Documentação do ADK
- [Documentação oficial do ADK](https://github.com/google/adk-python)
- [Guia de referência da API](https://google.github.io/adk-python/)
- [Exemplos adicionais](../../../examples/)

### Conceitos Relacionados
- **LiteLLM**: [Documentação](https://litellm.ai/) para integração com múltiplos modelos
- **Gemini**: [Documentação do modelo](https://ai.google.dev/docs) para modelos Gemini
- **Padrões de agente**: Documentação de padrões de design de agente

### Próximos Passos

Após completar este tutorial, considere explorar:

1. **Integração com APIs reais**: Conecte-se a serviços meteorológicos reais
2. **Persistência avançada**: Implemente armazenamento de banco de dados
3. **Interface de usuário**: Crie interfaces web ou mobile para seus agentes
4. **Deployment**: Implante agentes em ambientes de produção
5. **Monitoramento**: Adicione telemetria e métricas de desempenho

## 🤝 Contribuindo

Se você encontrar problemas ou tiver melhorias para sugerir:

1. Abra uma issue no repositório ADK
2. Proponha melhorias através de pull requests
3. Compartilhe seus próprios exemplos e extensões

## 📄 Licença

Este tutorial é parte do projeto ADK e está sob a mesma licença do repositório principal.

---

**🎉 Parabéns por completar o Weather Bot Tutorial!**

Você agora tem conhecimento sólido sobre como construir sistemas de agentes inteligentes usando o ADK. Use estes conceitos como base para criar suas próprias aplicações inovadoras de IA!
