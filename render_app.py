#!/usr/bin/env python3
"""
Render deployment wrapper for the English Teacher Agent.
This file handles port binding for Render deployment.
"""

import os
import sys
import asyncio
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

# Simple HTTP handler to respond to Render's port checking
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "healthy", "agent": "English Teacher Agent"}')
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"English Teacher Agent is running")
    
    def log_message(self, format, *args):
        # Suppress logging
        return

def start_health_server(port):
    """Start a simple HTTP server for health checks"""
    try:
        server = HTTPServer(('', port), HealthCheckHandler)
        print(f"Health check server started on port {port}")
        server.serve_forever()
    except Exception as e:
        print(f"Failed to start health check server: {e}")

def main():
    # Get port from Render environment or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    print(f"🚀 Starting English Teacher Agent for Render deployment on port {port}")
    
    # Start health check server in a separate thread
    health_thread = threading.Thread(target=start_health_server, args=(port,), daemon=True)
    health_thread.start()
    
    # Import and run the agent
    try:
        import agent
        print("✅ Agent module imported successfully")
        
        # Run the agent in the background
        print("🤖 Starting English Teacher Agent...")
        # Run the agent with auto-restart capability
        asyncio.run(agent.run_agent_with_auto_restart())
        
    except ImportError as e:
        print(f"❌ Failed to import agent module: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running agent: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()