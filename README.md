# Voice Assistant API

A FastAPI-based voice assistant with speech-to-text, text-to-speech, grammar correction, and LLM capabilities.

## Features

- Speech-to-Text using Parakeet TDT
- Grammar correction
- Integration with open-source LLM
- Text-to-Speech conversion
- RESTful API endpoints
- Docker support

## Project Structure

```
voice_assistant/
│
├── Dockerfile
├── pyproject.toml
├── uv.lock
│
└── src/
    ├── main.py                    # Entry point for FastAPI app
    ├── api/                       # API endpoints
    ├── core/                      # App configuration
    ├── db/                        # Database integration (future)
    ├── models/                    # ML/NLP models (future)
    ├── schemas/                   # Pydantic models
    └── services/                  # Core services
```

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install .
   ```

3. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

## Docker

Build and run with Docker:

```bash
docker build -t voice-assistant .
docker run -p 8000:8000 voice-assistant
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

This project uses FastAPI and follows modern Python practices. To contribute:

1. Create a virtual environment
2. Install dependencies
3. Run tests
4. Submit pull requests

## License

MIT
