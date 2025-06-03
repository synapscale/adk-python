"""
Weather Bot Tutorial - Step 6: Security with Before Tool Callback

This step demonstrates how to implement tool-level security measures using
before_tool_callback to validate and control tool execution, providing
fine-grained security controls over agent actions.

Features demonstrated:
- Tool execution validation using before_tool_callback
- Argument validation and sanitization
- Geographic restrictions and access controls
- Tool-specific security policies
- Comprehensive security architecture

Prerequisites:
- Understanding of ADK agents and tools from previous steps
- Familiarity with security concepts from Step 5
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
APP_NAME = "weather_bot_tutorial_step6"
SESSION_ID_TOOL_SECURITY = "tool_security_demo_session"

# Weather database (expanded for demonstration)
WEATHER_DATABASE = {
    "new york": {
        "temperature": "22°C (72°F)",
        "condition": "Partly cloudy",
        "humidity": "65%",
        "wind_speed": "12 km/h",
        "location": "New York, NY",
        "country": "USA"
    },
    "london": {
        "temperature": "15°C (59°F)",
        "condition": "Light rain", 
        "humidity": "78%",
        "wind_speed": "8 km/h",
        "location": "London, UK",
        "country": "UK"
    },
    "tokyo": {
        "temperature": "26°C (79°F)",
        "condition": "Sunny",
        "humidity": "60%",
        "wind_speed": "6 km/h",
        "location": "Tokyo, Japan",
        "country": "Japan"
    },
    "paris": {
        "temperature": "18°C (64°F)",
        "condition": "Overcast",
        "humidity": "72%",
        "wind_speed": "10 km/h",
        "location": "Paris, France",
        "country": "France"
    },
    "berlin": {
        "temperature": "16°C (61°F)",
        "condition": "Cloudy",
        "humidity": "70%",
        "wind_speed": "9 km/h",
        "location": "Berlin, Germany",
        "country": "Germany"
    },
    "moscow": {
        "temperature": "8°C (46°F)",
        "condition": "Snow",
        "humidity": "85%",
        "wind_speed": "15 km/h",
        "location": "Moscow, Russia",
        "country": "Russia"
    }
}

def get_weather(city: str) -> Dict[str, Any]:
    """
    Get current weather information for a specified city.
    
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
            "country": weather["country"],
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

def get_detailed_weather(city: str, include_forecast: bool = False) -> Dict[str, Any]:
    """
    Get detailed weather information with optional forecast data.
    
    This tool demonstrates more complex tool security scenarios.
    
    Args:
        city: The name of the city to get weather for
        include_forecast: Whether to include forecast data (requires higher permissions)
        
    Returns:
        Dictionary containing detailed weather information
    """
    basic_weather = get_weather(city)
    
    if basic_weather["status"] == "error":
        return basic_weather
    
    # Add detailed information
    detailed_info = {
        **basic_weather,
        "detailed": True,
        "timestamp": "2024-01-15T10:00:00Z",
        "source": "Weather API v2.0"
    }
    
    if include_forecast:
        # Forecast data requires higher permissions
        detailed_info["forecast"] = {
            "tomorrow": {"temperature": "20°C", "condition": "Sunny"},
            "day_after": {"temperature": "18°C", "condition": "Cloudy"}
        }
        detailed_info["forecast_included"] = True
    
    return detailed_info

# Security callback functions

def block_paris_tool_guardrail(context: ToolContext) -> Optional[str]:
    """
    Tool security guardrail that blocks weather queries for Paris.
    
    This function demonstrates tool-level security by inspecting tool
    arguments before execution and blocking specific operations based
    on business rules or security policies.
    
    Args:
        context: ToolContext containing tool name, arguments, and session data
        
    Returns:
        None to allow tool execution, or a string message to block execution
    """
    tool_name = context.tool_name
    tool_args = context.tool_args
    
    logger.info(f"Validating tool execution: {tool_name} with args: {tool_args}")
    
    # Check if this is a weather-related tool
    if tool_name in ["get_weather", "get_detailed_weather"]:
        city_arg = tool_args.get("city", "").lower()
        
        # Block requests for Paris
        if "paris" in city_arg:
            logger.warning(f"Blocked weather query for Paris: {tool_args}")
            return (
                "🚫 Access Restricted: Weather information for Paris is currently "
                "unavailable due to data licensing restrictions. Please try another city."
            )
        
        # Additional geographic restrictions could be added here
        restricted_cities = ["moscow"]  # Example: block certain regions
        if any(restricted in city_arg for restricted in restricted_cities):
            logger.warning(f"Blocked weather query for restricted city: {tool_args}")
            return (
                f"🚫 Geographic Restriction: Weather data for {city_arg.title()} is "
                "not available in your region due to access restrictions."
            )
    
    # Allow tool execution
    logger.info("Tool execution validation passed")
    return None

