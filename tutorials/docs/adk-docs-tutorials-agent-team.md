Kit de Desenvolvimento de 
Q Procurar 
profundar e construir um sistema multiagente mais sofisticado. 
Agentes 
Ferramentas 
> 
Aberto no Colab 
Agentes em execução # Kit de Desenvolvimento de Agente (ADK)

## Crie sua primeira equipe de agentes inteligentes: um bot de clima progressivo com ADK

Este tutorial é uma extensão do exemplo de Início Rápido do Kit de Desenvolvimento de Agentes (ADK).  Construiremos um sistema multiagente sofisticado, começando com um único agente e adicionando recursos gradualmente.

**Recursos abordados:**

* Uso de diferentes modelos de IA (Gemini, GPT, Claude).
* Criação de subagentes especializados (saudações, despedidas).
* Delegação inteligente entre agentes.
* Memória com estado de sessão persistente.
* Proteções de segurança com callbacks (before_model_callback e before_tool_callback).


**Por que um bot de clima multiagente?**

Este caso de uso, embora simples, demonstra os conceitos principais do ADK, essenciais para aplicações complexas.  Você aprenderá a estruturar interações, gerenciar estados, garantir segurança e orquestrar múltiplos modelos de IA.

**O que é o ADK?**

O ADK é um framework Python para desenvolvimento de aplicativos baseados em Large Language Models (LLMs). Ele oferece ferramentas para criação de agentes que raciocinam, planejam, usam ferramentas, interagem com usuários e colaboram em equipe.

**Neste tutorial, você aprenderá a:**

* Definir e usar ferramentas: criar funções Python que concedem habilidades específicas aos agentes.
* Usar múltiplos LLMs: configurar agentes para usar Gemini, GPT-4, Claude, etc., via LiteLLM.
* Implementar delegação e colaboração entre agentes.
* Utilizar estado de sessão para memória.
* Implementar segurança com callbacks.


**Pré-requisitos:**

* Conhecimento sólido de programação Python.
* Familiaridade com LLMs, APIs e o conceito de agentes.
* Conclusão do tutorial de Início Rápido do ADK ou conhecimento equivalente dos conceitos básicos (Agente, Executador, Serviço de Sessão, uso básico de ferramentas).
* Chaves de API para os LLMs que você pretende usar (Google AI Studio para Gemini, OpenAI Platform, Anthropic Console).

**Nota sobre o ambiente de execução:**

Este tutorial é ideal para notebooks interativos (Google Colab, Jupyter).  Considere:

* **Execução assíncrona:**  Use `await` (em loops de eventos) ou `asyncio.run()` (em scripts independentes).
* **Configuração manual do executor/sessão:**  O tutorial demonstra criação explícita de `Runner` e `SessionService` para controle preciso.
* **Alternativa: Ferramentas integradas do ADK:**  Para configuração automática, consulte a documentação do ADK sobre `adk web`, `adk run` e `adk api_server`.


---

## Etapas do Tutorial:

### Etapa 1: Seu primeiro agente - Consulta básica do clima

1. **Defina a ferramenta `get_weather`:**  Uma função Python que busca dados meteorológicos (simulando dados neste exemplo). A docstring é crucial para o LLM entender a função, seus argumentos e retorno.

2. **Defina o agente `weather_agent`:** Configura o agente com `name`, `model`, `description`, `instruction` e `tools`.  `instruction` detalha o comportamento do agente e como usar as ferramentas.

3. **Configure o `Runner` e o `SessionService`:** `SessionService` gerencia o histórico de conversas. `Runner` orquestra a interação entre usuário, agente e LLM.

4. **Interaja com o agente:** Use uma função `call_agent_async` para enviar consultas e receber respostas.

### Etapa 2: Adotando vários modelos com o LiteLLM (Opcional)

Esta etapa demonstra como usar diferentes LLMs (OpenAI, Anthropic) via LiteLLM.  Você criará e testará instâncias do `weather_agent` com modelos diferentes, observando as variações nas respostas.

### Etapa 3: Construindo uma Equipe de Agentes - Delegação para Saudações e Despedidas

1. **Defina ferramentas para saudações (`say_hello`) e despedidas (`say_goodbye`).**

2. **Crie subagentes `greeting_agent` e `farewell_agent`.**  `description` é crucial para a delegação automática.

3. **Atualize o agente climático principal (`weather_agent_v2`) para atuar como agente raiz, incluindo `sub_agents`.**  As instruções do agente raiz devem guiar as decisões de delegação.

4. **Teste o fluxo de delegação.**

### Etapa 4: Adicionando memória e personalização com estado de sessão

1. **Inicialize um novo `SessionService` e estado inicial.**

2. **Crie `get_weather_stateful`, uma versão com reconhecimento de estado da ferramenta meteorológica.**  Use `ToolContext` para acessar o estado da sessão.

3. **Atualize o agente raiz para usar `get_weather_stateful` e configure `output_key` para salvar automaticamente a resposta no estado da sessão.**

4. **Execute uma conversa para testar o fluxo de estado.**

### Etapa 5: Adicionando segurança - Guardrail de entrada com `before_model_callback`

1. **Defina `block_keyword_guardrail`, um `before_model_callback` que verifica a entrada do usuário para uma palavra-chave ("BLOCK").**  Retorne um `LlmResponse` para bloquear a solicitação ou `None` para permitir.

2. **Atualize o agente raiz para usar este callback.**

3. **Teste o guardrail.**

### Etapa 6: Adicionando segurança - Guardrail do argumento da ferramenta (`before_tool_callback`)

1. **Defina `block_paris_tool_guardrail`, um `before_tool_callback` que verifica se `get_weather_stateful` é chamado com a cidade "Paris".**  Retorne um dicionário de erros para bloquear ou `None` para permitir.

2. **Atualize o agente raiz para incluir ambos os callbacks.**

3. **Teste o guardrail.**


---

**Conclusão:**

Este tutorial demonstra a construção progressiva de um sistema multiagente, utilizando recursos essenciais do ADK para criar aplicações robustas, seguras e escaláveis.  A combinação de agentes, ferramentas, delegação inteligente, estado de sessão e callbacks proporciona um framework poderoso para desenvolvimento de IA avançada.
# Kit de Desenvolvimento de Agente (ADK)

## Crie sua primeira equipe de agentes inteligentes: um bot de clima progressivo com ADK

Este tutorial é uma extensão do exemplo de Início Rápido do Kit de Desenvolvimento de Agentes (ADK).  Construiremos um sistema multiagente sofisticado, começando com um único agente e adicionando recursos gradualmente.

**Recursos abordados:**

* Uso de diferentes modelos de IA (Gemini, GPT, Claude).
* Criação de subagentes especializados (saudações, despedidas).
* Delegação inteligente entre agentes.
* Memória com estado de sessão persistente.
* Proteções de segurança com callbacks (before_model_callback e before_tool_callback).


**Por que um bot de clima multiagente?**

Este caso de uso, embora simples, demonstra os conceitos principais do ADK, essenciais para aplicações complexas.  Você aprenderá a estruturar interações, gerenciar estados, garantir segurança e orquestrar múltiplos modelos de IA.

**O que é o ADK?**

O ADK é um framework Python para desenvolvimento de aplicativos baseados em Large Language Models (LLMs). Ele oferece ferramentas para criação de agentes que raciocinam, planejam, usam ferramentas, interagem com usuários e colaboram em equipe.

**Neste tutorial, você aprenderá a:**

* Definir e usar ferramentas: criar funções Python que concedem habilidades específicas aos agentes.
* Usar múltiplos LLMs: configurar agentes para usar Gemini, GPT-4, Claude, etc., via LiteLLM.
* Implementar delegação e colaboração entre agentes.
* Utilizar estado de sessão para memória.
* Implementar segurança com callbacks.


**Pré-requisitos:**

* Conhecimento sólido de programação Python.
* Familiaridade com LLMs, APIs e o conceito de agentes.
* Conclusão do tutorial de Início Rápido do ADK ou conhecimento equivalente dos conceitos básicos (Agente, Executador, Serviço de Sessão, uso básico de ferramentas).
* Chaves de API para os LLMs que você pretende usar (Google AI Studio para Gemini, OpenAI Platform, Anthropic Console).

**Nota sobre o ambiente de execução:**

Este tutorial é ideal para notebooks interativos (Google Colab, Jupyter).  Considere:

* **Execução assíncrona:**  Use `await` (em loops de eventos) ou `asyncio.run()` (em scripts independentes).
* **Configuração manual do executor/sessão:**  O tutorial demonstra criação explícita de `Runner` e `SessionService` para controle preciso.
* **Alternativa: Ferramentas integradas do ADK:**  Para configuração automática, consulte a documentação do ADK sobre `adk web`, `adk run` e `adk api_server`.


---

## Etapas do Tutorial:

### Etapa 1: Seu primeiro agente - Consulta básica do clima

1. **Defina a ferramenta `get_weather`:**  Uma função Python que busca dados meteorológicos (simulando dados neste exemplo). A docstring é crucial para o LLM entender a função, seus argumentos e retorno.

2. **Defina o agente `weather_agent`:** Configura o agente com `name`, `model`, `description`, `instruction` e `tools`.  `instruction` detalha o comportamento do agente e como usar as ferramentas.

3. **Configure o `Runner` e o `SessionService`:** `SessionService` gerencia o histórico de conversas. `Runner` orquestra a interação entre usuário, agente e LLM.

4. **Interaja com o agente:** Use uma função `call_agent_async` para enviar consultas e receber respostas.

### Etapa 2: Adotando vários modelos com o LiteLLM (Opcional)

Esta etapa demonstra como usar diferentes LLMs (OpenAI, Anthropic) via LiteLLM.  Você criará e testará instâncias do `weather_agent` com modelos diferentes, observando as variações nas respostas.

### Etapa 3: Construindo uma Equipe de Agentes - Delegação para Saudações e Despedidas

1. **Defina ferramentas para saudações (`say_hello`) e despedidas (`say_goodbye`).**

2. **Crie subagentes `greeting_agent` e `farewell_agent`.**  `description` é crucial para a delegação automática.

3. **Atualize o agente climático principal (`weather_agent_v2`) para atuar como agente raiz, incluindo `sub_agents`.**  As instruções do agente raiz devem guiar as decisões de delegação.

4. **Teste o fluxo de delegação.**

### Etapa 4: Adicionando memória e personalização com estado de sessão

1. **Inicialize um novo `SessionService` e estado inicial.**

2. **Crie `get_weather_stateful`, uma versão com reconhecimento de estado da ferramenta meteorológica.**  Use `ToolContext` para acessar o estado da sessão.

3. **Atualize o agente raiz para usar `get_weather_stateful` e configure `output_key` para salvar automaticamente a resposta no estado da sessão.**

4. **Execute uma conversa para testar o fluxo de estado.**

### Etapa 5: Adicionando segurança - Guardrail de entrada com `before_model_callback`

1. **Defina `block_keyword_guardrail`, um `before_model_callback` que verifica a entrada do usuário para uma palavra-chave ("BLOCK").**  Retorne um `LlmResponse` para bloquear a solicitação ou `None` para permitir.

2. **Atualize o agente raiz para usar este callback.**

3. **Teste o guardrail.**

### Etapa 6: Adicionando segurança - Guardrail do argumento da ferramenta (`before_tool_callback`)

1. **Defina `block_paris_tool_guardrail`, um `before_tool_callback` que verifica se `get_weather_stateful` é chamado com a cidade "Paris".**  Retorne um dicionário de erros para bloquear ou `None` para permitir.

2. **Atualize o agente raiz para incluir ambos os callbacks.**

3. **Teste o guardrail.**


---

**Conclusão:**

Este tutorial demonstra a construção progressiva de um sistema multiagente, utilizando recursos essenciais do ADK para criar aplicações robustas, seguras e escaláveis.  A combinação de agentes, ferramentas, delegação inteligente, estado de sessão e callbacks proporciona um framework poderoso para desenvolvimento de IA avançada.


