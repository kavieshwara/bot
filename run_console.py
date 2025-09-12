#!/usr/bin/env python3
"""
Simple console runner for the English Teacher Agent
"""

import os
import sys
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("=" * 50)
    print("ENGLISH TEACHER AGENT - CONSOLE MODE")
    print("=" * 50)
    print("Current working directory:", os.getcwd())
    print()
    
    # Import agent module
    try:
        import agent
        print("✅ Agent module imported successfully")
    except Exception as e:
        print(f"❌ Failed to import agent module: {e}")
        return 1
    
    # Try to run the agent
    try:
        print("🚀 Running agent in console mode...")
        print("The agent is ready to help you learn English!")
        print("In a full implementation, this would connect to LiveKit and start listening for voice input.")
        print()
        print("Features:")
        print("  • Helps Tamil speakers learn English")
        print("  • Provides grammar correction")
        print("  • Assists with pronunciation")
        print("  • Maintains friendly conversation")
        print()
        print("Press Ctrl+C to stop the agent")
        print()
        
        # This would normally connect to LiveKit, but we'll just show that it's working
        print("📢 Agent is ready to talk!")
        print("In a full implementation, this would connect to LiveKit and start listening for voice input.")
        
        return 0
    except Exception as e:
        print(f"❌ Error running agent: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())