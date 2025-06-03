"""
Weather Bot Tutorial - Step 4: Session State Management

This step demonstrates how to manage session state in ADK agents, allowing
the bot to remember information across multiple interactions and provide
a more personalized experience.

Features demonstrated:
- ToolContext for accessing session state
- Automatic state saving with output_key parameter
- Stateful weather recommendations based on previous queries
- Session persistence across multiple interactions
- User preference tracking

Prerequisites:
- Understanding of basic ADK agents from previous steps
- Familiarity with agent tools and configurations
"""

import asyncio
from typing import Dict, Any, Optional
import logging

# ADK Core imports
from google.adk.core import Agent, ToolContext
from google.adk.models import Gemini
from google.adk.core.runners import Runner
from google.adk.core.sessions import InMemorySessionService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Model configuration
MODEL_GEMINI_2_0_FLASH = Gemini(model="gemini-2.0-flash-exp")

# Application configuration
APP_NAME = "weather_bot_tutorial_step4"
SESSION_ID_STATEFUL = "stateful_demo_session"

# Enhanced weather database with more cities and detailed information
WEATHER_DATABASE = {
    "new york": {
        "temperature": "22°C (72°F)",
        "condition": "Partly cloudy", 
        "humidity": "65%",
        "wind_speed": "12 km/h",
        "location": "New York, NY",
        "feels_like": "24°C (75°F)",
        "uv_index": "6 (High)",
        "visibility": "10 km"
    },
    "london": {
        "temperature": "15°C (59°F)",
        "condition": "Light rain",
        "humidity": "78%", 
        "wind_speed": "8 km/h",
        "location": "London, UK",
        "feels_like": "13°C (55°F)",
        "uv_index": "2 (Low)",
        "visibility": "8 km"
    },
    "tokyo": {
        "temperature": "26°C (79°F)",
        "condition": "Sunny",
        "humidity": "60%",
        "wind_speed": "6 km/h", 
        "location": "Tokyo, Japan",
        "feels_like": "28°C (82°F)",
        "uv_index": "8 (Very High)",
        "visibility": "15 km"
    },
    "paris": {
        "temperature": "18°C (64°F)",
        "condition": "Overcast",
        "humidity": "72%",
        "wind_speed": "10 km/h",
        "location": "Paris, France",
        "feels_like": "17°C (63°F)",
        "uv_index": "3 (Moderate)",
        "visibility": "12 km"
    },
    "sydney": {
        "temperature": "25°C (77°F)",
        "condition": "Clear skies",
        "humidity": "55%",
        "wind_speed": "14 km/h",
        "location": "Sydney, Australia", 
        "feels_like": "27°C (81°F)",
        "uv_index": "9 (Very High)",
        "visibility": "20 km"
    },
    "berlin": {
        "temperature": "16°C (61°F)",
        "condition": "Cloudy",
        "humidity": "70%",
        "wind_speed": "9 km/h",
        "location": "Berlin, Germany",
        "feels_like": "15°C (59°F)",
        "uv_index": "4 (Moderate)",
        "visibility": "11 km"
    }
}

def get_weather(city: str) -> Dict[str, Any]:
    """
    Get current weather information for a specified city (basic version).
    
    Args:
        city: The name of the city to get weather for
        
    Returns:
        Dictionary containing weather information
    """
    city_lower = city.lower()
    if city_lower in WEATHER_DATABASE:
        weather = WEATHER_DATABASE[city_lower]
        return {
            "status": "success",
            "city": weather["location"],
            "temperature": weather["temperature"],
            "condition": weather["condition"],
            "humidity": weather["humidity"],
            "wind_speed": weather["wind_speed"]
        }
    else:
        available_cities = ", ".join([data["location"] for data in WEATHER_DATABASE.values()])
        return {
            "status": "error", 
            "error_message": f"Weather data not available for {city}. Available cities: {available_cities}"
        }