> 
Compartilhar em: 
Implantar 
Sessões e Memória 
> 
Retornos de chamada 
> 
Artefatos 
Eventos 
Contexto 
Avaliar 
MCP 
Transmissão bidirecional (ao 
vivo) 
Segurança e Proteção 
Protocolo Agent2Agent (A2A) 
Recursos da Comunidade 
Guia de Contribuição 
> 
Começaremos a construir uma equipe de agentes do Weather Bot, agregando progressivamente recursos avançados a uma base simples. Começando com um único agente que pode consultar a previsão do tempo, adicionaremos gradualmente recursos como: 
• Aproveitando diferentes modelos de IA (Gemini, GPT, Claude). 
Projetar subagentes especializados para tarefas distintas (como saudações e despedidas). 
· 
Referência de API 
· 
Habilitando delegação inteligente entre agentes. 
Fornecendo memória aos agentes usando estado de sessão 
persistente. 
• Implementando proteções de segurança cruciais usando retornos de chamada. 
Por que uma equipe de bots meteorológicos? 
Este caso de uso, embora aparentemente simples, oferece uma tela prática e compreensível para explorar os principais conceitos do ADK, essenciais para a construção de aplicações complexas e reais. Você aprenderá a estruturar interações, gerenciar estados, garantir a segurança e orquestrar múltiplos "cérebros" de IA trabalhando juntos. 
O que é ADK Again? 
Vale lembrar que o ADK é um framework Python projetado para agilizar o desenvolvimento de aplicativos baseados em Large Language Models (LLMs). Ele oferece blocos de construção robustos para a criação de agentes que podem raciocinar, planejar, utilizar ferramentas, interagir dinamicamente com os usuários e colaborar efetivamente em equipe. 
Neste tutorial avançado, você dominará: 
· 
· 
Definição e uso da ferramenta: criação de funções Python (tools) que concedem aos agentes habilidades específicas (como buscar dados) e instruem os agentes sobre como usá- 
las de forma eficaz. 
Flexibilidade Multi-LLM: configuração de agentes para utilizar vários LLMs lideres (Gemini, GPT-40, Claude Sonnet) por meio da integração do LiteLLM, permitindo que você escolha o 
melhor modelo para cada tarefa. 
Delegação e colaboração de agentes: projetando subagentes especializados e permitindo o roteamento automático (auto flow) de solicitações de usuários para o 
agente mais apropriado dentro de uma equipe. 
Estado de sessão para memória: utilizar Session State e 
Tool Context permitir que os agentes se lembrem de 
Índice 
Etapa 1: Seu primeiro agente - Consulta básica do clima 
Etapa 2: Adotando vários modelos com o LiteLLM [opcional] 
Etapa 3: Construindo uma Equipe de Agentes - Delegação para Saudações e Despedidas 
Etapa 4: Adicionando memória e personalização com estado de sessão 
Etapa 5: Adicionando segurança - Guardrail de entrada com before_model_callback 
Etapa 6: Adicionando segurança - Guardrail do argumento da ferramenta 
(before_tool_callback) 
Conclusão: sua equipe de agentes está pronta! 
B 
ཕྱས་ལ་ Pian ཤསཔ པབསཕ་་་པབབ་ 
informações em turnos de conversação, levando a interações 
mais contextuais. 
Guardrails de segurança com retornos de chamada: implementar before_model_callback e 
before_tool_callback inspecionar, modificar ou bloquear solicitações/uso de ferramentas com base em regras predefinidas, aumentando a segurança e o controle do aplicativo. 
Expectativa do estado final: 
Ao concluir este tutorial, você terá construído um sistema Weather 
Bot multiagente funcional. Este sistema não apenas fornecerá informações meteorológicas, mas também lidará com sutilezas de conversação, lembrará a última cidade verificada e operará dentro de limites de segurança definidos, tudo orquestrado com o ADK. 
Pré-requisitos: 
Sólido conhecimento de programação Python. 
Familiaridade com Large Language Models (LLMs), APIs e o conceito de agentes. 
! Crucial: Conclusão do(s) tutorial(s) de Início Rápido do ADK ou conhecimento básico equivalente dos conceitos básicos do ADK (Agente, Executador, Serviço de Sessão, 
uso básico de ferramentas). Este tutorial se baseia 
diretamente nesses conceitos. 
Chaves de API para os LLMs que você pretende usar (por exemplo, Google Al Studio para Gemini, OpenAl Platform, Anthropic Console). 
Nota sobre o ambiente de execução: 
Este tutorial é estruturado para ambientes de notebooks interativos, como Google Colab, Colab Enterprise ou Jupyter. Lembre-se do 
seguinte: 
Execução de código assíncrono: ambientes de notebook lidam com código assíncrono de forma diferente. Você verá exemplos usando await (adequado quando um loop de eventos já está em execução, comum em notebooks) ou 
asyncio.run() (frequentemente necessário ao executar como um script independente .py ou em configurações específicas de notebook). Os blocos de código fornecem orientação para 
ambos os cenários. 
• Configuração manual do executor/sessão: as etapas envolvem a criação explícita Runner de 
SessionService instâncias. Essa abordagem é mostrada porque oferece controle preciso sobre o ciclo de vida de execução do agente, o gerenciamento de sessões e a persistência de estado. 
Alternativa: Usando as ferramentas integradas do ADK (interface de usuário da Web / CLI / servidor de API) 
Se preferir uma configuração que lide com o executor e o gerenciamento de sessão automaticamente usando as ferramentas padrão do ADK, você pode encontrar o código equivalente estruturado para essa finalidade aqui. Essa versão foi projetada 
para ser executada diretamente com comandos como adk 
web (para uma interface web), adk run (para interação com a CLI) 
ou adk api_server (para expor uma API). Siga as 
README.md instruções fornecidas nesse recurso alternativo. 
Pronto para montar sua equine de agentes? Vamos lál 
momo para muna sua equipe do ayomeo. vantivo iu. 
# @title Step 8: Setup and Installation 
# Install ADK and LiteLLM for multi-model support 
!pip install google-adk -q 
!pip install litellm -q 
print("Installation complete.") 
# @title Import necessary libraries 
import os 
import asyncio 
from google.adk.agents import Agent 
from google.adk.models.lite_llm import LiteLlm # For multi from google.adk.sessions import InMemorySessionService 
from google.adk.runners import Runner 
from google.genai import types # For creating message Cont 
import warnings 
# Ignore all warnings 
warnings.filterwarnings("ignore") 
import logging 
logging.basicConfig (level-logging.ERROR) 
print("Libraries imported.") 
# @title Configure API Keys (Replace with your actual keys 
# 
IMPORTANT: Replace placeholders with your real API k 
# Gemini API Key (Get from Google AI Studio: https://aistu os.environ[ "GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY" # <-- 
# [Optional] 
# OpenAI API Key (Get from OpenAI Platform: https://platfo os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY' # <-- 
# [Optional] 
# Anthropic API Key (Get from Anthropic Console: https://c os.environ['ANTHROPIC_API_KEY'] = 'YOUR_ANTHROPIC_API_KEY' 
# Verify Keys (Optional Check) 
print("API Keys Set: ") 
print (f"Google API Key set: {'Yes' if os.environ.get('GOOG print (f"OpenAI API Key set: {'Yes' if os.environ.get('OPEN print (f" Anthropic API Key set: {'Yes' if os.environ.get('A 
# Configure ADK to use API keys directly (not Vertex AI fo os.environ [ "GOOGLE_GENAI_USE_VERTEXAI"] = "False" 
# @markdown **Security Note:** It's best practice to manag 
# 
Define Model Constants for easier use --- 
# More supported models can be referenced he Copiar para a área de transferência MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash" 
# More supported models can be referenced here: https://do MODEL_GPT_40 = "openai/gpt-4.1" # You can also try: gpt-4. 
# More supported models can be referenced here: https://do MODEL_CLAUDE SONNET = "anthropic/claude-sonnet-4-20250514" 
print("\nEnvironment configured.") 
Etapa 1: Seu primeiro agente - Consulta básica do clima 
Vamos começar construindo o componente fundamental do nosso Weather Bot: um único agente capaz de executar uma tarefa específica - consultar informações meteorológicas. Isso envolve a criação de duas peças principais: 
1. Uma ferramenta: uma função Python que equipa o agente 
com a capacidade de buscar dados meteorológicos. 
2. Um agente: o "cérebro" da IA que entende a solicitação do 
usuário, sabe que tem uma ferramenta meteorológica e decide quando e como usá-la. 
1. Defina a ferramenta ( get_weather) 
No ADK, as ferramentas são os blocos de construção que fornecem aos agentes recursos concretos que vão além da simples geração de texto. Normalmente, são funções comuns do Python que realizam ações específicas, como chamar uma API, consultar 
um banco de dados ou realizar cálculos. 
Nossa primeira ferramenta fornecerá um relatório meteorológico simulado. Isso nos permite focar na estrutura do agente sem precisar ainda de chaves de API externas. Posteriormente, você poderá facilmente trocar essa função simulada por uma que chame um serviço meteorológico real. 
Conceito-chave: Docstrings são cruciais! O LLM do agente depende muito da docstring da função para entender: 
• O que a ferramenta faz. 
• Quando usar. 
• Quais argumentos são necessários (city: str). 
• Quais informações ele retorna. 
Boas Práticas: Escreva docstrings claras, descritivas e precisas para suas ferramentas. Isso é essencial para que o LLM utilize a 
ferramenta corretamente. 
@title Define the get_weather Tool 
f get_weather (city: str) -> dict: 
"""Retrieves the current weather report for a specified ci 
Args: 
city (str): The name of the city (e.g., "New York", "L 
Returns: 
dict: A dictionary containing the weather information. 
Includes a 'status' key ('success' or 'error'). If 'success', includes a 'report' key with weath If 'error', includes an 'error_message' key. 
7111 
print (f" Tool: get_weather called for city: {city} city_normalized = city.lower().replace("", "") # Basic no 
# Mock weather data mock_weather_db = { 
} 
"newyork": {"status": 'success", "report": "The weathe "london": {"status": " success" "report": "It's cloudy 
"tokyo": {"status": "success", "report": "Tokyo is exp 
if city_normalized in mock_weather_db: 
else: 
return mock_weather_db [city_normalized] 
return {"status": "error", "error_message": f"Sorry, I 
Example tool usage (optional test) 
int (get_weather ("New York")) 
int (get_weather ("Paris")) 
2. Defina o Agente (weather_agent) 
Agora, vamos criar o Agente em si. Um Agent no ADK orquestra a interação entre o usuário, o LLM e as ferramentas disponíveis. 
Nós o configuramos com vários parâmetros-chave: 
⚫ name : Um identificador exclusivo para este agente (por 
exemplo, "weather_agent_v1"). 
• model: Especifica qual LLM usar (por exemplo, 
MODEL_GEMINI_2_0_FLASH). Começaremos com um modelo 
Gemini específico. 
• description: Um resumo conciso do propósito geral do 
agente. Isso se torna crucial mais tarde, quando outros agentes precisam decidir se delegam tarefas a este agente. 
• instruction: Orientação detalhada para o LLM sobre como se 
comportar, sua persona, seus objetivos e, especificamente, como e quando utilizar sua atribuição tools. 
⚫ tools : Uma lista contendo as funções reais da ferramenta 
Python que o agente tem permissão para usar (por exemplo, 
[get_weather]). 
Boas Práticas: Forneça instruções claras e específicas 
instruction. Quanto mais detalhadas forem as instruções, melhor 
o LLM poderá compreender seu papel e como usar suas ferramentas de forma eficaz. Seja explícito sobre o tratamento de erros, se necessário. 
Prática recomendada: escolha descritivos name e 
description valores. Eles são usados internamente pelo ADK e são essenciais para recursos como delegação automática (abordada posteriormente). 
# @title Define the Weather Agent 
# Use one of the model constants defined earlier 
AGENT_MODEL = MODEL_GEMINI_2_0_FLASH # Starting with Gemin 
weather_agent = Agent ( 
name="weather_agent_v1", 
model=AGENT_MODEL, # Can be a string for Gemini or a L description= "Provides weather information for specific instruction="You are a helpful weather assistant. " 
"When the user asks for the weather in a s "use the 'get_weather' tool to find the in "If the tool returns an error, inform the "If the tool is successful, present the we tools=[get_weather], # Pass the function directly 
) 
print (f" Agent (weather_agent.name}' created using model 
3. Configurar o Runner e o Serviço de Sessão 
Para gerenciar conversas e executar o agente, precisamos de mais dois componentes: 
• SessionService : Responsável por gerenciar o histórico de 
conversas e o estado de diferentes usuários e sessões. Esta 
InMemorySessionService é uma implementação simples que armazena tudo na memória, adequada para testes e aplicações simples. Ela rastreia as mensagens trocadas. Exploraremos a persistência de estado com mais detalhes na Etapa 4. 
• Runner : O mecanismo que orquestra o fluxo de interação. Ele recebe a entrada do usuário, encaminha-a para o agente apropriado, gerencia chamadas para o LLM e ferramentas com base na lógica do agente, processa atualizações de sessão por meio do SessionService e gera eventos que representam o progresso da interação. 
# @title Setup Session Service and Runner 
# 
Session Management 
# Key Concept: SessionService stores conversation history # InMemorySessionService is simple, non-persistent storage session_service = InMemorySessionService() 
# Define constants for identifying the interaction context APP_NAME = "weather_tutorial_app" 
USER_ID = "user_1" 
SESSION_ID = "session_001" # Using a fixed ID for simplici 
# Create the specific session where the conversation will session= await session_service.create_session( 
B 
) 
app_name=APP_NAME, user_id=USER_ID, 
session_id=SESSION_ID 
print (f" Session created: App='{APP_NAME}', User='{USER_ID} 
#--- Runner --- 
# Key Concept: Runner orchestrates the agent execution loo 
Runner( 
runner = 
) 
agent weather_agent, # The agent we want to run app_name=APP_NAME, # Associates runs with our app 
session_service-session_service # Uses our session man 
print (f" Runner created for agent '{runner.agent.name}'.") 
4. Interaja com o agente 
Precisamos de uma maneira de enviar mensagens ao nosso agente 
e receber suas respostas. Como as chamadas do LLM e as execuções de ferramentas podem levar tempo, o ADK 
Runner opera de forma assíncrona. 
Definiremos uma async função auxiliar (call_agent_async) que: 
1. Recebe uma sequência de consulta do usuário. 
2. Empacota-o no formato ADK Content. 
3. Chamadas runner.run_async, fornecendo o contexto do 
usuário/sessão e a nova mensagem. 
4. Itera pelos eventos gerados pelo executor. Os eventos 
representam etapas na execução do agente (por exemplo, chamada de ferramenta solicitada, resultado da ferramenta 
recebido, pensamento intermediário do LLM, resposta final). 
5. Identifica e imprime o evento de resposta final usando 
event.is_final_response(). 
Por quê async ? Interações com LLMs e potencialmente ferramentas (como APIs externas) são operações limitadas por E/S. O uso asyncio permite que o programa lide com essas operações de forma eficiente, sem bloquear a execução. 
# @title Define Agent Interaction Function 
from google.genai import types # For creating message Cont 
async def call_agent_async (query: str, runner, user_id, se "Sends a query to the agent and prints the final respo print (f"\n>>> User Query: {query}") 
# Prepare the user's message in ADK format content types. Content (role='user', parts=[types. Part (t 
final_response_text 
= "Agent did not produce a final res 
# Key Concept: run_async executes the agent logic and yi # We iterate through events to find the final answer. async for event in runner.run_async (user_id=user_id, ses # You can uncomment the line below to see *all* even # print(f" [Event] Author: {event.author}, Type: {t 
# Key Concept: is_final_response() marks the conclud if event.is_final_response(): 
if event.content and event.content.parts: 
# Assuming text response in the first part final_response_text = event.content.parts[0]. elif event.actions and event.actions.escalate: # final_response_text = f "Agent escalated: {eve # Add more checks here if needed (e.g., specific break # Stop processing events once the final re 
print("<<<<<< Agent Response: (final_response_text}") 
5. Conduza a conversa 
Por fim, vamos testar nossa configuração enviando algumas 
consultas ao agente. Encapsulamos nossas async chamadas em 
B 
-- 
uma async função principal e a executamos usando await. 
Assista ao resultado: 
· 
Veja as consultas dos usuários. 
• Observe os --- Tool: get_weather called... --- logs quando o agente usa a ferramenta. 
• Observe as respostas finais do agente, incluindo como ele lida com o caso em que os dados meteorológicos não estão disponíveis (para Paris). 
# @title Run the Initial Conversation 
# We need an async function to await our interaction helpe async def run_conversation(): 
await call_agent_async("What is the weather like in Lo 
runner runner, user_id=USER_ID, session_id=SESSION_ 
await call_agent_async("How about Paris?", 
runner runner, user_id=USER_ID, session_id=SESSION_ 
await call_agent_async("Tell me the weather in New Yor 
runner=runner, user_id=USER_ID, session_id=SESSION_ 
# Execute the conversation using await in an async context await run_conversation() 
#--- OR 
# Uncomment the following lines if running as a standard P 
# import asyncio 
__name__ "__main__": 
# if 
# 
try: 
# 
asyncio.run(run_conversation()) 
except Exception as e: 
print (f"An error occurred: {e}") 
Parabéns! Você criou e interagiu com sucesso com seu primeiro agente ADK. Ele entende a solicitação do usuário, usa uma ferramenta para encontrar informações e responde adequadamente com base no resultado da ferramenta. 
Na próxima etapa, exploraremos como alternar facilmente o Modelo de Linguagem subjacente que alimenta este agente. 
Etapa 2: Adotando vários modelos com o LiteLLM [opcional] 
Na Etapa 1, construímos um Agente Meteorológico funcional baseado em um modelo Gemini específico. Embora eficazes, aplicações reais frequentemente se beneficiam da flexibilidade de usar diferentes Modelos de Linguagem Ampla (LLMs). Por quê? 
• Desempenho: alguns modelos se destacam em tarefas específicas (por exemplo, codificação, raciocínio, escrita criativa). 
• Custo: Diferentes modelos têm faixas de preço variadas. 
Capacidades: Os modelos oferecem diversos recursos, tamanhos de janela de contexto e opções de ajuste fino. 
· 
• Disponibilidade/Redundância: Ter alternativas garante que 
seu aplicativo permaneça funcional mesmo se um provedor tiver problemas. 
O ADK facilita a alternância entre modelos por meio de sua integração com a biblioteca LiteLLM. O LiteLLM atua como uma 
interface consistente para mais de 100 LLMs diferentes. 
Nesta etapa, iremos: 
1. Aprenda a configurar um ADK Agent para usar modelos de 
provedores como OpenAI (GPT) e Anthropic (Claude) usando o 
LiteLlm wrapper. 
2. Defina, configure (com suas próprias sessões e executores) e 
teste imediatamente instâncias do nosso Weather Agent, cada uma apoiada por um LLM diferente. 
3. Interaja com esses diferentes agentes para observar possíveis 
variações em suas respostas, mesmo ao usar a mesma ferramenta subjacente. 
1. Import LiteLlm 
Importamos isso durante a configuração inicial (Etapa O), mas é o componente-chave para suporte a vários modelos: 
# @title 1. Import Litellm 
from google.adk.models.lite_llm import Litellm 
2. Definir e testar agentes multimodelo 
Em vez de passar apenas uma string de nome de modelo (que é o padrão dos modelos Gemini do Google), encapsulamos a string de identificador de modelo desejada dentro da LiteLlm classe. 
· 
Conceito-chave: LiteLlm Wrapper: a 
LiteLlm(model="provider/model_name") sintaxe informa ao ADK para rotear solicitações para esse agente por meio da biblioteca LiteLLM para o provedor de modelo especificado. 
Certifique-se de ter configurado as chaves de API necessárias para OpenAl e Anthropic na Etapa O. Usaremos a 
call_agent_async função (definida anteriormente, que agora aceita runner, user_ide session_id ) para interagir com cada agente imediatamente após sua configuração. 
Cada bloco abaixo irá: 
• Defina o agente usando um modelo LiteLLM específico ( 
MODEL_GPT_40 OU MODEL CLAUDE_SONNET). 
• Crie uma nova InMemorySessionService sessão separada especificamente para o teste desse agente. Isso mantém os históricos de conversas isolados para esta demonstração. 
• Crie uma Runner configuração para o agente específico e seu serviço de sessão. 
Ligue imediatamente call_agent_async para enviar uma consulta e testar o agente. 
Prática recomendada: use constantes para nomes de modelos (como MODEL_GPT_40, MODEL CLAUDE_SONNET definido na Etapa 0) para evitar erros de digitação e tornar o código mais fácil de gerenciar. 
Tratamento de Erros: Encapsulamos as definições do agente em try...except blocos. Isso evita que toda a célula de código falhe caso uma chave de API para um provedor específico esteja ausente ou inválida, permitindo que o tutorial prossiga com os modelos configurados. 
Primeiro, vamos criar e testar o agente usando o GPT-40 da OpenAl. 
# @title Define and Test GPT Agent 
# Make sure 'get_weather' function from Step 1 is defined 
# Make sure 'call_agent_async' is defined from earlier. 
# 
--- 
Agent using GPT-40 
weather_agent_gpt = None # Initialize to None 
runner_gpt = None 
# Initialize runner to None 
try: 
weather_agent_gpt = Agent ( 
) 
name="weather_agent_gpt", 
# Key change: Wrap the LiteLLM model identifier model-LiteLlm (model =MODEL_GPT_40), description="Provides weather information (using G instruction="You are a helpful weather assistant p "Use the 'get_weather' tool for city w "Clearly present successful reports or tools=[get_weather], # Re-use the same tool 
print (f" Agent (weather_agent_gpt.name}' created using 
# InMemorySessionService is simple, non-persistent sto session_service_gpt InMemorySessionService() # Creat 
# Define constants for identifying the interaction con APP_NAME_GPT = "weather_tutorial_app_gpt" # Unique app USER_ID_GPT = "user_1_gpt" 
SESSION_ID_GPT = "session_001_gpt" # Using a fixed ID 
# Create the specific session where the conversation w session_gpt = await session_service_gpt.create_session 
) 
app_name=APP_NAME_GPT, user_id=USER_ID_GPT, 
session_id=SESSION_ID_GPT 
print (f" Session created: App='{APP_NAME_GPT}', User='{ 
# Create a runner specific to this agent and its sessi runner_gpt = Runner ( 
agent weather_agent_gpt, 
app_name=APP_NAME_GPT, 
# Use the specific ap 
session_service-session_service_gpt # Use the spec 
) 
print (f"Runner created for agent '{runner_gpt.agent.na 
#--- Test the GPT Agent 
print("\n--- Testing GPT Agent ---") 
# Ensure call_agent_async uses the correct runner, use await call_agent_async (query = "What's the weather in 
runner=runner_gpt, 
user_id=USER_ID_GPT, session_id=SESSION_ID_GPT) 
# 
OR 
# Uncomment the following lines if running as a standa #import asyncio 
# if __name__ == "__main__": 
# 
try: 
asyncio.run(call_agent_async(query = "What's 
runner=runner_gpt, 
user_id=USER_ID_GPT, 
session_id=SESSION_ID_GPT) 
except Exception as e: 
print (f" An error occurred: {e}") 
except Exception as e: 
print (f" Could not create or run GPT agent '{MODEL_G 
Em seguida, faremos o mesmo com Claude Sonnet, da Anthropic. 
# @title Define and Test Claude Agent 
# Make sure 'get_weather' function from Step 1 is defined 
# Make sure 'call_agent_async' is defined from earlier. 
#--- Agent using Claude Sonnet 
weather_agent_claude = None # Initialize to None runner_claude = None 
# Initialize runner to None 
try: 
weather_agent_claude 
= 
Agent ( 
name="weather_agent_claude", 
# Key change: Wrap the LiteLLM model identifier model-LiteLlm (model =MODEL_CLAUDE_SONNET), description="Provides weather information (using C instruction="You are a helpful weather assistant p 
"Use the 'get_weather' tool for city w "Analyze the tool's dictionary output "Clearly present successful reports or 
B 
ດ 
) 
tools=[get_weather], # Re-use the same tool 
print (f" Agent '{weather_agent_claude.name}' created us 
# InMemorySessionService is simple, non-persistent sto session_service_claude = InMemorySessionService() # Cr 
# Define constants for identifying the interaction con APP_NAME_CLAUDE = "weather_tutorial_app_claude" # Uniq USER_ID_CLAUDE = "user_1_claude" 
SESSION_ID_CLAUDE = "session_001_claude" # Using a fix 
# Create the specific session where the conversation w session_claude = await session_service_claude.create_s 
) 
app_name=APP_NAME_CLAUDE, user_id=USER_ID_CLAUDE, 
session_id=SESSION_ID_CLAUDE 
print (f"Session created: App='{APP_NAME_CLAUDE}', User 
# Create a runner specific to this agent and its sessi runner_claude = Runner ( 
agent weather_agent_claude, 
app_name=APP_NAME_CLAUDE, 
# Use the specific 
session_service-session_service_claude # Use the s 
) 
print (f"Runner created for agent (runner_claude.agent 
# 
Test the Claude Agent 
print("\n--- Testing Claude Agent ---") 
# Ensure call_agent_async uses the correct runner, use await call_agent_async (query = "Weather in London plea 
runner=runner_claude, 
user_id=USER_ID_CLAUDE, 
session_id=SESSION_ID_CLAUDE) 
# 
OR --- 
# Uncomment the following lines if running as a standa 
# import asyncio 
# if __name__ == "__main__": 
# 
try: 
asyncio.run(call_agent_async (query= "Weathe 
runner=runner_claude, 
user_id=USER_ID_CLAUDE, 
session_id=SESSION_ID_CLAUDE) 
except Exception as e: 
print (f" An error occurred: {e}") 
except Exception as e: 
print(f" 
Could not create or run Claude agent '{MODE 
Observe atentamente a saída de ambos os blocos de código. Você 
deverá ver: 
1. Cada agente (weather_agent_gpt, weather_agent_claude) é 
criado com sucesso (se as chaves de API forem válidas). 
2. Uma sessão dedicada e um corredor são configurados para 
cada um. 
3. Cada agente identifica corretamente a necessidade de usar a 
get_weather ferramenta ao processar a consulta (você verá o 
Tool: get_weather called...log). 
4. A lógica da ferramenta subjacente permanece idêntica, sempre 
retornando nossos dados simulados. 
5. No entanto, a resposta textual final gerada por cada agente 
pode diferir ligeiramente em fraseado, tom ou formatação. Isso ocorre porque o prompt de instrução é interpretado e executado por diferentes LLMS (GPT-40 vs. Claude Sonnet). 
Esta etapa demonstra o poder e a flexibilidade que o ADK + LiteLLM oferecem. Você pode facilmente experimentar e implementar agentes usando vários LLMs, mantendo a lógica principal do seu aplicativo (ferramentas, estrutura fundamental do agente) 
consistente. 
Na próxima etapa, deixaremos de ter apenas um agente e criaremos uma pequena equipe onde os agentes poderão delegar 
tarefas uns aos outros! 
Etapa 3: Construindo uma Equipe de Agentes - Delegação para Saudações e Despedidas 
Nas Etapas 1 e 2, criamos e experimentamos um único agente focado exclusivamente em consultas meteorológicas. Embora eficaz para sua tarefa específica, aplicações reais frequentemente envolvem lidar com uma variedade maior de interações do usuário. Poderíamos continuar adicionando mais ferramentas e instruções complexas ao nosso único agente meteorológico, mas isso pode rapidamente se tornar incontrolável e menos eficiente. 
Uma abordagem mais robusta é construir uma Equipe de Agentes. Isso envolve: 
1. Criação de vários agentes especializados, cada um projetado 
para uma capacidade específica (por exemplo, um para clima, 
um para saudações, um para cálculos). 
2. Designar um agente raiz (ou orquestrador) que recebe a 
solicitação inicial do usuário. 
3. Permitir que o agente raiz delegue a solicitação ao subagente 
especializado mais apropriado com base na intenção do 
usuário. 
Por que criar uma Equipe de Agentes? 
• Modularidade: mais fácil de desenvolver, testar e manter 
agentes individuais. 
· 
Especialização: Cada agente pode ser ajustado (instruções, 
escolha de modelo) para sua tarefa específica. 
• Escalabilidade: Mais simples adicionar novos recursos adicionando novos agentes. 
• Eficiência: Permite usar modelos potencialmente mais simples/baratos para tarefas mais simples (como saudações). 
Nesta etapa, iremos: 
1. Defina ferramentas simples para lidar com saudações ( 
say_hello) e despedidas ( say goodbye). 
2. Crie dois novos subagentes especializados: greeting_agent e 
farewell_agent. 
3. Atualize nosso principal agente climático (weather_agent_v2) 
para atuar como agente raiz. 
4. Configure o agente raiz com seus subagentes, habilitando a 
delegação automática. 
5. Teste o fluxo de delegação enviando diferentes tipos de 
solicitações ao agente raiz. 
1. Definir ferramentas para subagentes 
Primeiro, vamos criar as funções Python simples que servirão como ferramentas para nossos novos agentes especialistas. Lembre-se: docstrings claras são essenciais para os agentes que as utilizarão. 
# @title Define Tools for Greeting and Farewell Agents from typing import Optional # Make sure to import Optional 
# Ensure 'get_weather' from Step 1 is available if running 
# def get_weather (city: str) -> dict: ... (from Step 1) 
def say_hello (name: Optional [str] = None) -> str: 
"""Provides a simple greeting. If a name is provided, 
ຕ 
Args: 
name (str, optional): The name of the person to gr 
Returns: 
str: A friendly greeting message. 
if name: 
else: 
greeting 
= 
f"Hello, {name}!" 
print("--- Tool: say_hello called with name: {nam 
greeting = "Hello there!" # Default greeting if na print (f" Tool: say_hello called without a speci return greeting 
def say goodbye() -> str: 
"""Provides a simple farewell message to conclude the print (f" Tool: say goodbye called ---") return "Goodbye! Have a great day." 
print("Greeting and Farewell tools defined.") 
# Optional self-test 
print (say_hello("Alice")) 
print(say_hello()) # Test with no argument (should use def print(say_hello (name=None)) # Test with name explicitly as 
2. Defina os Subagentes (Saudação e Despedida) 
Agora, crie as Agent instâncias para nossos especialistas. Observe o alto foco deles instruction e, principalmente, a clareza deles description. Essa description é a principal informação que o agente raiz usa para decidir quando delegar a esses subagentes. 
Prática recomendada: Os campos dos subagentes description devem resumir de forma precisa e concisa suas capacidades específicas. Isso é crucial para uma delegação 
automática eficaz. 
Melhor prática: os campos dos subagentes instruction devem ser adaptados ao seu escopo limitado, informando-lhes exatamente o que fazer e o que não fazer (por exemplo, "Sua única 
tarefa é..."). 
# @title Define Greeting and Farewell Sub-Agents 
# If you want to use models other than Gemini, Ensure Lite 
# from google.adk.models.lite_llm import Litellm 
# MODEL_GPT_40, MODEL CLAUDE_SONNET etc. should be defined 
# Or else, continue to use: model = MODEL_GEMINI_2_0_FLASH 
#--- 
- Greeting Agent 
greeting_agent = None 
try: 
greeting agent = Agent ( 
) 
# Using a potentially different/cheaper model for model MODEL_GEMINI_2_0_FLASH, 
# model=LiteLlm (model =MODEL_GPT_40), # If you woul name="greeting_agent", 
instruction="You are the Greeting Agent. Your ONLY 
"Use the 'say_hello' tool to generate "If the user provides their name, make "Do not engage in any other conversati description="Handles simple greetings and hellos u tools=[say_hello], 
print (f"✓ Agent '{greeting_agent.name}' created using except Exception as e: 
print (f" Could not create Greeting agent. Check API 
# --- Farewell Agent 
farewell_agent = None 
try: 
farewell_agent = Agent ( 
# Can use the same or a different model model = MODEL GEMINI_2_0_FLASH, 
#model-LiteLlm (model=MODEL_GPT_40), # If you woul name="farewell_agent", 
instruction="You are the Farewell Agent. Your ONLY "Use the 'say goodbye' tool when the u "(e.g., using words like 'bye', 'goodb "Do not perform any other actions.", 
B 
) 
description="Handles simple farewells and goodbyes 
tools=[say goodbye], 
print (f"✓ Agent '{farewell_agent.name}' created using except Exception as e: 
print(f" Could not create Farewell agent. Check API 
3. Defina o agente raiz (Weather Agent v2) com subagentes 
Agora, atualizamos nosso weather_agent. As principais mudanças são: 
Adicionando o sub_agents parâmetro: Passamos uma lista contendo as instâncias greeting_agent e farewell_agent que 
acabamos de criar. 
Atualizando o instruction: Informamos explicitamente ao agente raiz sobre seus subagentes e quando ele deve delegar 
tarefas a eles. 
Conceito-chave: Delegação Automática (Fluxo Automático) Ao fornecer a sub_agents lista, o ADK habilita a delegação automática. Quando o agente raiz recebe uma consulta de usuário, seu LLM considera não apenas suas próprias instruções e ferramentas, mas também as description de cada subagente. Se o LLM determinar 
que uma consulta se alinha melhor com a capacidade descrita de um subagente (por exemplo, "Lida com saudações simples"), ele gerará automaticamente uma ação interna especial para transferir o controle para esse subagente naquele turno. O subagente então processa a consulta usando seu próprio modelo, instruções e 
ferramentas. 
Prática recomendada: Garanta que as instruções do agente raiz orientem claramente suas decisões de delegação. Mencione os subagentes pelo nome e descreva as condições sob as quais a delegação deve ocorrer. 
# @title Define the Root Agent with Sub-Agents 
# Ensure sub-agents were created successfully before defin 
# Also ensure the original 'get_weather' tool is defined. root_agent = None 
runner_root = None # Initialize runner 
if greeting_agent and farewell_agent and 'get_weather' in # Let's use a capable Gemini model for the root agent root_agent_model = MODEL_GEMINI_2_0_FLASH 
weather_agent_team = Agent( 
) 
name="weather_agent_v2", # Give it a new version n model=root_agent_model, 
description="The main coordinator agent. Handles w instruction="You are the main Weather Agent coordi 
"Use the 'get_weather' tool ONLY for s "You have specialized sub-agents: 
"1. 'greeting_agent': Handles simple g "2. 'farewell_agent': Handles simple f "Analyze the user's query. If it's a g "If it's a weather request, handle it "For anything else, respond appropriat tools=[get_weather], # Root agent still needs the # Key change: Link the sub-agents here! sub_agents=[greeting_agent, farewell_agent] 
print (f" Root Agent (weather_agent_team.name}' crea 
else: 
- 
print("X Cannot create root agent because one or more if not greeting_agent: print(" Greeting Agent is mis if not farewell_agent: print(" - Farewell Agent is mis if 'get_weather' not in globals(): print(" - get_weath 
4. Interaja com a equipe de agentes 
Agora que definimos nosso agente raiz (weather_agent_team - 
Nota: Certifique-se de que o nome desta variável corresponda ao 
" 
definido no bloco de código anterior, provavelmente # @title 
Define the Root Agent with Sub-Agents, que pode tê-lo nomeado root_agent) com seus subagentes especializados, vamos testar o mecanismo de delegação. 
O seguinte bloco de código irá: 
1. Defina uma async função run_team_conversation. 
2. Dentro desta função, crie uma nova InMemorySessionService 
sessão dedicada e específica ( session_001_agent_team) apenas para este teste. Isso isola o histórico de conversas para testar a dinâmica da equipe. 
3. Crie um Runner ( runner_agent_team) configurado para usar 
nosso weather_agent_team (o agente raiz) e o serviço de sessão dedicado. 
4. Use nossa função atualizada call_agent_async para enviar 
diferentes tipos de consultas (saudação, solicitação de previsão do tempo, despedida) para o runner_agent_team. Passamos explicitamente o executor, o ID do usuário e o ID da sessão para 
este teste específico. 
5. Execute a run_team_conversation função imediatamente. 
Esperamos o seguinte fluxo: 
1. A consulta "Olá!" vai para runner_agent_team. 
2. O agente raiz (weather_agent_team) recebe e, com base em 
suas instruções e na greeting_agent descrição do, delega a tarefa. 
3. greeting agent manipula a consulta, chama sua 
say_hello ferramenta e gera a resposta. 
4. A consulta "Qual é o clima em Nova York?" não é delegada e é 
tratada diretamente pelo agente raiz usando sua 
get_weather ferramenta. 
5. A consulta "Obrigado, tchau!" é delegada ao farewell_agent, 
que usa sua say goodbye ferramenta. 
# @title Interact with the Agent Team 
import asyncio # Ensure asyncio is imported 
# Ensure the root agent (e.g., 'weather_agent_team' or 'ro 
# Ensure the call_agent_async function is defined. 
# Check if the root agent variable exists before defining root_agent_var_name = 'root_agent' # Default name from Ste if 'weather_agent_team' in globals(): # Check if user used 
root_agent_var_name = 'weather_agent_team' 
elif 'root_agent' not in globals(): 
print("! Root agent ('root_agent' or 'weather_agent_t # Assign a dummy value to prevent NameError later if t root_agent = None # Or set a flag to prevent execution 
# Only define and run if the root agent exists 
if root_agent_var_name in globals() and globals ( ) [root_age 
# Define the main async function for the conversation # The 'await' keywords INSIDE this function are necess 
async def run_team_conversation(): 
print("\n--- Testing Agent Team Delegation ---") session_service = InMemorySessionService() 
APP_NAME = "weather_tutorial_agent_team" 
USER_ID = "user_1_agent_team" 
SESSION_ID = "session_001_agent_team" 
session= await session_service.create_session( 
app_name=APP_NAME, user_id=USER_ID, session_id 
) 
print (f" Session created: App='{APP_NAME}', User='{ 
actual_root_agent = globals() [root_agent_var_name] runner_agent_team Runner ( # Or use InMemoryRunne 
agent actual_root_agent, 
) 
app_name=APP_NAME, 
session_service-session_service 
print (f"Runner created for agent (actual_root_age 
# 
# 
Interactions using await (correct within asy await call_agent_async (query= "Hello there!", 
runner=runner_agent_team, 
user_id=USER_ID, 
session_id=SESSION_ID) 
await call_agent_async (query= "What is the weathe 
runner=runner_agent_team, 
user_id=USER_ID, 
session_id=SESSION_ID) 
await call_agent_async (query= "Thanks, bye!", 
runner=runner_agent_team, 
user_id=USER_ID, session_id=SESSION_ID) 
Execute the run_team_conversation` async functi # Choose ONE of the methods below based on your enviro # Note: This may require API keys for the models used! 
# METHOD 1: Direct await (Default for Notebooks/Async # If your environment supports top-level await (like C # it means an event loop is already running, so you ca print("Attempting execution using 'await' (default for 
await run_team_conversation() 
# METHOD 2: asyncio.run (For Standard Python Scripts [ # If running this code as a standard Python script fro # the script context is synchronous. asyncio.run() i # create and manage an event loop to execute your asyn # To use this method: 
# 1. Comment out the await run_team_conversation()` 1 # 2. Uncomment the following block: 
import asyncio 
if __name__ == "__main__": # Ensures this runs only wh print("Executing using 'asyncio.run()' (for standa 
try: 
# This creates an event loop, runs your async asyncio.run(run_team_conversation()) 
except Exception as e: 
print (f"An error occurred: {e}") 
else: 
# This message prints if the root agent variable wasn' print("\n! Skipping agent team conversation executior 
Observe atentamente os logs de saída, especialmente as Tool: ... called --- mensagens. Você deve observar: 
• Para "Olá!", a say_hello ferramenta foi chamada (indicando 
greeting agent que foi manipulada). 
• Para "Qual é o clima em Nova York?", a get_weather ferramenta foi chamada (indicando o agente raiz que a manipulou). 
Para "Obrigado, tchau!", a say goodbye ferramenta foi chamada (indicando farewell_agent que foi manipulada). 
Isso confirma o sucesso da delegação automática ! O agente raiz, guiado por suas instruções e pelos description seus s 
sub_agents, encaminhou corretamente as solicitações do usuário para o agente especialista apropriado dentro da equipe. 
Agora você estruturou sua aplicação com vários agentes colaborativos. Esse design modular é fundamental para a construção de sistemas de agentes mais complexos e eficientes. Na próxima etapa, daremos aos nossos agentes a capacidade de memorizar informações entre turnos usando o estado da sessão. 
Etapa 4: Adicionando memória e personalização com estado de sessão 
Até o momento, nossa equipe de agentes consegue lidar com diferentes tarefas por meio de delegação, mas cada interação começa do zero - os agentes não se lembram de conversas anteriores ou das preferências do usuário em uma sessão. Para criar experiências mais sofisticadas e contextualizadas, os agentes 
precisam de memória. O ADK fornece isso por meio do Estado da Sessão. 
O que é estado de sessão? 
• É um dicionário Python (session.state) vinculado a uma sessão de usuário específica (identificada por APP_NAME, 
USER_ID, SESSION_ID). 
Ele persiste com informações em vários turnos de conversação dentro daquela sessão. 
Agentes e ferramentas podem ler e escrever nesse estado, permitindo que eles se lembrem de detalhes, adaptem 
comportamentos e personalizem respostas. 
Como os agentes interagem com o Estado: 
1. ToolContext (Método Primário): As ferramentas podem 
aceitar um ToolContext objeto (fornecido automaticamente pelo ADK se declarado como último argumento). Este objeto fornece acesso direto ao estado da sessão via 
tool_context.state, permitindo que as ferramentas leiam preferências ou salvem resultados durante a execução. 
2. output_key (Resposta do agente de salvamento 
automático): Um Agent pode ser configurado com um 
output_key="your_key". O ADK salvará automaticamente a resposta textual final do agente para uma conversão em 
session.state["your_key"]. 
Nesta etapa, aprimoraremos nossa equipe do Weather Bot por meio de: 
1. Usando um novo InMemorySessionService para demonstrar o 
estado isoladamente. 
2. Inicializando o estado da sessão com uma preferência do 
usuário para temperature_unit. 
3. Criando uma versão com reconhecimento de estado da 
ferramenta meteorológica ( get_weather_stateful) que lê essa preferência ToolContext e ajusta seu formato de saída (Celsius/Fahrenheit). 
4. Atualizar o agente raiz para usar esta ferramenta com estado e 
configurá-lo output_key para salvar automaticamente seu relatório meteorológico final no estado da sessão. 
5. Executar uma conversa para observar como o estado inicial 
afeta a ferramenta, como as mudanças manuais de estado alteram o comportamento subsequente e como output_key a resposta do agente persiste. 
1. Inicializar novo serviço de sessão e estado 
Para demonstrar claramente o gerenciamento de estado sem interferência de etapas anteriores, instanciaremos um novo arquivo InMemorySessionService. Também criaremos uma sessão com um estado inicial definindo a unidade de temperatura preferida do 
usuário. 
# @title 1. Initialize New Session Service and State 
# Import necessary session components 
from google.adk.sessions import InMemorySessionService 
# Create a NEW session service instance for this state dem session_service_stateful = InMemorySessionService() print(" New InMemorySessionService created for state den 
# Define a NEW session ID for this part of the tutorial SESSION_ID_STATEFUL = "session_state_demo_001" USER_ID_STATEFUL = "user_state_demo" 
# Define initial state data user prefers Celsius initial initial_state 
} 
= 
{ 
"user_preference_temperature_unit": "Celsius" 
# Create the session, providing the initial state 
session_stateful = await session_service_stateful.create_s 
) 
app_name=APP_NAME, # Use the consistent app name 
user_id=USER_ID_STATEFUL, 
session_id=SESSION_ID_STATEFUL, 
state-initial_state # <<< Initialize state during crea 
print (f" Session '{SESSION_ID_STATEFUL}' created for use 
# Verify the initial state was set correctly retrieved_session = await session_service_stateful.get_ses 
print("\n--- Initial Session State ---") 
if retrieved_session: 
print (retrieved_session.state) 
else: 
print("Error: Could not retrieve session.") 
2. Criar ferramenta de clima com reconhecimento de estado ( 
get_weather_stateful) 
Agora, criamos uma nova versão da ferramenta de clima. Seu principal recurso é aceitar, tool_context: ToolContext o que lhe permite acessar tool_context.state. Ela lerá 
user_preference_temperature_unit e formatará a temperatura de 
acordo. 
· 
Conceito-chave: ToolContext Este objeto é a ponte que 
permite que a lógica da sua ferramenta interaja com o contexto da sessão, incluindo a leitura e a escrita de variáveis de estado. 
O ADK o injeta automaticamente se definido como o último parâmetro da função da sua ferramenta. 
• Prática recomendada: ao ler o estado, use 
dictionary.get('key', default_value) para lidar com casos em que a chave pode não existir ainda, garantindo que sua ferramenta não trave. 
U 
S 
from google.adk.tools.tool_context import ToolContext 
def get_weather_stateful (city: str, tool_context: ToolCont """Retrieves weather, converts temp unit based on sess print("--- Tool: get_weather_stateful called for {cit 
# Read preference from state 
preferred_unit = tool_context.state.get("user_preferen print (f" Tool: Reading state 'user_preference_tempe 
-- 
city_normalized = city.lower().replace("", "") 
# Mock weather data (always stored in Celsius internal mock_weather_db = { 
"newyork": {"temp_c": 25, "condition": "sunny"}, "london":{"temp_c": 15, "condition": "cloudy"}, "tokyo":{"temp_c": 18, "condition": "light rain"} 
} 
if city_normalized in mock_weather_db: 
data = mock_weather_db [city_normalized] 
temp_c = data["temp_c"] 
condition = data["condition"] 
# Format temperature based on state preference 
if preferred_unit == "Fahrenheit": 
temp_value 
= 
(temp_c* 9/5) + 32 # Calculate F 
temp_unit = "F" 
else: # Default to Celsius 
temp_value = temp_c 
temp_unit = "C" 
report f"The weather in {city.capitalize()} is { result = {"status": "success", "report": report} print("--- Tool: Generated report in {preferred_u 
# Example of writing back to state (optional for t tool_context.state["last_city_checked_stateful"] print (f" --- Tool: Updated state 'last_city_checked 
else: 
return result 
# Handle city not found 
= 
error_msg = f"Sorry, I don't have weather informat print (f" Tool: City '{city}' not found. ---") return {"status": "error", "error_message": error_ 
print("✓ State-aware 'get_weather_stateful' tool defined. 
3. Redefinir subagentes e atualizar o agente raiz 
Para garantir que esta etapa seja independente e seja construída corretamente, primeiro redefinimos o greeting_agent e 
farewell_agent exatamente como estavam na Etapa 3. Em seguida, definimos nosso novo agente raiz ( 
weather_agent_v4_stateful): 
• Ele usa a nova get_weather_stateful ferramenta. 
• Inclui os subagentes de saudação e despedida para delegação. 
• Fundamentalmente, ele define 
output_key="last_weather_report" qual salva 
automaticamente sua resposta meteorológica final no estado 
da sessão. 
# @title 3. Redefine Sub-Agents and Update Root Agent with 
# Ensure necessary imports: Agent, LiteLlm, Runner 
from google.adk.agents import Agent 
from google.adk.models.lite_llm import Litellm 
from google.adk.runners import Runner 
# Ensure tools 'say_hello', 'say goodbye' are defined (fro 
# Ensure model constants MODEL_GPT_40, MODEL GEMINI_2_0_FL 
#--- Redefine Greeting Agent (from Step 3) 
greeting_agent = None 
try: 
greeting_agent = Agent ( 
) 
model=MODEL_GEMINI_2_0_FLASH, 
name="greeting_agent", 
instruction="You are the Greeting Agent. Your ONLY description= "Handles simple greetings and hellos u tools=[say_hello], 
print (f"✓ Agent '{greeting_agent.name}' redefined.") except Exception as e: 
print (f" Could not redefine Greeting agent. Error: { 
#Redefine Farewell Agent (from Step 3) 
farewell_agent = None 
try: 
farewell_agent = Agent ( 
) 
model=MODEL_GEMINI_2_0_FLASH, 
name="farewell_agent", 
instruction="You are the Farewell Agent. Your ONLY description= "Handles simple farewells and goodbyes tools [say goodbye], 
print (f" Agent {farewell_agent.name}' redefined.") except Exception as e: 
print(f" Could not redefine Farewell agent. Error: { 
#--- Define the Updated Root Agent 
root_agent_stateful = None 
runner_root_stateful = None # Initialize runner 
# Check prerequisites before creating the root agent 
if greeting_agent and farewell_agent and 'get_weather_stat 
root_agent_model = MODEL_GEMINI_2_0_FLASH # Choose orc 
root_agent_stateful = 
Agent ( 
name="weather_agent_v4_stateful", # New version na 
model=root_agent_model, 
description="Main agent: Provides weather (state-a instruction="You are the main Weather Agent. Your 
"The tool will format the temperature 
"Delegate simple greetings to 'greetin 
B 
) 
"Handle only weather requests, greetin tools=[get_weather_stateful], # Use the state-awar sub_agents=[greeting_agent, farewell_agent], # Inc output_key="last_weather_report" # <<< Auto-save a 
print (f" Root Agent {root_agent_stateful.name}' cre 
#--- Create Runner for this Root Agent & NEW Session 
runner_root_stateful Runner ( 
) 
else: 
agent=root_agent_stateful, 
app_name=APP_NAME, 
session_service-session_service_stateful # Use the 
print (f"✓ Runner created for stateful root agent '{ru 
print("X Cannot create stateful root agent. Prerequis if not greeting_agent: print(" - greeting_agent defini if not farewell_agent: print(" - farewell_agent defini if 'get_weather_stateful' not in globals(): print(" - 
B 
4. Interaja e teste o fluxo de estado 
Agora, vamos executar uma conversa projetada para testar as interações de estado usando o runner_root_stateful (associado ao nosso agente com estado e o session_service_stateful). Usaremos a call_agent_async função definida anteriormente, garantindo que passamos o executor, o ID do usuário ( 
USER_ID_STATEFUL) e o ID da sessão ( SESSION_ID_STATEFUL) 
corretos. 
O fluxo da conversa será: 
1. Verificar clima (Londres): A 
get_weather_stateful ferramenta deve ler a preferência inicial "Celsius" do estado da sessão inicializado na Seção 1. A 
resposta final do agente raiz (o relatório meteorológico em Celsius) deve ser salva por 
state['last_weather_report'] meio da 
output_key configuração. 
2. Atualizar estado manualmente: modificaremos diretamente o 
estado armazenado na InMemorySessionService instância ( 
session_service_stateful). 
• Por que modificação direta? O 
session_service.get_session() método retorna uma cópia da sessão. Modificar essa cópia não afetaria o estado usado em execuções subsequentes do agente. Para este cenário de teste com InMemorySessionService, 
acessamos o sessions dicionário interno para alterar o valor real user_preference_temperature_unit do estado armazenado para "Fahrenheit". Observação: em aplicações reais, as alterações de estado normalmente são acionadas por ferramentas ou lógica do agente que retornam 
EventActions (state_delta=...), e não por atualizações 
manuais diretas. 
3. Verifique a previsão do tempo novamente (Nova York): A 
get_weather_stateful ferramenta agora deve ler a preferência "Fahrenheit" atualizada do estado e converter a temperatura de acordo. A nova resposta do agente raiz (previsão do tempo em Fahrenheit) substituirá o valor anterior devido 
state['last_weather_report'] à alteração output_key. 
4. Cumprimente o agente: Verifique se a delegação para o agente greeting_agent ainda funciona corretamente em conjunto com as operações com estado. Essa interação se tornará a última resposta salva por output_key nessa sequência específica. 
5. Inspecionar estado final: Após a conversa, recuperamos a 
sessão uma última vez (obtendo uma cópia) e imprimimos seu 
estado para confirmar que 
" 
༦བསསཔ Pས་ས༦VIII----་ ༥u༦ 
user_preference_temperature_unit é de fato "Fahrenheit", observamos o valor final salvo por output_key (que será a saudação nesta execução) e vemos o 
last_city_checked_stateful valor escrito pela ferramenta. 
# @title 4. Interact to Test State Flow and output_key import asyncio # Ensure asyncio is imported 
# Ensure the stateful runner (runner_root_stateful) is ava # Ensure call_agent_async, USER_ID_STATEFUL, SESSION_ID_ST 
if 'runner_root_stateful' in globals() and runner_root_sta # Define the main async function for the stateful conv # The 'await' keywords INSIDE this function are necess async def run_stateful_conversation(): 
print("\n--- Testing State: Temp Unit Conversion & 
# 1. Check weather (Uses initial state: Celsius) print("--- Turn 1: Requesting weather in London (e await call_agent_async (query= "What's the weather 
) 
runner=runner_root_stateful user_id=USER_ID_STATEFUL, session_id=SESSION_ID_STATE 
# 2. Manually update state preference to Fahrenhei print("\n--- Manually Updating State: Setting unit 
try: 
# Access the internal storage directly- THIS # NOTE: In production with persistent services # typically update state via agent actions or # not by direct manipulation of internal stora stored_session session_service_stateful.sess 
stored_session.state["user_preference_temperat 
# Optional: You might want to update the times #import time 
# stored_session.last_update_time = time.time( print(f" Stored session state updated. Curr except KeyError: 
print("Error: Could not retrieve session except Exception as e: 
print("--- Error updating internal session s 
# 3. Check weather again (Tool should now use Fahr # This will also update 'last_weather_report' via print("\n--- Turn 2: Requesting weather in New Yor await call_agent_async(query= "Tell me the weather runner runner_root_stateful 
) 
user_id=USER_ID_STATEFUL, session_id=SESSION_ID_STATE 
# 4. Test basic delegation (should still work) 
# This will update 'last_weather_report' again, ov print("\n--- Turn 3: Sending a greeting ---") 
await call_agent_async (query= "Hi!", 
runner runner_root_stateful 
user_id=USER_ID_STATEFUL, session_id=SESSION_ID_STATE 
) 
2 
# 
Execute the run_stateful_conversation 
async fu 
# Choose ONE of the methods below based on your enviro 
# METHOD 1: Direct await (Default for Notebooks/Async # If your environment supports top-level await (like C # it means an event loop is already running, so you ca print("Attempting execution using 'await' (default for await run_stateful_conversation() 
# METHOD 2: asyncio.run (For Standard Python Scripts [ # If running this code as a standard Python script fro # the script context is synchronous. asyncio.run()` i 
# create and manage an event loop to execute your asyn # To use this method: 
# 1. Comment out the await run_stateful_conversation( # 2. Uncomment the following block: 
import asyncio 
if __name__ == "__main__": # Ensures this runs only wh print("Executing using 'asyncio.run()' (for standa 
try: 
# This creates an event loop, runs your async asyncio.run(run_stateful_conversation()) 
except Exception as e: 
print/f" An error occurred: fal") 
ALL CIIVI 
# 
Inspect final session state after the conversati # This block runs after either execution method comple print("\n--- Inspecting Final Session State ---") final_session = await session_service_stateful.get_ses 
U 
S 
if final_session: 
# Use .get() for safer access to potentially missi print (f"Final Preference: (final_session.state.get print (f"Final Last Weather Report (from output_key print (f"Final Last City Checked (by tool): {final_ # Print full state for detailed view 
# print(f "Full State Dict: (final_session.state}") else: 
print("\nX Error: Could not retrieve final sessic 
else: 
print("\n! Skipping state test conversation. Stateful 
Ao revisar o fluxo da conversa e a impressão final do estado da sessão, você pode confirmar: 
· 
Leitura do estado: A ferramenta de previsão do tempo ( 
get_weather_stateful) leu corretamente 
user_preference_temperature_unit o estado, inicialmente usando "Celsius" para Londres. 
Atualização de estado: a modificação direta alterou com 
sucesso a preferência armazenada para "Fahrenheit". 
• Leitura do estado (atualizado): a ferramenta leu "Fahrenheit" 
· 
· 
quando solicitada a previsão do tempo para Nova York e realizou a conversão. 
Ferramenta de gravação de estado: a ferramenta gravou com 
sucesso last_city_checked_stateful ("Nova York" após a 
segunda verificação de clima) no estado via 
tool_context.state. 
Delegação: A delegação para greeting_agent "Oi!" funcionou corretamente mesmo após modificações de estado. 
⚫ output_key: A resposta 
· 
final output_key="last_weather_report" do agente raiz foi salva com sucesso para cada turno em que o agente raiz foi quem respondeu. Nessa sequência, a última resposta foi a saudação ("Olá!"), o que substituiu o relatório meteorológico na 
chave de estado. 
Estado final: a verificação final confirma que a preferência persistiu como "Fahrenheit". 
Agora você integrou com sucesso o estado da sessão para personalizar o comportamento do agente usando ToolContext, manipulou manualmente o estado para testes 
InMemorySessionService e observou como output_key fornece um mecanismo simples para salvar a última resposta do agente ao estado. Essa compreensão fundamental do gerenciamento de estado é fundamental para implementarmos proteções de segurança usando retornos de chamada nas próximas etapas. 
Etapa 5: Adicionando segurança - Guarda- corpo de entrada 
com before_model_callback 
Nossa equipe de agentes está se tornando mais capaz, memorizando preferências e utilizando ferramentas de forma 
eficaz. No entanto, em cenários reais, frequentemente precisamos de mecanismos de segurança para controlar o comportamento do 
scente auton ale solicitesã. 
cialmente problemaétions 
ດ 
agente antes que solicitações potencialmente prodiematicas cheguem ao Large Language Model (LLM) principal. 
O ADK fornece Callbacks - funções que permitem que você se conecte a pontos específicos no ciclo de vida de execução do agente. Isso before_model_callback é particularmente útil para segurança de entrada. 
O que é before_model_callback? 
• É uma função Python que você define e que o ADK executa logo antes de um agente enviar sua solicitação compilada (incluindo histórico de conversas, instruções e a última mensagem do usuário) para o LLM subjacente. 
• Objetivo: inspecionar a solicitação, modificá-la se necessário ou bloqueá-la totalmente com base em regras predefinidas. 
Casos de uso comuns: 
• Validação/filtragem de entrada: verifique se a entrada do usuário atende aos critérios ou contém conteúdo não permitido (como Pll ou palavras-chave). 
· 
· 
Guardrails: evite que solicitações prejudiciais, fora do tópico 
ou que violem políticas sejam processadas pelo LLM. 
Modificação dinâmica de prompt: adicione informações 
oportunas (por exemplo, do estado da sessão) ao contexto da solicitação LLM antes do envio. 
Como funciona: 
1. Defina uma função que aceite callback_context: 
CallbackContexte 11m_request: LlmRequest. 
· 
· 
callback_context: Fornece acesso às informações do 
agente, estado da sessão (callback_context.state), etc. 
11m_request: Contém a carga útil completa destinada ao LLM (contents, config). 
2. Dentro da função: 
· 
Inspecionar: Examine 
11m_request.contents (especialmente a última mensagem do usuário). 
Modificar (Tenha cuidado): Você pode alterar partes de 
11m_request. 
• Bloqueio (Guardrail): Retorna um L1mResponse objeto. O ADK enviará esta resposta imediatamente, ignorando a chamada do LLM para aquele turno. 
• Permitir: Retornar None. O ADK prossegue chamando o 
LLM com a solicitação (potencialmente modificada). 
Nesta etapa, iremos: 
1. Defina uma before_model_callback função ( 
block_keyword_guardrail) que verifica a entrada do usuário 
para uma palavra-chave específica ("BLOCK"). 
2. Atualize nosso agente raiz com estado ( 
weather_agent_v4_stateful da Etapa 4) para usar esse 
retorno de chamada. 
3. Crie um novo executor associado a este agente atualizado, mas 
usando o mesmo serviço de sessão com estado para manter a 
continuidade do estado. 
4. Teste o guardrail enviando solicitações normais e contendo 
palavras-chave. 
1. Defina a função de retorno de chamada do Guardrail 
Esta função inspecionará a última mensagem do usuário dentro do 
11m_request conteúdo. Se encontrar "BLOCK" (sem distinção entre maiúsculas e minúsculas), ela constrói e retorna um 
LlmResponse para bloquear o fluxo; caso contrário, retorna None. 
# @title 1. Define the before_model_callback Guardrail 
# Ensure necessary imports are available 
from google.adk.agents.callback_context import CallbackCon from google.adk.models.11m_request import LlmRequest from google.adk.models.11m_response import LlmResponse from google.genai import types # For creating response con from typing import Optional 
def block_keyword_guardrail( 
) 
-> 
callback_context: CallbackContext, 11m_request: LlmReq 
Optional [LlmResponse]: 
Inspects the latest user message for 'BLOCK'. If found and returns a predefined LlmResponse. Otherwise, retur 
agent_name = callback_context.agent_name # Get the nam print (f" Callback: block_keyword_guardrail running 
# Extract the text from the latest user message in the last_user_message_text = 
if 11m_request.contents: 
# Find the most recent message with role 'user' for content in reversed (11m_request.contents): 
if content.role == 'user' and content.parts: 
# Assuming text is in the first part for s if content.parts[0].text: 
last_user_message_text = content.parts break # Found the last user message te 
print(f" Callback: Inspecting last user message: '{ 
#--- Guardrail Logic keyword_to_block = "BLOCK" 
if keyword_to_block in last_user_message_text.upper(): 
print (f" Callback: Found {keyword_to_block}'. # Optionally, set a flag in state to record the bl callback_context.state[ "guardrail_block_keyword_tr print (f" Callback: Set state 'guardrail_block_k 
# Construct and return an LlmResponse to stop the return LlmResponse( 
) 
else: 
print(" 
content-types.Content( 
) 
role="model", # Mimic a response from the parts=[types. Part (text=f"I cannot process 
# Note: You could also set an error_message fi 
# Keyword not found, allow the request to proceed print (f" Callback: Keyword not found. Allowing return None # Returning None signals ADK to contin 
block_keyword_guardrail function defined.") 
2. Atualize o agente raiz para usar o retorno de chamada 
Redefinimos o agente raiz, adicionando o 
before_model_callback parâmetro e apontando-o para nossa nova função de guardrail. Daremos a ele um novo nome de versão para 
maior clareza. 
Importante: Precisamos redefinir os subagentes ( greeting_agent, 
farewell_agent) e a ferramenta com estado ( 
get_weather_stateful) dentro deste contexto se eles ainda não 
estiverem disponíveis nas etapas anteriores, garantindo que a 
definição do agente raiz tenha acesso a todos os seus 
componentes. 
# @title 2. Update Root Agent with before_model_callback 
#--- Redefine Sub-Agents (Ensures they exist in this cont greeting_agent = None 
try: 
# Use a defined model constant 
greeting_agent = Agent ( 
) 
model=MODEL_GEMINI_2_0_FLASH, 
name="greeting_agent", # Keep original name for co instruction="You are the Greeting Agent. Your ONLY description="Handles simple greetings and hellos u tools=[say_hello], 
print (f" 
Sub-Agent {greeting_agent.name}' redefinec 
except Exception as e: 
print (f"Could not redefine Greeting agent. Check Mc 
farewell_agent = None 
try: 
# Use a defined model constant 
farewell_agent = Agent ( 
) 
model=MODEL_GEMINI_2_0_FLASH, 
name="farewell_agent", # Keep original name 
instruction="You are the Farewell Agent. Your ONLY description="Handles simple farewells and goodbyes 
tools=[say goodbye], 
print (f" 
Sub-Agent {farewell_agent.name}' redefinec 
except Exception as e: 
print (f" Could not redefine Farewell agent. Check Mc 
#--- Define the Root Agent with the Callback root_agent_model_guardrail = None runner_root_model_guardrail = None 
# Check all components before proceeding 
if greeting_agent and farewell_agent and 'get_weather_stat 
# Use a defined model constant 
root_agent_model = MODEL_GEMINI_2_0_FLASH 
root_agent_model_guardrail 
) 
else: 
= 
Agent ( 
name="weather_agent_v5_model_guardrail", # New ver 
model=root_agent_model, 
description="Main agent: Handles weather, delegate instruction="You are the main Weather Agent. Provi "Delegate simple greetings to 'greetin "Handle only weather requests, greetin 
tools=[get_weather], sub_agents=[greeting_agent, farewell_agent], # Ref output_key="last_weather_report", # Keep output_ke before_model_callback=block_keyword_guardrail # << 
print (f"✓ Root Agent '{root_agent_model_guardrail.nam 
#--- Create Runner for this Agent, Using SAME Statefu # Ensure session_service_stateful exists from Step 4 if 'session_service_stateful' in globals(): 
runner_root_model_guardrail = Runner ( 
) 
else: 
agent=root_agent_model_guardrail, 
app_name=APP_NAME, # Use consistent APP_NAME session_service-session_service_stateful # <<< 
print (f"✓ Runner created for guardrail agent '{ru 
print("X Cannot create runner. 'session_service_s 
print("X Cannot create root agent with model guardrai if not greeting_agent: print(" Greeting Agent") 
if not farewell_agent: print(" - Farewell Agent") if 'get_weather_stateful' not in globals(): print(" if 'block_keyword_guardrail' not in globals(): print(" 
3. Interaja para testar o guardrail 
Vamos testar o comportamento do guardrail. Usaremos a mesma sessão ( SESSION_ID_STATEFUL) da Etapa 4 para mostrar que o estado persiste durante essas mudanças. 
1. Envie uma solicitação de clima normal (deve passar pelo 
guardrail e ser executada). 
2. Envie uma solicitação contendo "BLOCK" (deve ser 
interceptada pelo retorno de chamada). 
3. Enviar uma saudação (deve passar pelo guardrail do agente 
raiz, ser delegada e executar normalmente). 
# @title 3. Interact to Test the Model Input Guardrail import asyncio # Ensure asyncio is imported 
# Ensure the runner for the guardrail agent is available if 'runner_root_model_guardrail' in globals() and runner_r # Define the main async function for the guardrail tes # The 'await' keywords INSIDE this function are necess async def run_guardrail_test_conversation(): 
print("\n--- Testing Model Input Guardrail ---") 
# Use the runner for the agent with the callback a # Define a helper lambda for cleaner interaction c interaction_func = lambda query: call_agent_async( 
B 
r 
U 
# 
S ) 
# 1. Normal request (Callback allows, should use F print("-- Turn 1: Requesting weather in London (e await interaction_func("What is the weather in Lon 
# 2. Request containing the blocked keyword (Callb print("\n--- Turn 2: Requesting with blocked keywo await interaction_func("BLOCK the request for weat 
# 3. Normal greeting (Callback allows root agent, print("\n--- Turn 3: Sending a greeting (expect al await interaction_func("Hello again") 
Execute the run_guardrail_test_conversation` as # Choose ONE of the methods below based on your enviro 
# METHOD 1: Direct await (Default for Notebooks/Async # If your environment supports top-level await (like C # it means an event loop is already running, so you ca print("Attempting execution using 'await' (default for await run_guardrail_test_conversation() 
# METHOD 2: asyncio.run (For Standard Python Scripts [ # If running this code as a standard Python script fro # the script context is synchronous. `asyncio.run()` i 
# create and manage an event loop to execute your asyn #To use this method: 
# 1. Comment out the await run_guardrail_test_convers # 2. Uncomment the following block: 
import asyncio 
if __name__ == "__main__": # Ensures this runs only wh print("Executing using 'asyncio.run()' (for standa 
try: 
# This creates an event loop, runs your async asyncio.run(run_guardrail_test_conversation()) 
except Exception as e: 
print (f"An error occurred: {e}") 
# 
Inspect final session state after the conversati 
# This block runs after either execution method comple 
# Optional: Check state for the trigger flag set by th print("\n--- Inspecting Final Session State (After Gua 
# Use the session service instance associated with thi final_session= await session_service_stateful.get_ses 
U 
S 
else: 
if final_session: 
# Use .get() for safer access 
print (f"Guardrail Triggered Flag: {final_session.s print (f"Last Weather Report: (final_session.state. print (f" Temperature Unit: {final_session.state.get # print(f"Full State Dict: {final_session.state}") else: 
print("\nX Error: Could not retrieve final sessic 
print("\n! Skipping model guardrail test. Runner ('ru 
Observe o fluxo de execução: 
1. Clima de Londres: O retorno de chamada é executado para 
weather_agent_v5_model_guardrail, inspeciona a mensagem, imprime "Palavra-chave não encontrada. Permitindo chamada LLM." e retorna None. O agente prossegue, chama a 
not weather stateful forramenta (avo ves a proforância 
yel_weather_state canca luc usa a piciciccia 
"Fahrenheit" da alteração de estado da Etapa 4) e retorna a previsão do tempo. Esta resposta é atualizada 
last_weather_report via output_key. 
2. Solicitação BLOCK: O retorno de chamada é executado 
novamente para weather_agent_v5_model_guardrail, inspeciona a mensagem, encontra "BLOCK", exibe "Chamada LLM bloqueando!", define o sinalizador de estado e retorna o predefinido L1mResponse. O LLM subjacente do agente nunca é chamado neste turno. O usuário vê a mensagem de bloqueio do retorno de chamada. 
3. Olá Novamente: O retorno de chamada é executado para 
weather_agent_v5_model_guardrail, permite a solicitação. O agente raiz então delega para greeting_agent. Observação: O 
before_model_callback definido no agente raiz NÃO se aplica automaticamente aos subagentes. O 
greeting agent prossegue normalmente, chama sua say_hello ferramenta e retorna a saudação. 
Você implementou com sucesso uma camada de segurança de 
entrada! Ela before_model_callback fornece um mecanismo poderoso para impor regras e controlar o comportamento do agente antes que chamadas de LLM caras ou potencialmente arriscadas sejam feitas. Em seguida, aplicaremos um conceito semelhante para adicionar proteções ao próprio uso da ferramenta. 
Etapa 6: Adicionando Segurança - Argumento da Ferramenta Guardrail ( 
before_tool_callback) 
Na Etapa 5, adicionamos uma proteção para inspecionar e potencialmente bloquear a entrada do usuário antes que ela chegue ao LLM. Agora, adicionaremos outra camada de controle depois que o LLM decidir usar uma ferramenta, mas antes que ela seja efetivamente executada. Isso é útil para validar os argumentos que o LLM deseja passar para a ferramenta. 
O ADK fornece isso before_tool_callback exatamente para esse propósito. 
O que é before_tool_callback? 
• É uma função Python executada logo antes de uma função de ferramenta específica ser executada, depois que o LLM solicita seu uso e decide os argumentos. 
· 
Objetivo: validar argumentos de ferramentas, impedir a execução de ferramentas com base em entradas específicas, modificar argumentos dinamicamente ou impor políticas de uso de recursos. 
Casos de uso comuns: 
• Validação de argumentos: verifique se os argumentos fornecidos pelo LLM são válidos, estão dentro dos intervalos 
permitidos ou estão em conformidade com os formatos 
esperados. 
· 
Proteção de recursos: evite que ferramentas sejam chamadas com entradas que podem ser caras, acessar dados restritos ou causar efeitos colaterais indesejados (por exemplo, bloquear 
chamadas de API para determinados parâmetros). 
Modificação dinâmica de argumentos: ajuste os argumentos 
com base no estado da sessão ou outras informações contextuais antes da execução da ferramenta. 
Como funciona: 
1. Defina uma função que aceite tool: BaseTool, args: 
Dict(str, Any], e tool_context: ToolContext. 
⚫ tool: O objeto de ferramenta prestes a ser chamado 
(inspecionar tool.name). 
⚫ args: O dicionário de argumentos que o LLM gerou para a 
ferramenta. 
• 
tool_context: Fornece acesso ao estado da sessão ( tool_context.state), informações do agente, etc. 
2. Dentro da função: 
• 
Inspecionar: Examine o tool. name e o args dicionário. 
• Modificar: Altera valores diretamente no args dicionário. Se você retornar, a ferramenta será executada com esses argumentos modificados. None 
• 
· 
Bloqueio/Substituição (Guardrail): Retorna um dicionário 
. O ADK trata este dicionário como o resultado da chamada 
da ferramenta, ignorando completamente a execução da função original da ferramenta. O dicionário deve, idealmente, corresponder ao formato de retorno esperado da ferramenta que está bloqueando. 
Permitir: Retornar None. O ADK prossegue para executar 
a função da ferramenta real com os argumentos (potencialmente modificados). 
Nesta etapa, iremos: 
1. Defina uma before_tool_callback função ( 
block_paris_tool_guardrail) que verifica especificamente se 
a get_weather_stateful ferramenta é chamada com a cidade 
"Paris". 
2. Se "Paris" for detectado, o retorno de chamada bloqueará a 
ferramenta e retornará um dicionário de erros personalizado. 
3. Atualize nosso agente raiz ( 
weather_agent_v6_tool_guardrail) para incluir o e 
before_model_callback este novo before_tool_callback. 
4. Crie um novo executor para este agente, usando o mesmo 
serviço de sessão com estado. 
5. Teste o fluxo solicitando informações meteorológicas para as 
cidades permitidas e para a cidade bloqueada ("Paris"). 
1. Defina a função de retorno de chamada do Guardrail da 
ferramenta 
Esta função tem como alvo a get_weather_stateful ferramenta. Ela verifica o city argumento. Se for "Paris", retorna um dicionário de erros que se parece com a resposta de erro da própria ferramenta. Caso contrário, permite que a ferramenta seja executada retornando None. 
# @title 1. Define the before_tool_callback Guardrail 
# Ensure necessary imports are available 
from google.adk.tools.base_tool import BaseTool from google.adk.tools.tool_context import ToolContext from typing import Optional, Dict, Any # For type hints 
def block_paris_tool_guardrail( 
tool: BaseTool, args: Dict[str, Any], tool_context: To ) -> Optional[Dict]: 
Checks if 'get_weather_stateful' is called for 'Paris' If so, blocks the tool execution and returns a specifi Otherwise, allows the tool call to proceed by returnin 
tool_name 
tool.name 
agent_name = tool_context.agent_name # Agent attemptin print(f" --- Callback: block paris tool quardrail runni 
B 
print("--- Callback: Inspecting args: (args} ---") 
# 
Guardrail Logic 
target_tool_name = "get_weather_stateful" # Match the blocked_city = "paris" 
# Check if it's the correct tool and the city argument if tool_name == target_tool_name: 
city_argument = args.get("city", "") # Safely get if city_argument and city_argument.lower() == bloc print (f" Callback: Detected blocked city '{ # Optionally update state tool_context.state [ "guardrail_tool_block_trigg print (f" Callback: Set state 'guardrail_toc 
# Return a dictionary matching the tool's expe # This dictionary becomes the tool's result, s return { 
} 
else: 
else: 
"status": "error", 
"error_message": f"Policy restriction: Wea 
print(f" Callback: City '{city_argument}' 
print (f" Callback: Tool '{tool_name}' is not th 
# If the checks above didn't return a dictionary, allo print (f" Callback: Allowing tool '{tool_name}' to p return None # Returning None allows the actual tool fu 
print("✓ block_paris_tool_guardrail function defined.") 
2. Atualize o agente raiz para usar ambos os retornos de 
chamada 
Redefinimos o agente raiz novamente ( 
weather_agent_v6_tool_guardrail), desta vez adicionando o 
before_tool_callback parâmetro junto com o 
before_model_callback da Etapa 5. 
Nota de execução autocontida: semelhante à Etapa 5, certifique-se 
de que todos os pré-requisitos (subagentes, ferramentas 
before_model_callback) estejam definidos ou disponíveis no contexto de execução antes de definir este agente. 
# @title 2. Update Root Agent with BOTH Callbacks (Self-Co 
# 
--- 
Ensure Prerequisites are Defined 
# (Include or ensure execution of definitions for: Agent, 
# MODEL constants, say_hello, say goodbye, greeting_agent # get_weather_stateful, block_keyword_guardrail, block_pa 
#--- Redefine Sub-Agents (Ensures they exist in this cont greeting_agent = None 
try: 
# Use a defined model constant greeting_agent 
) 
= 
Agent ( 
model=MODEL_GEMINI_2_0_FLASH, 
name="greeting_agent", # Keep original name for co instruction="You are the Greeting Agent. Your ONLY description="Handles simple greetings and hellos u tools=[say_hello], 
print (f"✓ Sub-Agent {greeting_agent.name}' redefinec except Exception as e: 
print(f" Could not redefine Greeting agent. Check Mc 
farewell_agent = None 
try: 
# Use a defined model constant 
farewell_agent 
= 
Agent( 
) 
model=MODEL_GEMINI_2_0_FLASH, 
name="farewell_agent", # Keep original name 
instruction="You are the Farewell Agent. Your ONLY description="Handles simple farewells and goodbyes 
tools=[say goodbye], 
print (f" 
Sub-Agent {farewell_agent.name}' redefinec 
except Exception as e: 
print(f"X Could not redefine Farewell agent. Check Mc 
ດ 
#--- Define the Root Agent with Both Callbacks 
root_agent_tool_guardrail = None 
runner_root_tool_guardrail = None 
if ('greeting_agent' in globals() and greeting_agent and 'farewell_agent' in globals() and farewell_agent and 'get_weather_stateful' in globals() and 'block_keyword_guardrail' in globals() and 'block_paris_tool_guardrail' in globals()): 
root_agent_model = MODEL_GEMINI_2_0_FLASH 
root_agent_tool_guardrail = Agent ( 
) 
name="weather_agent_v6_tool_guardrail", # New vers 
model=root_agent_model, 
description="Main agent: Handles weather, delegate instruction="You are the main Weather Agent. Provi "Delegate greetings to 'greeting_agent "Handle only weather, greetings, and f 
tools=[get_weather_stateful], 
sub_agents=[greeting_agent, farewell_agent], output_key="last_weather_report", 
before_model_callback=block_keyword_guardrail, # K before_tool_callback-block_paris_tool_guardrail # 
print (f" Root Agent {root_agent_tool_guardrail.name 
#--- Create Runner, Using SAME Stateful Session Servi if 'session_service_stateful' in globals(): 
else: 
runner_root_tool_guardrail = Runner ( 
) 
else: 
agent=root_agent_tool_guardrail, 
app_name=APP_NAME, 
session_service-session_service_stateful # <<< 
print (f"✓ Runner created for tool guardrail agent 
print("X Cannot create runner. 'session_service_s 
print("X Cannot create root agent with tool guardrail 
3. Interaja para testar o guarda-corpo da ferramenta 
Vamos testar o fluxo de interação, novamente usando a mesma sessão com estado ( SESSION_ID_STATEFUL) das etapas anteriores. 
1. Solicitar previsão do tempo para "Nova York": Passa ambos os 
retornos de chamada, a ferramenta executa (usando a preferência Fahrenheit do estado). 
2. Solicitação de previsão do tempo para "Paris": Passa 
before_model_callback. O LLM decide chamar 
get_weather_stateful (city= 'Paris'). 
before_tool_callback Intercepta, bloqueia a ferramenta e retorna o dicionário de erros. O agente retransmite esse erro. 
3. Solicitação de previsão do tempo para "Londres": Passa ambos 
os retornos de chamada, a ferramenta é executada 
normalmente. 
# @title 3. Interact to Test the Tool Argument Guardrail import asyncio # Ensure asyncio is imported 
# Ensure the runner for the tool guardrail agent is availa if 'runner_root_tool_guardrail' in globals() and runner_rc # Define the main async function for the tool guardrai # The 'await' keywords INSIDE this function are necess async def run_tool_guardrail_test(): 
print("\n--- Testing Tool Argument Guardrail ('Par 
# Use the runner for the agent with both callbacks # Define a helper lambda for cleaner interaction c interaction_func = lambda query: call_agent_async( 
r 
U 
S 
) 
# 1. Allowed city (Should pass both callbacks, use print("--- Turn 1: Requesting weather in New York await interaction_func("What's the weather in New 
# 2. Blocked city (Should pass model callback, but 
print("\n--- Turn 2: Requesting weather in Paris ( await interaction_func("How about Paris?") # Tool 
# 3. Another allowed city (Should work normally ag print("\n--- Turn 3: Requesting weather in London await interaction_func("Tell me the weather in Lon 
#--- Execute the run_tool_guardrail_test` async func # Choose ONE of the methods below based on your enviro 
# METHOD 1: Direct await (Default for Notebooks/Async # If your environment supports top-level await (like C # it means an event loop is already running, so you ca print("Attempting execution using 'await' (default for await run_tool_guardrail_test() 
# METHOD 2: asyncio.run (For Standard Python Scripts [ # If running this code as a standard Python script fro # the script context is synchronous. asyncio.run()` i # create and manage an event loop to execute your asyn # To use this method: 
#1. Comment out the await run_tool_guardrail_test() # 2. Uncomment the following block: 
import asyncio 
if __name__ == "__main__": # Ensures this runs only wh print("Executing using asyncio.run()' (for standa 
try: 
# This creates an event loop, runs your async asyncio.run(run_tool_guardrail_test()) 
except Exception as e: 
print (f" An error occurred: {e}") 
# 
Inspect final session state after the conversati 
# This block runs after either execution method comple # Optional: Check state for the tool block trigger fla print("\n--- Inspecting Final Session State (After Toc # Use the session service instance associated with thi final_session = await session_service_stateful.get_ses 
B 
U 
S 
if final_session: 
# Use .get() for safer access 
print (f" Tool Guardrail Triggered Flag: {final_sess print (f"Last Weather Report: (final_session.state. print (f"Temperature Unit: {final_session.state.get # print(f "Full State Dict: {final_session.state}") else: 
print("\nX Error: Could not retrieve final sessic 
else: 
print("\n! Skipping tool guardrail test. Runner ('rur 
Analisar a saída: 
1. Nova York: O before_model_callback permite a solicitação. O 
LLM solicita get_weather_stateful.O 
before_tool_callback executa, inspeciona os argumentos ( {'city': 'New York' }), verifica se não é "Paris", imprime "Permitindo ferramenta..." e retorna None. A função real 
get_weather_stateful é executada, lê "Fahrenheit" do estado e retorna o relatório meteorológico. O agente retransmite isso, e ele é salvo via output_key. 
2. Paris: O before_model_callback permite a solicitação. O LLM 
solicita get_weather_stateful (city='Paris').O 
before_tool_callback executa, inspeciona os argumentos, detecta "Paris", exibe "Execução da ferramenta bloqueando!", 
define o sinalizador de estado e retorna o dicionário de erros 
{'status': 'error', 'error_message': 'Policy restriction...}. A get_weather_stateful função em si nunca é executada. O agente recebe o dicionário de erros como se fosse a saída da ferramenta e formula uma resposta com base nessa mensagem de erro. 
3. Londres: Comporta-se como Nova York, passando ambos os 
retornos de chamada e executando a ferramenta com sucesso. 
O novo relatório meteorológico de Londres substitui o 
leet 
- do octado 
Last_weather_repofu estauu. 
Agora você adicionou uma camada de segurança crucial que controla não apenas o que chega ao LLM, mas também como as 
ferramentas do agente podem ser usadas com base nos argumentos específicos gerados pelo LLM. Callbacks como 
before_model_callback e before_tool_callback são essenciais 
para a construção de aplicativos de agente robustos, seguros e em conformidade com as políticas. 
Conclusão: sua equipe de agentes está pronta! 
Parabéns! Você evoluiu com sucesso da criação de um único agente meteorológico básico para a construção de uma equipe sofisticada com vários agentes usando o Kit de Desenvolvimento de Agentes (ADK). 
Vamos recapitular o que você realizou: 
• Você começou com um agente fundamental equipado com uma única ferramenta ( get_weather). 
· 
Você explorou a flexibilidade de vários modelos do ADK usando o LiteLLM, executando a mesma lógica central com diferentes LLMs, como Gemini, GPT-40 e Claude. 
Você adotou a modularidade criando subagentes especializados ( greeting_agent, farewell_agent) e habilitando a delegação automática de um agente raiz. 
• Você deu memória aos seus agentes usando o Estado da Sessão, permitindo que eles se lembrassem das preferências do usuário ( temperature_unit) e das interações anteriores ( output_key). 
• Você implementou proteções de segurança cruciais usando 
ambos before_model_callback (bloqueando palavras-chave de entrada específicas) e before_tool_callback (bloqueando a execução da ferramenta com base em argumentos como a cidade "Paris"). 
Ao construir esta equipe progressiva do Weather Bot, você adquiriu experiência prática com os principais conceitos do ADK essenciais para o desenvolvimento de aplicativos complexos e inteligentes. 
Principais conclusões: 
• Agentes e Ferramentas: Os blocos de construção 
· 
fundamentais para definir capacidades e raciocínio. Instruções 
e docstrings claras são essenciais. 
Runners & Session Services: O mecanismo e o sistema de 
gerenciamento de memória que orquestram a execução do 
agente e mantêm o contexto da conversação. 
· 
Delegação: Projetar equipes multiagentes permite 
especialização, modularidade e melhor gerenciamento de 
tarefas complexas. O agente description é essencial para o 
fluxo automático. 
B 
