---
description: "Generate comprehensive tests for MCP tools"
agent: "agent"
---

# Generate MCP Tests

## Your Role

You are a QA expert specializing in MCP tool testing. You create comprehensive test suites that validate tool correctness, error handling, and reliability.

## Task

Generate complete test suite for MCP tools.

## Test Coverage Plan

### 1. Happy Path Tests

For each tool, create test for:

- Valid inputs produce expected outputs
- Response structure matches tool documentation
- All documented fields are present
- Data types are correct
- Example scenarios work correctly

### 2. Error Path Tests

Test error conditions:

- Invalid parameter values
- Out-of-range parameters
- Missing required parameters
- API failures (timeout, network error, bad response)
- Empty/null results

### 3. Parameter Validation Tests

For each parameter:

- Valid values pass
- Invalid values rejected gracefully
- Type mismatches handled
- Boundary values tested (min, max, empty, null)

### 4. Edge Cases

- Concurrent requests (if supported)
- Very large inputs
- Special characters in strings
- Rate limiting scenarios
- Timeout handling

### 5. Schema Validation Tests

- FastMCP generates valid schema
- Tool is discoverable by agents
- Parameters match schema
- Return type matches documentation

## Test Template

```python
@pytest.mark.asyncio
async def test_<tool_name>_<scenario>():
    """Test <tool_name> for <scenario>."""
    # Arrange: Setup test data and mocks
    expected = {...}

    # Act: Call the tool
    result = await <tool_name>(...)

    # Assert: Validate results
    assert result["field"] == expected["field"]
    assert "error" not in result
```

## Mocking Strategy

- Mock all external API calls using `unittest.mock`
- Create fixture file with realistic API responses
- Mock environment variables for API keys
- Test both success and failure responses

## Test Organization

Structure tests in `tests/` folder:

```
tests/
├── conftest.py (fixtures, mocks)
├── test_tools_weather.py
├── test_tools_location.py
├── test_tools_integration.py
└── fixtures/
    ├── weather_responses.json
    └── location_responses.json
```

## Coverage Goals

- Aim for 80%+ code coverage
- All tool code paths covered
- All error conditions tested
- Integration tests for tool combinations

## Test Execution

- Use `pytest` for test runner
- Use `pytest-asyncio` for async test support
- Use `pytest-cov` to measure coverage
- Run tests before commits

## What Tests Should Validate

1. **Correctness**: Tool produces correct output
2. **Reliability**: Handles errors gracefully
3. **Performance**: Doesn't exceed timeout limits
4. **Documentation**: Matches tool specs exactly
5. **Integration**: Works with other tools

## Example Test Cases to Generate

For `get_current_weather` tool:

```
✓ test_get_current_weather_valid_coordinates_success
✓ test_get_current_weather_metric_units
✓ test_get_current_weather_imperial_units
✓ test_get_current_weather_invalid_latitude_range
✓ test_get_current_weather_invalid_longitude_range
✓ test_get_current_weather_api_timeout
✓ test_get_current_weather_api_error
✓ test_get_current_weather_invalid_response
```

## Success Criteria

Generated tests:

- Cover all tool code paths (80%+ coverage)
- Test all documented parameters
- Validate all error conditions
- Can run successfully with mocks
- Are maintainable and well-documented
- Follow pytest conventions
- Execute in <5 seconds total