def get_weather_stateful(city: str, context: ToolContext) -> Dict[str, Any]:
    """
    Get weather information with stateful capabilities that remembers user preferences.
    
    This function demonstrates ADK's session state management by:
    - Accessing previous queries from session state
    - Providing personalized recommendations based on history
    - Automatically saving new query information to state
    
    Args:
        city: The name of the city to get weather for
        context: ToolContext providing access to session state
        
    Returns:
        Dictionary containing weather information plus personalized insights
    """
    logger.info(f"Getting stateful weather for: {city}")
    
    # Get basic weather information
    city_lower = city.lower()
    if city_lower not in WEATHER_DATABASE:
        available_cities = ", ".join([data["location"] for data in WEATHER_DATABASE.values()])
        return {
            "status": "error",
            "error_message": f"Weather data not available for {city}. Available cities: {available_cities}"
        }
    
    weather = WEATHER_DATABASE[city_lower]
    
    # Access session state to get previous queries
    previous_queries = context.get("previous_weather_queries", [])
    user_preferences = context.get("user_preferences", {})
    
    # Build comprehensive weather response
    response = {
        "status": "success",
        "city": weather["location"],
        "temperature": weather["temperature"],
        "condition": weather["condition"],
        "humidity": weather["humidity"],
        "wind_speed": weather["wind_speed"],
        "feels_like": weather["feels_like"],
        "uv_index": weather["uv_index"],
        "visibility": weather["visibility"]
    }
    
    # Add personalized insights based on previous queries
    if previous_queries:
        response["personalized_insights"] = generate_personalized_insights(
            current_city=city_lower,
            current_weather=weather,
            previous_queries=previous_queries
        )
        
        # Update user preferences based on query patterns
        user_preferences = update_user_preferences(
            user_preferences, 
            city_lower, 
            weather,
            previous_queries
        )
        
        response["user_preferences"] = user_preferences
    
    # Prepare data to save to session state
    new_query = {
        "city": city_lower,
        "location": weather["location"],
        "temperature": weather["temperature"],
        "condition": weather["condition"],
        "timestamp": "current"  # In real implementation, use actual timestamp
    }
    
    # Add current query to history
    updated_queries = previous_queries + [new_query]
    
    # Keep only last 5 queries to prevent state from growing too large
    if len(updated_queries) > 5:
        updated_queries = updated_queries[-5:]
    
    # This data will be automatically saved to session state due to output_key
    response["session_data"] = {
        "previous_weather_queries": updated_queries,
        "user_preferences": user_preferences
    }
    
    logger.info(f"Updated session state with {len(updated_queries)} queries")
    return response

def generate_personalized_insights(current_city: str, current_weather: Dict, previous_queries: list) -> list:
    """
    Generate personalized insights based on user's weather query history.
    
    Args:
        current_city: Current city being queried
        current_weather: Current weather data
        previous_queries: List of previous weather queries
        
    Returns:
        List of personalized insight strings
    """
    insights = []
    
    # Check if user has queried this city before
    previous_cities = [query["city"] for query in previous_queries]
    if current_city in previous_cities:
        insights.append(f"You've checked weather for {current_weather['location']} before!")
    
    # Compare temperature with previous queries
    if previous_queries:
        last_query = previous_queries[-1]
        try:
            current_temp = int(current_weather["temperature"].split("°")[0])
            last_temp = int(last_query["temperature"].split("°")[0])
            
            if current_temp > last_temp + 5:
                insights.append(f"It's significantly warmer in {current_weather['location']} compared to your last query ({last_query['location']})!")
            elif current_temp < last_temp - 5:
                insights.append(f"It's much cooler in {current_weather['location']} compared to your last query ({last_query['location']})!")
        except:
            pass  # Skip temperature comparison if parsing fails
    
    # Suggest based on conditions
    if current_weather["condition"].lower() in ["sunny", "clear skies"]:
        insights.append("Great weather for outdoor activities!")
    elif "rain" in current_weather["condition"].lower():
        insights.append("Don't forget an umbrella if you're heading out!")
    
    return insights

