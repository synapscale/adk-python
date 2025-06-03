"""
Weather Bot Tutorial - Step 3: Multi-Agent System with Delegation

This step demonstrates how to create a multi-agent system where a main agent
can delegate specific tasks to specialized sub-agents, showcasing ADK's
agent orchestration capabilities.

Features demonstrated:
- Multiple specialized agents (greeting, weather, farewell)
- Agent delegation through sub_agents configuration
- Tool distribution across different agents
- Coordinated multi-agent interactions
- Automatic agent selection based on user intent

Prerequisites:
- Basic understanding of ADK agents from Steps 1-2
"""

import asyncio
from typing import Dict, Any
import logging

# ADK Core imports
from google.adk.core import Agent
from google.adk.models import Gemini
from google.adk.core.runners import Runner
from google.adk.core.sessions import InMemorySessionService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Model configuration
MODEL_GEMINI_2_0_FLASH = Gemini(model="gemini-2.0-flash-exp")

# Application configuration
APP_NAME = "weather_bot_tutorial_step3"
SESSION_ID_MULTI_AGENT = "multi_agent_demo_session"

# Weather tool (reused from previous steps)
def get_weather(city: str) -> Dict[str, Any]:
    """
    Get current weather information for a specified city.
    
    Args:
        city: The name of the city to get weather for
        
    Returns:
        Dictionary containing weather information
    """
    weather_data = {
        "new york": {
            "temperature": "22°C (72°F)",
            "condition": "Partly cloudy",
            "humidity": "65%",
            "wind_speed": "12 km/h",
            "location": "New York, NY"
        },
        "london": {
            "temperature": "15°C (59°F)", 
            "condition": "Light rain",
            "humidity": "78%",
            "wind_speed": "8 km/h",
            "location": "London, UK"
        },
        "tokyo": {
            "temperature": "26°C (79°F)",
            "condition": "Sunny",
            "humidity": "60%", 
            "wind_speed": "6 km/h",
            "location": "Tokyo, Japan"
        },
        "paris": {
            "temperature": "18°C (64°F)",
            "condition": "Overcast",
            "humidity": "72%",
            "wind_speed": "10 km/h",
            "location": "Paris, France"
        }
    }
    
    city_lower = city.lower()
    if city_lower in weather_data:
        return {
            "status": "success",
            "city": weather_data[city_lower]["location"],
            "temperature": weather_data[city_lower]["temperature"],
            "condition": weather_data[city_lower]["condition"],
            "humidity": weather_data[city_lower]["humidity"],
            "wind_speed": weather_data[city_lower]["wind_speed"]
        }
    else:
        available_cities = ", ".join([data["location"] for data in weather_data.values()])
        return {
            "status": "error",
            "error_message": f"Weather data not available for {city}. Available cities: {available_cities}"
        }

# New tools for greeting and farewell agents
def say_hello(name: str = "there") -> str:
    """
    Provide a friendly greeting to the user.
    
    Args:
        name: The name of the person to greet (optional, defaults to "there")
        
    Returns:
        A personalized greeting message
    """
    logger.info(f"Greeting tool called for: {name}")
    return f"Hello {name}! Welcome to the Weather Bot service. I'm here to help you with weather information and more!"

def say_goodbye(name: str = "there") -> str:
    """
    Provide a friendly farewell to the user.
    
    Args:
        name: The name of the person to say goodbye to (optional, defaults to "there")
        
    Returns:
        A personalized farewell message
    """
    logger.info(f"Farewell tool called for: {name}")
    return f"Goodbye {name}! Thank you for using Weather Bot. Have a wonderful day and stay safe!"

def create_greeting_agent() -> Agent:
    """
    Create a specialized agent for handling greetings and introductions.
    
    Returns:
        Configured greeting agent
    """
    return Agent(
        name="greeting_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a friendly greeting specialist. Your job is to welcome users warmly "
            "and make them feel comfortable. Use the say_hello tool to provide personalized "
            "greetings. Be enthusiastic and helpful in setting a positive tone for the interaction."
        ),
        tools=[say_hello]
    )

