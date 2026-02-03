---
description: "FastMCP server and tool development best practices"
applyTo: "**"
---

# MCP Server Development Standards

## FastMCP-Specific Guidelines

### Tool Definition Pattern

```python
@mcp.tool()
async def tool_name(param1: str, param2: int = 10) -> dict:
    """
    Descriptive one-liner.

    Detailed explanation of what the tool does, when to use it,
    and what problems it solves.

    Args:
        param1: Description of param1, constraints, valid values
        param2: Description with default value (default: 10)

    Returns:
        Description of return structure and fields

    Raises:
        Describes error conditions and how they're handled
    """
    # Implementation
    pass
```

### Type Hints Requirements

- Use specific types: `str`, `int`, `float`, `dict`, `list`
- Use `Optional[Type]` for nullable values
- Use `Union[Type1, Type2]` for multiple types
- For complex returns, specify structure: `dict` with field descriptions in docstring
- **Never** use `Any` type

### Async Patterns

- All I/O operations (API calls, database queries) must be async
- Use `httpx.AsyncClient` for HTTP calls
- Use `async with` for context managers
- Non-blocking operations throughout the call chain

### Error Handling Pattern

```python
try:
    # Operation
    result = await external_api_call()
    return {"success": True, "data": result}
except httpx.TimeoutException:
    return {"error": "API request timed out", "code": "TIMEOUT"}
except Exception as e:
    return {"error": f"Operation failed: {str(e)}", "code": "UNKNOWN"}
```

### Parameter Validation

- Validate all input parameters before use
- Check type constraints, ranges, valid values
- Return validation errors in response dict (not as exceptions)
- Example:
  ```python
  if not (-90 <= lat <= 90):
      return {"error": "Latitude must be between -90 and 90"}
  ```

### Resource/API Integration

- Use environment variables for API keys (`.env` files)
- Never hardcode credentials
- Implement timeouts for external calls
- Include User-Agent headers for API requests
- Handle rate limiting gracefully

## Tool Naming Conventions

- Use `get_` prefix for retrieval operations: `get_current_weather`
- Use `search_` prefix for search operations: `search_location`
- Use `reverse_` prefix for reverse operations: `reverse_geocode`
- Use `calculate_` prefix for computations: `calculate_distance`
- Always use `snake_case`, lowercase
- Be specific and descriptive

## Documentation Standards for Tools

Each tool docstring must include:

1. **One-liner**: What the tool does
2. **Detailed description**: Context and use cases
3. **Args section**: All parameters with constraints
4. **Returns section**: Structure of return value
5. **Example values** (in comments or docstring): Help agents understand usage

## Response Structure

Consistent response format for all tools:

```python
# Success response
{"<data_field>": value, "units": "metric", "timestamp": 1234567890}

# Error response
{"error": "descriptive error message", "code": "ERROR_CODE", "context": "what was attempted"}
```

## Testing Requirements

- Test happy path: valid inputs, successful execution
- Test error cases: invalid inputs, API failures, timeout scenarios
- Mock external APIs using `httpx` mocking or similar
- Each tool should have at least 2-3 test cases
- Name tests: `test_<tool_name>_<scenario>`

## Performance Considerations

- Avoid unnecessary API calls (cache when possible)
- Set reasonable timeouts (30 seconds for external calls)
- Return partial results if some data fails to load
- Log slow operations for debugging

## Async/Await Best Practices

- Define tools as `async def`
- Use `async with httpx.AsyncClient()` for HTTP
- Await all async operations
- Handle cancellation gracefully
- Don't block the event loop

## Version Management

- Use semantic versioning for API stability
- Document breaking changes in tool descriptions
- Support multiple API versions when possible
- Include version info in responses where relevant
