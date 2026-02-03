---
description: "Project technology stack, versions, and dependencies"
---

# Technology Stack

## Core Technologies

### FastMCP (Python MCP Server Framework)

- **Version**: 2.x (production-ready)
- **Documentation**: https://gofastmcp.com/
- **Repository**: https://github.com/jlowin/fastmcp
- **Installation**: `pip install fastmcp`
- **Key Features**:
  - Automatic JSON schema generation from Python type hints
  - Built-in async/await support
  - Decorator-based tool/resource/prompt definition
  - Handles MCP protocol compliance automatically
  - Zero-config deployment ready

### OpenWeatherMap API

- **Service**: Weather data and forecasts
- **API Base URL**: `https://api.openweathermap.org/data/2.5`
- **Key Endpoints**:
  - `/weather` - Current weather
  - `/forecast` - 5-day forecast
- **Authentication**: API key via `OPENWEATHERMAP_API_KEY` env var
- **Rate Limits**: Free tier 1000 calls/day
- **Docs**: https://openweathermap.org/api

### OpenStreetMap Nominatim API

- **Service**: Location search and reverse geocoding
- **API Base URL**: `https://nominatim.openstreetmap.org`
- **Key Endpoints**:
  - `/search` - Search for locations
  - `/reverse` - Reverse geocoding (coordinates to address)
- **Rate Limits**: 1 request per second
- **User-Agent**: Required header must be set
- **Docs**: https://nominatim.org/release-docs/latest/api/Overview/

### Python Runtime

- **Version**: 3.9+
- **Package Manager**: pip or uv
- **Virtual Environment**: venv (recommended)

### HTTP Client

- **Library**: httpx (async HTTP client)
- **Version**: 0.24+
- **Features**: Async support, timeouts, streaming

## Development Tools

### Testing

- **Framework**: pytest
- **Async Support**: pytest-asyncio
- **Mocking**: unittest.mock (built-in)
- **Coverage**: pytest-cov

### Code Quality

- **Linting**: pylint or ruff
- **Formatting**: black
- **Type Checking**: mypy

## Environment Configuration

### Required Environment Variables

```bash
# OpenWeatherMap API
OPENWEATHERMAP_API_KEY=your-api-key-here

# Optional: API rate limit configs
WEATHER_API_TIMEOUT=30
NOMINATIM_REQUEST_DELAY=1
```

### Suggested Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastmcp httpx pytest pytest-asyncio pytest-cov

# Copy and configure .env
cp .env.example .env
# Edit .env with your API keys
```

## Deployment Considerations

### Prefect Horizon (Free Hosting)

- Managed MCP server deployment
- Automatic scaling
- Dashboard monitoring
- Free tier available
- https://www.prefect.io/

### Docker Deployment

- Can containerize FastMCP servers
- Use Python 3.11+ slim images
- Mount .env for credentials

### Performance Targets

- Tool invocation: <1s (local logic)
- API calls: <5s (with timeout)
- Concurrent calls: Support at least 10 simultaneous requests

## Compatibility

### VS Code Copilot Integration

- Requires MCP server via stdio transport
- Works with Copilot Chat in VS Code
- Custom agents can access server tools automatically
- Slash commands discover server tools as options

### MCP Protocol Version

- Protocol v1 (stable)
- Supports tools, resources, and prompts
- Backwards compatible with MCP clients

## Library Dependencies

### Production

- fastmcp >= 2.0
- httpx >= 0.24
- python >= 3.9

### Development

- pytest >= 7.0
- pytest-asyncio >= 0.20
- pytest-cov >= 4.0
- black >= 23.0
- mypy >= 1.0

### Optional

- ruff (fast linting)
- pre-commit (git hooks)
- uvloop (faster event loop)
