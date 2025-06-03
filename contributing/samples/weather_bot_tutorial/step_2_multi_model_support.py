"""
Weather Bot Tutorial - Step 2: Multi-Model Support with LiteLLM

This step demonstrates how to use multiple language models with the same agent configuration,
showcasing the flexibility of ADK's model abstraction through LiteLLM integration.

Features demonstrated:
- LiteLLM integration with OpenAI GPT-4
- LiteLLM integration with Anthropic Claude
- Model comparison and flexibility
- Same agent logic with different underlying models

Prerequisites:
- Valid OpenAI API key (set as OPENAI_API_KEY environment variable)
- Valid Anthropic API key (set as ANTHROPIC_API_KEY environment variable)
"""

import asyncio
from typing import Dict, Any
import os

# ADK Core imports
from google.adk.core import Agent
from google.adk.models import Gemini, LiteLlm
from google.adk.core.runners import Runner
from google.adk.core.sessions import InMemorySessionService

# Reuse the weather tool from Step 1
def get_weather(city: str) -> Dict[str, Any]:
    """
    Get current weather information for a specified city.
    
    Args:
        city: The name of the city to get weather for
        
    Returns:
        Dictionary containing weather information including temperature,
        condition, humidity, and wind speed
    """
    # Mock weather database with realistic data
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
        return {
            "status": "error",
            "error_message": f"Weather data not available for {city}. Available cities: New York, London, Tokyo"
        }

# Model configurations
MODEL_GEMINI_2_0_FLASH = Gemini(model="gemini-2.0-flash-exp")
MODEL_GPT_4O = LiteLlm(model="openai/gpt-4o")
MODEL_CLAUDE_3_SONNET = LiteLlm(model="anthropic/claude-3-sonnet-20240229")

# Application configuration
APP_NAME = "weather_bot_tutorial_step2"
SESSION_ID_MULTI_MODEL = "multi_model_demo_session"

def create_weather_agent(model, agent_name: str) -> Agent:
    """
    Create a weather agent with the specified model.
    
    Args:
        model: The model instance to use (Gemini, LiteLLM, etc.)
        agent_name: Name for the agent instance
        
    Returns:
        Configured Agent instance
    """
    return Agent(
        name=agent_name,
        model=model,
        instruction=(
            "You are a helpful weather assistant. Use the get_weather tool to provide "
            "accurate weather information for cities. Always be polite and informative."
        ),
        tools=[get_weather]
    )

async def test_model_comparison():
    """
    Test the same weather request across different models to demonstrate flexibility.
    """
    print("=== Weather Bot Tutorial - Step 2: Multi-Model Support ===\n")
    
    # Create session service
    session_service = InMemorySessionService()
    
    # Define models to test
    models_to_test = [
        (MODEL_GEMINI_2_0_FLASH, "weather_agent_gemini"),
        (MODEL_GPT_4O, "weather_agent_gpt4"),
        (MODEL_CLAUDE_3_SONNET, "weather_agent_claude")
    ]
    
    # Test query
    test_query = "What's the weather like in Tokyo?"
    
    for model, agent_name in models_to_test:
        try:
            print(f"--- Testing with {agent_name} ---")
            
            # Create agent with specific model
            agent = create_weather_agent(model, agent_name)
            
            # Create runner
            runner = Runner(
                agent=agent,
                app_name=APP_NAME,
                session_service=session_service
            )
            
            # Test the interaction
            result = await runner.run_async(
                session_id=f"{SESSION_ID_MULTI_MODEL}_{agent_name}",
                user_message=test_query
            )
            
            print(f"Response from {agent_name}:")
            print(f"{result.response}")
            print()
            
        except Exception as e:
            error_msg = str(e)
            if "authentication" in error_msg.lower() or "api" in error_msg.lower():
                print(f"❌ {agent_name}: API key not configured or invalid")
                print(f"   Make sure to set the appropriate environment variable:")
                if "gpt4" in agent_name:
                    print("   export OPENAI_API_KEY='your-openai-api-key'")
                elif "claude" in agent_name:
                    print("   export ANTHROPIC_API_KEY='your-anthropic-api-key'")
                print()
            else:
                print(f"❌ {agent_name}: Error - {error_msg}\n")

def check_api_keys():
    """
    Check if required API keys are configured.
    """
    print("=== Checking API Key Configuration ===")
    
    openai_key = os.getenv("OPENAI_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    
    if openai_key:
        print("✅ OpenAI API key found")
    else:
        print("❌ OpenAI API key not found")
        print("   Set it with: export OPENAI_API_KEY='your-openai-api-key'")
    
    if anthropic_key:
        print("✅ Anthropic API key found")  
    else:
        print("❌ Anthropic API key not found")
        print("   Set it with: export ANTHROPIC_API_KEY='your-anthropic-api-key'")
    
    print("Note: Gemini model uses default ADK authentication\n")

async def test_individual_models():
    """
    Test each model individually with different queries.
    """
    print("=== Individual Model Testing ===\n")
    
    session_service = InMemorySessionService()
    
    # Test cases for different models
    test_cases = [
        {
            "model": MODEL_GEMINI_2_0_FLASH,
            "name": "Gemini 2.0 Flash",
            "agent_name": "weather_agent_gemini_individual",
            "query": "Tell me about the weather in New York"
        },
        {
            "model": MODEL_GPT_4O,
            "name": "GPT-4o",
            "agent_name": "weather_agent_gpt4_individual", 
            "query": "What's the current weather condition in London?"
        },
        {
            "model": MODEL_CLAUDE_3_SONNET,
            "name": "Claude 3 Sonnet",
            "agent_name": "weather_agent_claude_individual",
            "query": "Can you check the weather in Tokyo for me?"
        }
    ]
    
    for test_case in test_cases:
        try:
            print(f"--- {test_case['name']} ---")
            
            # Create agent
            agent = create_weather_agent(test_case["model"], test_case["agent_name"])
            
            # Create runner
            runner = Runner(
                agent=agent,
                app_name=APP_NAME,
                session_service=session_service
            )
            
            # Run test
            result = await runner.run_async(
                session_id=f"individual_test_{test_case['agent_name']}",
                user_message=test_case["query"]
            )
            
            print(f"Query: {test_case['query']}")
            print(f"Response: {result.response}")
            print()
            
        except Exception as e:
            print(f"❌ Error with {test_case['name']}: {str(e)}\n")

async def main():
    """
    Main function to run all multi-model demonstrations.
    """
    print("🌤️  Weather Bot Tutorial - Step 2: Multi-Model Support\n")
    print("This step demonstrates how the same agent logic can work with different LLM providers.")
    print("We'll test the weather agent with Gemini, GPT-4, and Claude models.\n")
    
    # Check API configuration
    check_api_keys()
    
    # Run model comparison test
    await test_model_comparison()
    
    print("=" * 60)
    
    # Run individual model tests
    await test_individual_models()
    
    print("=" * 60)
    print("✅ Step 2 Complete!")
    print("\nKey Learnings:")
    print("• ADK provides model abstraction through LiteLLM integration")
    print("• Same agent configuration works with different LLM providers")
    print("• Easy switching between Gemini, OpenAI, and Anthropic models")
    print("• Model-specific behaviors can be observed with identical inputs")

if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(main())
