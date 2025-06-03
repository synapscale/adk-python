# filepath: /workspaces/adk-python/contributing/samples/weather_bot_tutorial/step_1_basic_weather_agent.py
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

"""
Weather Bot Tutorial - Step 1: Basic Weather Agent
=================================================

This step demonstrates:
- Creating a basic weather agent with a single tool
- Setting up Session Service and Runner
- Basic agent interaction patterns
"""

import asyncio
import os
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

# Configure environment for ADK
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"


def get_weather(city: str) -> dict:
  """Retrieves weather report for a specified city.

  Args:
    city (str): The name of the city (e.g., "New York", "London").

  Returns:
    dict: A dictionary containing the weather information.
  """
  print(f"--- Tool: get_weather called for city: {city} ---")

  city_normalized = city.lower().replace(" ", "")

  # Mock weather data
  mock_weather_db = {
    "newyork": {
      "status": "success",
      "report": ("The weather in New York is sunny with a "
                 "temperature of 25°C (77°F).")
    },
    "london": {
      "status": "success",
      "report": ("It's cloudy in London with a temperature "
                 "of 15°C (59°F).")
    },
    "tokyo": {
      "status": "success",
      "report": ("Tokyo is experiencing light rain with a "
                 "temperature of 18°C (64°F).")
    }
  }

  if city_normalized in mock_weather_db:
    return mock_weather_db[city_normalized]
  else:
    return {
      "status": "error",
      "error_message": (f"Sorry, I don't have weather information "
                        f"for '{city}' at the moment.")
    }


# Define the Weather Agent
weather_agent = Agent(
  name="weather_agent_v1",
  model=MODEL_GEMINI_2_0_FLASH,
  description="Provides weather information for specific cities",
  instruction=(
    "You are a helpful weather assistant. "
    "When the user asks for the weather in a specific city, "
    "use the 'get_weather' tool to find the information. "
    "If the tool returns an error, inform the user politely. "
    "If the tool is successful, present the weather clearly."
  ),
  tools=[get_weather],
)

print(f"✓ Agent '{weather_agent.name}' created using model "
      f"{MODEL_GEMINI_2_0_FLASH}")


async def setup_session_and_runner():
  """Setup session service and runner for the weather agent."""
  session_service = InMemorySessionService()
  print("✓ InMemorySessionService created")

  app_name = "weather_tutorial_app"
  user_id = "user_1"
  session_id = "session_001"

  await session_service.create_session(
    app_name=app_name,
    user_id=user_id,
    session_id=session_id
  )

  print(f"✓ Session created: App='{app_name}', User='{user_id}', "
        f"Session='{session_id}'")

  runner = Runner(
    agent=weather_agent,
    session_service=session_service,
    app_name=app_name,
  )
  print(f"✓ Runner created for agent '{runner.agent.name}'")

  return runner, user_id, session_id


async def call_agent_async(query, runner, user_id, session_id):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User Query: {query}")

  content = types.Content(
    role="user",
    parts=[types.Part(text=query)]
  )

  final_response_text = "Agent did not produce a final response"

  async for event in runner.run_async(
    content=content,
    user_id=user_id,
    session_id=session_id,
  ):
    if event.is_final_response():
      if event.content and event.content.parts:
        final_response_text = event.content.parts[0].text
      elif event.actions and event.actions.escalate:
        final_response_text = (f"Agent escalated: "
                               f"{event.actions.escalate}")
      break

  print(f"<<< Agent Response: {final_response_text}")
  return final_response_text


async def run_conversation():
  """Run the initial conversation with the weather agent."""
  print("\n=== Weather Bot Tutorial - Step 1: Basic Weather Agent ===")

  runner, user_id, session_id = await setup_session_and_runner()

  await call_agent_async(
    "What is the weather like in London?",
    runner=runner,
    user_id=user_id,
    session_id=session_id,
  )

  await call_agent_async(
    "How about Paris?",
    runner=runner,
    user_id=user_id,
    session_id=session_id,
  )

  await call_agent_async(
    "Tell me the weather in New York",
    runner=runner,
    user_id=user_id,
    session_id=session_id,
  )

  await call_agent_async(
    "What about Tokyo?",
    runner=runner,
    user_id=user_id,
    session_id=session_id,
  )


def test_tool():
  """Test the get_weather tool directly."""
  print("\n=== Testing get_weather tool directly ===")
  print(get_weather("New York"))
  print(get_weather("Paris"))
  print(get_weather("London"))


if __name__ == "__main__":
  test_tool()

  try:
    asyncio.run(run_conversation())
  except KeyboardInterrupt:
    print("\nConversation interrupted by user.")
  except Exception as e:  # pylint: disable=broad-except
    print(f"An error occurred: {e}")