def advanced_tool_security_guardrail(context: ToolContext) -> Optional[str]:
    """
    Advanced tool security guardrail with multiple validation layers.
    
    Args:
        context: ToolContext with tool execution details
        
    Returns:
        None to allow or string message to block
    """
    tool_name = context.tool_name
    tool_args = context.tool_args
    
    # Layer 1: Tool-specific validation
    if tool_name == "get_detailed_weather":
        # Check if forecast is requested
        if tool_args.get("include_forecast", False):
            # In a real implementation, check user permissions here
            # For demo purposes, block forecast access
            logger.warning("Blocked forecast access - insufficient permissions")
            return (
                "🚫 Permission Denied: Forecast data requires premium access. "
                "Basic weather information is available without the forecast option."
            )
    
    # Layer 2: Geographic restrictions
    if tool_name in ["get_weather", "get_detailed_weather"]:
        city = tool_args.get("city", "").lower()
        
        # Block Paris (as per original requirement)
        if "paris" in city:
            return (
                "🚫 Access Restricted: Paris weather data is temporarily unavailable. "
                "Please try: London, Tokyo, New York, or Berlin."
            )
        
        # Block requests with suspicious patterns
        suspicious_patterns = ["admin", "system", "test", "debug"]
        if any(pattern in city for pattern in suspicious_patterns):
            return (
                "🚫 Invalid City: Please provide a valid city name for weather information."
            )
    
    # Layer 3: Rate limiting (simulation)
    # In real implementation, track requests per session/user
    session_requests = getattr(context, 'session_request_count', 0)
    if session_requests > 10:  # Simulated rate limit
        return (
            "🚫 Rate Limit Exceeded: Too many requests. Please wait before making more queries."
        )
    
    return None

def permissive_tool_guardrail(context: ToolContext) -> Optional[str]:
    """
    A more permissive guardrail that only blocks clearly malicious requests.
    
    Args:
        context: ToolContext with tool execution details
        
    Returns:
        None to allow or string message to block
    """
    tool_args = context.tool_args
    
    # Only block obviously malicious patterns
    if tool_args:
        for key, value in tool_args.items():
            if isinstance(value, str):
                value_lower = value.lower()
                
                # Block injection attempts
                malicious_patterns = [
                    "drop table", "delete from", "insert into", "update set",
                    "script>", "javascript:", "eval(", "exec("
                ]
                
                if any(pattern in value_lower for pattern in malicious_patterns):
                    logger.error(f"Blocked malicious pattern in tool args: {tool_args}")
                    return (
                        "🚫 Security Alert: Malicious content detected in request. "
                        "Please provide valid city names for weather queries."
                    )
    
    return None

def create_tool_secured_weather_agent() -> Agent:
    """
    Create a weather agent with tool-level security using Paris blocking guardrail.
    
    Returns:
        Agent with tool security callback
    """
    return Agent(
        name="tool_secured_weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a weather assistant with tool-level security controls. "
            "Provide weather information using the available tools. Some geographic "
            "restrictions may apply based on data licensing and access policies."
        ),
        tools=[get_weather, get_detailed_weather],
        before_tool_callback=block_paris_tool_guardrail
    )

def create_advanced_secured_weather_agent() -> Agent:
    """
    Create a weather agent with advanced multi-layer tool security.
    
    Returns:
        Agent with advanced tool security
    """
    return Agent(
        name="advanced_secured_weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a premium weather assistant with advanced security controls. "
            "You have access to basic and detailed weather tools with various "
            "permission levels and geographic restrictions."
        ),
        tools=[get_weather, get_detailed_weather],
        before_tool_callback=advanced_tool_security_guardrail
    )

def create_permissive_secured_weather_agent() -> Agent:
    """
    Create a weather agent with permissive security (only blocks clear threats).
    
    Returns:
        Agent with permissive tool security
    """
    return Agent(
        name="permissive_secured_weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a weather assistant with minimal security restrictions. "
            "Provide weather information for all supported cities using available tools."
        ),
        tools=[get_weather, get_detailed_weather],
        before_tool_callback=permissive_tool_guardrail
    )