def update_user_preferences(current_prefs: Dict, city: str, weather: Dict, previous_queries: list) -> Dict:
    """
    Update user preferences based on query patterns.
    
    Args:
        current_prefs: Current user preferences
        city: City being queried
        weather: Weather data for the city
        previous_queries: Historical queries
        
    Returns:
        Updated user preferences dictionary
    """
    prefs = current_prefs.copy()
    
    # Track favorite cities (most queried)
    city_counts = prefs.get("city_query_counts", {})
    city_counts[city] = city_counts.get(city, 0) + 1
    prefs["city_query_counts"] = city_counts
    
    # Determine favorite city
    if city_counts:
        favorite_city = max(city_counts, key=city_counts.get)
        prefs["favorite_city"] = favorite_city
    
    # Track weather condition preferences
    condition_prefs = prefs.get("condition_preferences", {})
    condition = weather["condition"].lower()
    condition_prefs[condition] = condition_prefs.get(condition, 0) + 1
    prefs["condition_preferences"] = condition_prefs
    
    # Update query streak
    prefs["total_queries"] = len(previous_queries) + 1
    
    return prefs

def create_stateful_weather_agent() -> Agent:
    """
    Create a weather agent with session state management capabilities.
    
    Returns:
        Configured Agent with stateful weather functionality
    """
    return Agent(
        name="stateful_weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are an advanced weather assistant with memory capabilities. "
            "Use the get_weather_stateful tool to provide weather information that "
            "includes personalized insights based on the user's previous queries. "
            "Always mention any personalized insights or preferences when available. "
            "Be helpful and reference the user's history when it adds value to your response."
        ),
        tools=[{
            "function": get_weather_stateful,
            "output_key": "session_data"  # Automatically save session_data to state
        }]
    )

def create_basic_weather_agent() -> Agent:
    """
    Create a basic weather agent without state management for comparison.
    
    Returns:
        Basic weather agent
    """
    return Agent(
        name="basic_weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a basic weather assistant. Use the get_weather tool to provide "
            "weather information for cities. Be helpful and informative."
        ),
        tools=[get_weather]
    )

async def test_stateful_interactions():
    """
    Test stateful interactions showing how the agent remembers previous queries.
    """
    print("=== Testing Stateful Weather Interactions ===\n")
    
    session_service = InMemorySessionService()
    agent = create_stateful_weather_agent()
    
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Series of queries that should build up session state
    queries = [
        "What's the weather like in Tokyo?",
        "How about London?",
        "Can you check Paris weather?",
        "What's it like in Tokyo again?",  # Should recognize repeat query
        "Tell me about Berlin weather",
        "How's Sydney doing weather-wise?"
    ]
    
    print("Running a series of weather queries to demonstrate state management:")
    print("(Notice how the bot starts providing personalized insights based on history)\n")
    
    for i, query in enumerate(queries, 1):
        try:
            result = await runner.run_async(
                session_id=SESSION_ID_STATEFUL,
                user_message=query
            )
            print(f"Query {i}: {query}")
            print(f"Response: {result.response}")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Error in query {i}: {str(e)}\n")