def create_farewell_agent() -> Agent:
    """
    Create a specialized agent for handling farewells and goodbyes.
    
    Returns:
        Configured farewell agent
    """
    return Agent(
        name="farewell_agent", 
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a friendly farewell specialist. Your job is to provide warm goodbyes "
            "and ensure users feel appreciated. Use the say_goodbye tool to provide personalized "
            "farewells. Be gracious and leave users with a positive final impression."
        ),
        tools=[say_goodbye]
    )

def create_weather_agent() -> Agent:
    """
    Create a specialized agent for weather information (same as previous steps).
    
    Returns:
        Configured weather agent
    """
    return Agent(
        name="weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a weather information specialist. Use the get_weather tool to provide "
            "accurate and helpful weather information for cities. Be informative and clear "
            "in your responses."
        ),
        tools=[get_weather]
    )

def create_main_agent() -> Agent:
    """
    Create the main coordination agent that delegates to specialized sub-agents.
    
    Returns:
        Configured main agent with sub-agent delegation
    """
    # Create sub-agents
    greeting_agent = create_greeting_agent()
    weather_agent = create_weather_agent()
    farewell_agent = create_farewell_agent()
    
    # Create main coordinating agent
    return Agent(
        name="main_weather_bot",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are the main coordinator for a weather service bot. You have access to "
            "specialized agents that can help with different types of requests:\n"
            "- For greetings and welcome messages, delegate to the greeting_agent\n"
            "- For weather information requests, delegate to the weather_agent\n"
            "- For farewells and goodbye messages, delegate to the farewell_agent\n\n"
            "Analyze the user's intent and delegate to the appropriate specialist agent. "
            "You can also handle general conversation and coordinate between agents as needed."
        ),
        sub_agents=[greeting_agent, weather_agent, farewell_agent]
    )

async def test_greeting_flow():
    """
    Test the greeting functionality through the multi-agent system.
    """
    print("--- Testing Greeting Flow ---")
    
    session_service = InMemorySessionService()
    main_agent = create_main_agent()
    
    runner = Runner(
        agent=main_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    test_cases = [
        "Hello there! I'm Alice.",
        "Hi! Can you welcome me to your service?",
        "Good morning! I'm new here."
    ]
    
    for i, query in enumerate(test_cases):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_MULTI_AGENT}_greeting_{i}",
                user_message=query
            )
            print(f"User: {query}")
            print(f"Bot: {result.response}")
            print()
        except Exception as e:
            print(f"❌ Error in greeting test: {str(e)}\n")

async def test_weather_flow():
    """
    Test the weather functionality through the multi-agent system.
    """
    print("--- Testing Weather Flow ---")
    
    session_service = InMemorySessionService()
    main_agent = create_main_agent()
    
    runner = Runner(
        agent=main_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    test_cases = [
        "What's the weather like in Tokyo?",
        "Can you check the weather in London for me?",
        "I need weather information for New York"
    ]
    
    for i, query in enumerate(test_cases):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_MULTI_AGENT}_weather_{i}",
                user_message=query
            )
            print(f"User: {query}")
            print(f"Bot: {result.response}")
            print()
        except Exception as e:
            print(f"❌ Error in weather test: {str(e)}\n")

async def test_farewell_flow():
    """
    Test the farewell functionality through the multi-agent system.
    """
    print("--- Testing Farewell Flow ---")
    
    session_service = InMemorySessionService()
    main_agent = create_main_agent()
    
    runner = Runner(
        agent=main_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    test_cases = [
        "Goodbye! Thanks for your help.",
        "I need to go now. Can you say goodbye to Bob?",
        "Farewell! This was very helpful."
    ]
    
    for i, query in enumerate(test_cases):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_MULTI_AGENT}_farewell_{i}",
                user_message=query
            )
            print(f"User: {query}")
            print(f"Bot: {result.response}")
            print()
        except Exception as e:
            print(f"❌ Error in farewell test: {str(e)}\n")