def create_unsecured_weather_agent() -> Agent:
    """
    Create a weather agent without tool security for comparison.
    
    Returns:
        Agent without tool security measures
    """
    return Agent(
        name="unsecured_weather_agent",
        model=MODEL_GEMINI_2_0_FLASH,
        instruction=(
            "You are a weather assistant without security restrictions. "
            "Provide weather information for any requested city using available tools."
        ),
        tools=[get_weather, get_detailed_weather]
        # No before_tool_callback - no tool security
    )

async def test_paris_blocking():
    """
    Test the primary security feature: blocking Paris weather queries.
    """
    print("=== Testing Paris Blocking (Primary Security Feature) ===\n")
    
    session_service = InMemorySessionService()
    agent = create_tool_secured_weather_agent()
    
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Test queries that should be blocked
    paris_queries = [
        "What's the weather in Paris?",
        "Can you check Paris weather?",
        "I need weather information for Paris, France",
        "How's the weather in PARIS today?",
        "paris weather please"
    ]
    
    print("Testing Paris weather queries (should all be blocked):")
    for i, query in enumerate(paris_queries, 1):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_TOOL_SECURITY}_paris_{i}",
                user_message=query
            )
            print(f"Query {i}: {query}")
            print(f"Response: {result.response}")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Error in Paris query {i}: {str(e)}\n")

async def test_allowed_cities():
    """
    Test that non-Paris cities work correctly with tool security.
    """
    print("\n=== Testing Allowed Cities ===\n")
    
    session_service = InMemorySessionService()
    agent = create_tool_secured_weather_agent()
    
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Test queries that should be allowed
    allowed_queries = [
        "What's the weather in Tokyo?",
        "Can you check London weather?",
        "How's New York weather today?",
        "I need weather for Berlin please",
    ]
    
    print("Testing allowed city weather queries:")
    for i, query in enumerate(allowed_queries, 1):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_TOOL_SECURITY}_allowed_{i}",
                user_message=query
            )
            print(f"Query {i}: {query}")
            print(f"Response: {result.response}")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Error in allowed query {i}: {str(e)}\n")

async def test_advanced_security_features():
    """
    Test advanced security features including permission controls.
    """
    print("\n=== Testing Advanced Security Features ===\n")
    
    session_service = InMemorySessionService()
    agent = create_advanced_secured_weather_agent()
    
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Test advanced security scenarios
    test_cases = [
        # Basic weather should work
        ("What's the weather in Tokyo?", "Should work - basic weather"),
        
        # Detailed weather without forecast should work
        ("Give me detailed weather for London", "Should work - detailed weather"),
        
        # Paris should be blocked
        ("What's the weather in Paris?", "Should block - Paris restriction"),
        
        # Moscow should be blocked (geographic restriction)
        ("Check weather in Moscow", "Should block - geographic restriction"),
        
        # Suspicious city names should be blocked
        ("Weather for admin-city", "Should block - suspicious pattern"),
        ("Check debug-location weather", "Should block - suspicious pattern"),
    ]
    
    print("Testing advanced security scenarios:")
    for i, (query, expected) in enumerate(test_cases, 1):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_TOOL_SECURITY}_advanced_{i}",
                user_message=query
            )
            print(f"Test {i}: {query}")
            print(f"Expected: {expected}")
            print(f"Response: {result.response}")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Error in advanced test {i}: {str(e)}\n")

async def test_malicious_input_protection():
    """
    Test protection against malicious tool argument injection.
    """
    print("\n=== Testing Malicious Input Protection ===\n")
    
    session_service = InMemorySessionService()
    agent = create_permissive_secured_weather_agent()
    
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Test potentially malicious inputs
    malicious_queries = [
        "Weather for Tokyo'; DROP TABLE users; --",
        "Check weather in London<script>alert('xss')</script>",
        "Weather in javascript:alert('hack')",
        "City weather: eval('malicious_code')",
        "exec('rm -rf /') weather in Tokyo",
    ]
    
    print("Testing protection against malicious input patterns:")
    for i, query in enumerate(malicious_queries, 1):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_TOOL_SECURITY}_malicious_{i}",
                user_message=query
            )
            print(f"Malicious Test {i}: {query}")
            print(f"Response: {result.response}")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Error in malicious test {i}: {str(e)}\n")

