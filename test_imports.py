#!/usr/bin/env python3
"""
Test script to verify ADK and LiteLLM imports
"""

def test_imports():
    """Test all required imports for ADK and LiteLLM"""
    import_results = []
    
    # Test google.adk Agent import
    try:
        from google.adk import Agent
        import_results.append("✓ Agent imported successfully")
    except Exception as e:
        import_results.append(f"✗ Agent import failed: {e}")
    
    # Test LiteLlm import  
    try:
        from google.adk.models.lite_llm import LiteLlm
        import_results.append("✓ LiteLlm imported successfully")
    except Exception as e:
        import_results.append(f"✗ LiteLlm import failed: {e}")
    
    # Test InMemorySessionService import
    try:
        from google.adk.sessions.in_memory_session_service import InMemorySessionService
        import_results.append("✓ InMemorySessionService imported successfully")
    except Exception as e:
        import_results.append(f"✗ InMemorySessionService import failed: {e}")
    
    # Test Runner import
    try:
        from google.adk.runners import Runner
        import_results.append("✓ Runner imported successfully")
    except Exception as e:
        import_results.append(f"✗ Runner import failed: {e}")
    
    # Test types import
    try:
        from google.genai import types
        import_results.append("✓ types imported successfully")
    except Exception as e:
        import_results.append(f"✗ types import failed: {e}")
    
    # Test basic imports
    try:
        import os
        import asyncio
        import warnings
        import logging
        import_results.append("✓ Standard library imports successful")
    except Exception as e:
        import_results.append(f"✗ Standard library imports failed: {e}")
    
    return import_results

if __name__ == "__main__":
    print("# @title Import necessary libraries")
    print("Testing ADK and LiteLLM imports...")
    print()
    
    results = test_imports()
    for result in results:
        print(result)
    
    # Configure warnings and logging as requested
    import warnings
    warnings.filterwarnings("ignore")
    
    import logging
    logging.basicConfig(level=logging.ERROR)
    
    print()
    print("Installation and import test complete.")