async def test_session_persistence():
    """
    Test that session state persists across multiple runner instances.
    """
    print("\n=== Testing Session Persistence ===\n")
    
    session_service = InMemorySessionService()
    
    # First interaction
    print("--- First Runner Instance ---")
    agent1 = create_stateful_weather_agent()
    runner1 = Runner(
        agent=agent1,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    try:
        result1 = await runner1.run_async(
            session_id=SESSION_ID_STATEFUL + "_persistence",
            user_message="What's the weather in New York?"
        )
        print("First query: What's the weather in New York?")
        print(f"Response: {result1.response}")
        print()
    except Exception as e:
        print(f"❌ Error in first query: {str(e)}\n")
    
    # Second interaction with new runner instance but same session
    print("--- Second Runner Instance (Same Session) ---")
    agent2 = create_stateful_weather_agent()
    runner2 = Runner(
        agent=agent2,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    try:
        result2 = await runner2.run_async(
            session_id=SESSION_ID_STATEFUL + "_persistence",
            user_message="Now check London please"
        )
        print("Second query: Now check London please")
        print(f"Response: {result2.response}")
        print("(Should reference previous New York query)")
        print()
    except Exception as e:
        print(f"❌ Error in second query: {str(e)}\n")

async def compare_stateful_vs_basic():
    """
    Compare stateful agent vs basic agent to show the difference.
    """
    print("\n=== Comparing Stateful vs Basic Agent ===\n")
    
    session_service = InMemorySessionService()
    
    # Test basic agent
    print("--- Basic Agent (No State Management) ---")
    basic_agent = create_basic_weather_agent()
    basic_runner = Runner(
        agent=basic_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    queries = ["Weather in Tokyo?", "How about London?", "Tokyo again?"]
    
    for i, query in enumerate(queries):
        try:
            result = await basic_runner.run_async(
                session_id="basic_test",
                user_message=query
            )
            print(f"Basic Agent - {query}")
            print(f"Response: {result.response}")
            print()
        except Exception as e:
            print(f"❌ Basic agent error: {str(e)}\n")
    
    print("-" * 60)
    
    # Test stateful agent
    print("--- Stateful Agent (With State Management) ---")
    stateful_agent = create_stateful_weather_agent()
    stateful_runner = Runner(
        agent=stateful_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    for i, query in enumerate(queries):
        try:
            result = await stateful_runner.run_async(
                session_id="stateful_test",
                user_message=query
            )
            print(f"Stateful Agent - {query}")
            print(f"Response: {result.response}")
            print()
        except Exception as e:
            print(f"❌ Stateful agent error: {str(e)}\n")

async def test_tool_context_access():
    """
    Test direct tool usage to show how ToolContext works.
    """
    print("\n=== Testing Direct ToolContext Access ===\n")
    
    # Create a mock ToolContext for demonstration
    class MockToolContext:
        def __init__(self):
            self.state = {}
        
        def get(self, key: str, default=None):
            return self.state.get(key, default)
        
        def set(self, key: str, value):
            self.state[key] = value
    
    context = MockToolContext()
    
    # Simulate a series of tool calls
    cities = ["Tokyo", "London", "Paris"]
    
    print("Simulating direct tool calls with ToolContext:")
    for city in cities:
        result = get_weather_stateful(city, context)
        
        # Update context with the returned session data
        if "session_data" in result:
            for key, value in result["session_data"].items():
                context.set(key, value)
        
        print(f"Query: {city}")
        print(f"Status: {result['status']}")
        if "personalized_insights" in result:
            print(f"Insights: {result['personalized_insights']}")
        if "user_preferences" in result:
            prefs = result["user_preferences"]
            if "favorite_city" in prefs:
                print(f"Favorite City: {prefs['favorite_city']}")
            print(f"Total Queries: {prefs.get('total_queries', 0)}")
        print("-" * 30)

async def main():
    """
    Main function to run all session state demonstrations.
    """
    print("💾 Weather Bot Tutorial - Step 4: Session State Management\n")
    print("This step demonstrates how ADK agents can maintain state across interactions,")
    print("providing personalized experiences based on user history.\n")
    
    # Test stateful interactions
    await test_stateful_interactions()
    
    # Test session persistence
    await test_session_persistence()
    
    # Compare stateful vs basic approaches
    await compare_stateful_vs_basic()
    
    # Test direct tool context access
    await test_tool_context_access()
    
    print("\n" + "=" * 60)
    print("✅ Step 4 Complete!")
    print("\nKey Learnings:")
    print("• ToolContext provides access to session state within tools")
    print("• output_key parameter automatically saves tool output to session state")
    print("• Session state enables personalized user experiences")
    print("• State persists across multiple interactions in the same session")
    print("• Stateful agents can provide insights based on user history")
    print("• Session management is handled automatically by ADK")

if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(main())