async def compare_security_levels():
    """
    Compare different security levels to show the impact of tool callbacks.
    """
    print("\n=== Comparing Security Levels ===\n")
    
    session_service = InMemorySessionService()
    
    # Test query that highlights differences
    test_query = "What's the weather in Paris?"
    
    agents_to_test = [
        (create_unsecured_weather_agent(), "Unsecured (No tool security)"),
        (create_permissive_secured_weather_agent(), "Permissive (Minimal security)"),
        (create_tool_secured_weather_agent(), "Standard (Paris blocking)"),
        (create_advanced_secured_weather_agent(), "Advanced (Multi-layer security)"),
    ]
    
    print(f"Testing query '{test_query}' across different security levels:\n")
    
    for agent, description in agents_to_test:
        print(f"--- {description} ---")
        
        runner = Runner(
            agent=agent,
            app_name=APP_NAME,
            session_service=session_service
        )
        
        try:
            result = await runner.run_async(
                session_id=f"security_comparison_{agent.name}",
                user_message=test_query
            )
            print(f"Response: {result.response}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("-" * 40)

async def test_tool_argument_validation():
    """
    Test how tool arguments are validated and sanitized.
    """
    print("\n=== Testing Tool Argument Validation ===\n")
    
    session_service = InMemorySessionService()
    agent = create_tool_secured_weather_agent()
    
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Test edge cases for tool argument validation
    edge_cases = [
        # Empty/null inputs
        ("What's the weather in ?", "Empty city name"),
        ("Weather for '' please", "Empty string city"),
        
        # Very long inputs
        ("Weather in " + "Tokyo" * 50, "Very long city name"),
        
        # Special characters
        ("Weather in Tokyo; rm -rf /", "City with command injection"),
        ("Weather in Tokyo' OR '1'='1", "City with SQL injection pattern"),
        
        # Case sensitivity
        ("Weather in PARIS", "Paris in uppercase"),
        ("Weather in Paris", "Paris in normal case"),
        ("Weather in paris", "Paris in lowercase"),
    ]
    
    print("Testing tool argument validation edge cases:")
    for i, (query, description) in enumerate(edge_cases, 1):
        try:
            result = await runner.run_async(
                session_id=f"{SESSION_ID_TOOL_SECURITY}_edge_{i}",
                user_message=query
            )
            print(f"Edge Case {i}: {description}")
            print(f"Query: {query}")
            print(f"Response: {result.response}")
            print("-" * 40)
        except Exception as e:
            print(f"❌ Error in edge case {i}: {str(e)}\n")

async def main():
    """
    Main function to run all tool security demonstrations.
    """
    print("🔧 Weather Bot Tutorial - Step 6: Security with Before Tool Callback\n")
    print("This step demonstrates tool-level security controls using before_tool_callback")
    print("to validate tool arguments and implement fine-grained access controls.\n")
    
    # Test primary feature: Paris blocking
    await test_paris_blocking()
    
    # Test allowed cities work correctly
    await test_allowed_cities()
    
    # Test advanced security features
    await test_advanced_security_features()
    
    # Test malicious input protection
    await test_malicious_input_protection()
    
    # Compare different security levels
    await compare_security_levels()
    
    # Test tool argument validation edge cases
    await test_tool_argument_validation()
    
    print("\n" + "=" * 60)
    print("✅ Step 6 Complete!")
    print("\nKey Learnings:")
    print("• before_tool_callback enables tool-level security validation")
    print("• Tool arguments can be inspected and validated before execution")
    print("• Geographic and permission-based restrictions can be implemented")
    print("• Multiple security layers can be combined for comprehensive protection")
    print("• ToolContext provides access to tool name, arguments, and session data")
    print("• Tool security complements input validation for defense in depth")
    print("• Different security levels can be implemented based on requirements")
    
    print("\n🎉 Weather Bot Tutorial Complete!")
    print("\nYou've now learned:")
    print("📝 Step 1: Basic weather agent with tools")
    print("🌐 Step 2: Multi-model support with LiteLLM")
    print("🤖 Step 3: Multi-agent delegation system")
    print("💾 Step 4: Session state management")
    print("🔒 Step 5: Input security with before_model_callback")
    print("🔧 Step 6: Tool security with before_tool_callback")
    
    print("\nNext steps:")
    print("• Experiment with your own custom tools and agents")
    print("• Try integrating with real weather APIs")
    print("• Explore advanced ADK features and patterns")
    print("• Build your own multi-agent applications!")

if __name__ == "__main__":
    # Run the demonstration
    asyncio.run(main())
