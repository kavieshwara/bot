# English Teacher Agent with Tavus Avatar

An English teacher AI that helps Tamil speakers learn English with virtual avatar support, deployed on Render.

## Features

- Voice conversation with Google Realtime API
- Visual avatar support via Tavus
- English teaching with multilingual understanding
- Grammar correction and pronunciation help
- Friendly conversation practice

## Deployment to Render

This application is configured for deployment to Render with the following components:

1. `render.yaml` - Defines the Render service configuration
2. `Dockerfile` - Container configuration for the application
3. `render_app.py` - Special entry point for Render deployment with health checks

### Environment Variables

The following environment variables need to be configured in your Render dashboard:

- `LIVEKIT_URL` - Your LiveKit server URL
- `LIVEKIT_API_KEY` - Your LiveKit API key
- `LIVEKIT_API_SECRET` - Your LiveKit API secret
- `GOOGLE_API_KEY` - Your Google API key for Gemini
- `TAVUS_API_KEY` - Your Tavus API key
- `TAVUS_REPLICA_ID` - Your Tavus Replica ID
- `TAVUS_PERSONA_ID` - Your Tavus Persona ID

### Deployment Steps

1. Fork this repository to your GitHub account
2. Create a new Web Service on Render
3. Connect it to your forked repository
4. Configure the environment variables listed above
5. Deploy the service

The application will automatically bind to the PORT environment variable provided by Render and includes a health check endpoint at `/health`.

## Local Development

### Installation

```bash
pip install -r requirements.txt
```

### Running the Agent

```bash
# Console mode
python agent.py console

# Playground connection mode
python agent.py dev

# Background mode
python agent.py background

# Render deployment mode (for testing)
python agent.py render
```

## Usage

Once deployed, the agent will be available at your Render URL. The health check endpoint is available at `/health`.