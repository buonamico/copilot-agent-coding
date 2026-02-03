---
description: "Testing strategies and patterns for MCP tools"
applyTo: "/src/**"
---

# Testing & Validation Standards

## Testing Philosophy

- Test coverage: aim for 80%+
- Test all tool code paths
- Mock external dependencies (APIs)
- Validate error handling paths
- Test tool schemas are valid

## Test Structure Pattern

### Unit Test Example

```python
import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_get_current_weather_success():
    """Test successful weather retrieval."""
    mock_response = {
        "main": {"temp": 20, "feels_like": 18, "humidity": 65, "pressure": 1013},
        "weather": [{"main": "Cloudy", "description": "overcast clouds"}],
        "wind": {"speed": 5},
        "name": "London"
    }

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response
        result = await get_current_weather(51.5, -0.1)
        assert result["temperature"] == 20
        assert result["location"] == "London"


@pytest.mark.asyncio
async def test_get_current_weather_api_failure():
    """Test error handling when API fails."""
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.side_effect = httpx.TimeoutException("API timeout")
        result = await get_current_weather(51.5, -0.1)
        assert "error" in result
        assert "timed out" in result["error"].lower()


def test_search_location_parameter_validation():
    """Test parameter validation."""
    # Validate that invalid parameters are rejected properly
    result = await search_location("", limit=0)
    assert "error" in result
```

## What to Test

### 1. Happy Path (Success Cases)

- Valid inputs produce expected outputs
- Response structure is correct
- All required fields are present
- Data types are correct

### 2. Parameter Validation

- Invalid parameter types are handled
- Out-of-range values are rejected
- Required parameters are enforced
- Optional parameters work correctly

### 3. Error Handling

- API timeouts are caught
- Invalid API responses are handled
- Network failures return error dicts
- Error messages are descriptive

### 4. Edge Cases

- Boundary values (0, max, min)
- Empty results
- Null/None values
- Special characters in strings

### 5. Schema Validation

- Tools have complete docstrings
- Type hints are present on all parameters
- Return types are documented
- Parameter descriptions are clear

## Test Organization

```
tests/
├── conftest.py (fixtures, mocks)
├── test_tools_weather.py (weather tool tests)
├── test_tools_location.py (location tool tests)
├── test_tools_integration.py (combined tool tests)
└── fixtures/ (mock data, responses)
```

## Mocking Strategy

- Mock all external API calls
- Use `unittest.mock` for patching
- Create fixture files with realistic API responses
- Mock httpx.AsyncClient for HTTP calls
- Mock os.getenv for environment variables

## Test Naming Convention

- `test_<tool_name>_<scenario>` for unit tests
- `test_<tool_name>_<scenario>_success` for happy path
- `test_<tool_name>_<scenario>_error` for failure cases
- `test_<tool_name>_<scenario>_validates_<param>` for validation

## Continuous Quality

- Run tests before committing
- Maintain 80%+ coverage
- Fix failing tests immediately
- Add tests for any bugs found
- Review test quality during code reviews

## Performance Testing

- Measure response times for each tool
- Flag tools taking >5 seconds
- Test with various data sizes
- Validate timeout handling

## Schema Validation Testing

- Verify FastMCP generates correct schemas from docstrings
- Validate tool names, parameters, descriptions appear in schema
- Test that agents can discover and invoke tools
- Verify return types match schema definitions

## Integration Testing

- Test multiple tools working together
- Test tool calling patterns agents use
- Test error recovery across tool chains
- Simulate real-world usage scenarios