async def test_full_conversation():
    """
    Test a complete conversation that exercises all agent types.
    """
    print("--- Testing Full Conversation Flow ---")
    
    session_service = InMemorySessionService()
    main_agent = create_main_agent()
    
    runner = Runner(
        agent=main_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Complete conversation flow
    conversation_steps = [
        "Hello! I'm Sarah and I'm planning a trip.",
        "Can you tell me the weather in Paris?",
        "What about Tokyo?", 
        "Great! Thanks for all the help. Goodbye!"
    ]
    
    session_id = f"{SESSION_ID_MULTI_AGENT}_full_conversation"
    
    print("=== Complete Conversation ===")
    for step in conversation_steps:
        try:
            result = await runner.run_async(
                session_id=session_id,
                user_message=step
            )
            print(f"User: {step}")
            print(f"Bot: {result.response}")
            print()
        except Exception as e:
            print(f"❌ Error in conversation step: {str(e)}\n")

async def test_individual_agents():
    """
    Test each sub-agent individually to verify they work correctly.
    """
    print("--- Testing Individual Agents ---")
    
    session_service = InMemorySessionService()
    
    # Test greeting agent directly
    print("Testing Greeting Agent:")
    greeting_agent = create_greeting_agent()
    greeting_runner = Runner(
        agent=greeting_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    try:
        result = await greeting_runner.run_async(
            session_id="test_greeting_individual",
            user_message="Please greet me! My name is Alex."
        )
        print(f"Greeting Agent Response: {result.response}\n")
    except Exception as e:
        print(f"❌ Greeting Agent Error: {str(e)}\n")
    
    # Test weather agent directly
    print("Testing Weather Agent:")
    weather_agent = create_weather_agent()
    weather_runner = Runner(
        agent=weather_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    try:
        result = await weather_runner.run_async(
            session_id="test_weather_individual",
            user_message="What's the weather in London?"
        )
        print(f"Weather Agent Response: {result.response}\n")
    except Exception as e:
        print(f"❌ Weather Agent Error: {str(e)}\n")
    
    # Test farewell agent directly
    print("Testing Farewell Agent:")
    farewell_agent = create_farewell_agent()
    farewell_runner = Runner(
        agent=farewell_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    try:
        result = await farewell_runner.run_async(
            session_id="test_farewell_individual",
            user_message="Please say goodbye to me! My name is Alex."
        )
        print(f"Farewell Agent Response: {result.response}\n")
    except Exception as e:
        print(f"❌ Farewell Agent Error: {str(e)}\n")

async def main():
    """
    Main function to run all multi-agent demonstrations.
    """
    print("🤖 Weather Bot Tutorial - Step 3: Multi-Agent System with Delegation\n")
    print("This step demonstrates how to create specialized agents and coordinate them")
    print("through a main agent that delegates tasks based on user intent.\n")
    
    # Test individual agents first
    await test_individual_agents()
    
    print("=" * 60)
    
    # Test different flows through the main coordinating agent
    await test_greeting_flow()
    
    print("=" * 60)
    
    await test_weather_flow()
    
    print("=" * 60)
    
    await test_farewell_flow()
    
    print("=" * 60)
    
    # Test a complete conversation
    await test_full_conversation()
    
    print("=" * 60)
    print("✅ Step 3 Complete!")
    print("\nKey Learnings:")
    print("• ADK supports multi-agent systems through sub_agents configuration")
    print("• Specialized agents can handle specific types of tasks")
    print("• Main agent coordinates and delegates to appropriate sub-agents") 
    print("• Agent delegation enables modular and maintainable bot architectures")
    print("• Each agent can have its own tools and instructions")

if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(main())
