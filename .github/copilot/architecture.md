---
description: "MCP protocol concepts and server architecture patterns"
---

# MCP Protocol & Architecture

## What is MCP (Model Context Protocol)?

The Model Context Protocol is a standardized way for AI agents to:

1. **Discover available tools** - What can the agent do?
2. **Invoke tools** - How does the agent call them?
3. **Handle resources** - What data sources exist?
4. **Use prompts** - What predefined interactions are available?

MCP enables agents to extend their capabilities by connecting to external systems via a standardized protocol.

## MCP Server Basics

### Architecture

```
MCP Server (FastMCP)
├── Tools (callable functions)
│   ├── get_current_weather(lat, lon) → current conditions
│   ├── search_location(query) → list of locations
│   ├── get_forecast(lat, lon) → forecast data
│   ├── reverse_geocode(lat, lon) → address
│   └── weather_for_location(name) → combined operation
├── Resources (data sources)
│   └── (Optional: static data, documentation)
└── Prompts (predefined interactions)
    └── (Optional: agent-usable templates)
```

### Tool Anatomy

Every MCP tool has:

1. **Name**: Unique identifier (snake_case)
2. **Description**: From docstring first line
3. **Input Schema**: Generated from type hints
4. **Output Schema**: From return type + description

Example in FastMCP:

```python
@mcp.tool()
async def get_current_weather(lat: float, lon: float) -> dict:
    """Get current weather for coordinates."""
    # Implementation
```

FastMCP automatically generates:

- JSON schema for parameters from type hints
- Tool documentation from docstring
- Input validation based on types
- Protocol-compliant responses

### Tools in This Server

| Tool                   | Purpose                            | Parameters           | Returns                          |
| ---------------------- | ---------------------------------- | -------------------- | -------------------------------- |
| `get_current_weather`  | Current conditions at coordinates  | lat, lon, units      | Temp, conditions, humidity, wind |
| `search_location`      | Find coordinates for location name | query, limit         | List of matching locations       |
| `get_forecast`         | Multi-day forecast                 | lat, lon, units      | 5-day forecast data points       |
| `reverse_geocode`      | Get address from coordinates       | lat, lon             | City, country, address           |
| `weather_for_location` | Combined: search then get weather  | location_name, units | Weather for named location       |

## Protocol Flow: Agent → MCP Server → Response

```
1. Agent receives user query: "What's the weather in London?"

2. Agent discovers available tools via MCP
   - Receives tool schemas, descriptions, parameters

3. Agent decides to use: search_location(query="London")
   - Validates query against schema
   - Invokes tool via MCP protocol

4. MCP Server receives request
   - Invokes Python function: search_location("London")
   - Function returns: [{"name": "London", "lat": 51.5, "lon": -0.1, ...}]
   - Wraps result in MCP response format
   - Returns to agent

5. Agent receives results
   - Parses response
   - Decides next action: get_current_weather(lat=51.5, lon=-0.1)
   - Repeats invoke process

6. Agent assembles final response to user
   - Combines data from multiple tool calls
   - Formats for readability
```

## Design Patterns for MCP Tools

### 1. Single-Purpose Tools

Each tool does ONE thing well:

- `get_current_weather` - Get weather ONLY
- `search_location` - Search ONLY
- Don't combine operations in one tool

### 2. Consistent Error Handling

Always return structured responses:

- Success: `{"field": value, "metadata": ...}`
- Error: `{"error": "message", "code": "ERROR_CODE"}`
- Never throw exceptions; return error dict

### 3. Parameter Validation

Validate inputs before external calls:

```python
# Good: Validate first
if not (-90 <= lat <= 90):
    return {"error": "Invalid latitude"}

# Then call external API
result = await api_call(lat, lon)
```

### 4. Async All The Way

All I/O operations are async:

```python
@mcp.tool()
async def get_current_weather(...) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(...)
```

### 5. Clear Docstrings

Every tool needs complete documentation:

```python
@mcp.tool()
async def get_current_weather(lat: float, lon: float, units: str = "metric") -> dict:
    """
    Get current weather for coordinates.

    Args:
        lat: Latitude (-90 to 90)
        lon: Longitude (-180 to 180)
        units: "metric" or "imperial" (default: metric)

    Returns:
        {"temperature": float, "condition": str, "humidity": int, ...}
    """
```

### 6. Meaningful Tool Names

- `search_` prefix: search operations
- `get_` prefix: retrieval operations
- `reverse_` prefix: reverse operations
- `calculate_` prefix: computations

### 7. Consistent Response Structure

Make it easy for agents to parse:

```python
# Good: Consistent, nested structure
{
    "temperature": 20.5,
    "condition": "Cloudy",
    "humidity": 65,
    "wind_speed": 5.2,
    "units": "metric"
}

# Avoid: Inconsistent field names/structure
{
    "temp": 20,
    "weather": "Cloudy",
    "wet": 65
}
```

## Tool Composition

### Combining Tools (Multi-Step Operations)

The `weather_for_location` tool combines two operations:

1. Search for location by name
2. Get weather for resulting coordinates

This is useful for agents because they can:

- Use simpler tools for complex tasks
- Reduce number of agent decisions
- Provide user-friendly high-level operations

### When to Combine Tools

- When combination is commonly needed
- When it reduces API calls
- When it's a standard workflow
- Document the combination strategy

### When NOT to Combine

- Breaks single-responsibility principle
- Makes tool reuse harder
- Reduces flexibility for agents
- Increases error complexity

## Data Flow in Tools

### External API Integration Pattern

```python
@mcp.tool()
async def get_data(...) -> dict:
    try:
        # 1. Validate inputs
        if not validate(param):
            return {"error": "Invalid parameter"}

        # 2. Make external call
        async with httpx.AsyncClient() as client:
            response = await client.get(
                API_URL,
                params={"key": param},
                timeout=30
            )
            response.raise_for_status()

        # 3. Parse response
        data = response.json()

        # 4. Transform/validate result
        result = {
            "field1": data["api_field_1"],
            "field2": data["api_field_2"]
        }

        # 5. Return formatted response
        return result

    except TimeoutException:
        return {"error": "API request timed out"}
    except Exception as e:
        return {"error": f"Failed: {str(e)}"}
```

## Performance Considerations

### Timeout Strategy

- Set 30-second timeout for external calls
- Return error if timeout occurs
- Don't retry automatically (agent decides retry)

### Caching

- No built-in caching (agent/client caches responses)
- Tool calls are stateless
- Each invocation is independent

### Concurrency

- FastMCP handles concurrent requests
- Each tool invocation is independent
- Use async for I/O-bound operations

## Deployment Considerations

### Stdio Transport (Standard)

FastMCP uses stdio (standard input/output):

- Server reads requests from stdin
- Server writes responses to stdout
- VS Code or other client manages transport
- No network configuration needed

### Hosting Options

1. **Local**: Run on developer machine
2. **Prefect Horizon**: Managed cloud hosting
3. **Docker**: Containerized deployment
4. **Cloud Functions**: Serverless deployment

## Security Considerations

### API Key Management

- Never commit API keys
- Use environment variables
- Use .env files (not tracked in git)
- Rotate keys regularly

### Input Validation

- Validate all parameters
- Check ranges and formats
- Prevent injection attacks
- Sanitize external data

### Rate Limiting

- Respect API rate limits
- Implement exponential backoff
- Return rate limit errors to agent
- Cache results when possible
