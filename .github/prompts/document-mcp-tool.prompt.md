---
description: "Generate production-ready documentation for MCP tools"
agent: "agent"
---

# Document MCP Tool

## Your Role

You are a technical documentation expert specializing in API and tool documentation. You create clear, comprehensive documentation that helps users and agents understand how to use tools effectively.

## Task

Generate professional documentation for MCP tools.

## Documentation Artifacts

### 1. Enhanced Docstring

Upgrade tool docstring to include:

- Clear one-liner purpose
- Detailed description of what tool does and when to use
- All parameters with types, ranges, constraints, examples
- Return value structure with field descriptions
- Common use cases and examples
- Related tools or recommended combinations
- Error codes and their meanings
- Any rate limiting or performance notes

### 2. README Section

Create dedicated README section including:

- Tool overview and purpose
- Quick start example
- All parameters explained with examples
- Response structure with example response
- Error handling guide
- Best practices for using the tool
- Common mistakes to avoid

### 3. Usage Examples

Provide multiple examples:

- Basic usage (simple case)
- Advanced usage (with all parameters)
- Error handling example (how to handle errors)
- Integration example (using with other tools)

### 4. API Reference

Create reference card:

- Function signature
- Parameter table (name, type, required, constraints, description)
- Response table (field, type, description, example)
- Error codes table
- Execution time estimates

## Docstring Template

```python
@mcp.tool()
async def tool_name(param1: str, param2: int = 10) -> dict:
    """
    [One-liner: what the tool does]

    [Detailed description explaining when/why to use this tool]

    Args:
        param1: [Description of param1]
                [Valid values/constraints]
                Example: "London"
        param2: [Description of param2]
                (default: 10)

    Returns:
        Dictionary with fields:
        - field1 (type): Description of field1
        - field2 (type): Description of field2

    Example return:
        {
            "field1": "value",
            "field2": 123
        }

    Raises/Errors:
        API calls are wrapped in try-catch. No exceptions raised.
        Returns error dict: {"error": "message", "code": "ERROR_CODE"}
    """
```

## README Example Section

```markdown
## Tool: weather_for_location

Gets current weather for any location by name.

### Quick Start

\`\`\`
Ask Copilot: "What's the weather in Paris?"
Tool is called automatically with location_name="Paris"
Returns current temperature, conditions, humidity, wind speed
\`\`\`

### Parameters

- **location_name** (string, required): City or location name. Examples: "London", "New York", "Sydney"
- **units** (string, optional): "metric" for Celsius or "imperial" for Fahrenheit. Default: "metric"

### Response Structure
```

{
"location": "Paris, Île-de-France, France",
"temperature": 18.5,
"condition": "Partly Cloudy",
"humidity": 65,
"wind_speed": 3.2,
"units": "metric"
}

```

### Error Handling
If location not found:
```

{
"error": "Could not find location: Atlantis",
"searched_for": "Atlantis"
}

```

### Common Use Cases
1. User asks "Is it raining in Seattle?" → Tool searches, gets weather, reports conditions
2. User asks "Which city is warmer, London or Paris?" → Tool called twice for comparison
3. User asks "Plan a picnic in a good weather location" → Tool called for multiple cities
```

## API Reference Table Example

| Parameter     | Type   | Required | Constraints            | Example                 |
| ------------- | ------ | -------- | ---------------------- | ----------------------- |
| location_name | string | Yes      | Any city/address       | "Tokyo", "Eiffel Tower" |
| units         | string | No       | "metric" or "imperial" | "metric"                |

| Field       | Type   | Description                  | Example               |
| ----------- | ------ | ---------------------------- | --------------------- |
| location    | string | Matched location name        | "London, England, UK" |
| temperature | float  | Current temperature          | 15.2                  |
| condition   | string | Main weather condition       | "Cloudy"              |
| humidity    | int    | Relative humidity percentage | 72                    |

## Documentation Best Practices

- [ ] Clear, jargon-free language
- [ ] Examples for every parameter
- [ ] Multiple usage examples (basic → advanced)
- [ ] Error codes documented
- [ ] Related tools mentioned
- [ ] Performance info included
- [ ] Integration patterns shown
- [ ] Troubleshooting section

## Success Criteria

Generated documentation:

- Agents can understand how to use the tool
- Users can understand what tool does
- All parameters are explained with examples
- All error conditions are documented
- Integration with other tools is clear
- Can be used as complete API reference
- Is written at appropriate technical level
- Includes best practices and common patterns

## Output Files Generated

1. Updated tool docstring (copy-paste ready)
2. README.md section (can be merged into docs)
3. Usage examples (in docs/TOOL_NAME_examples.md)
4. API reference (in docs/API_REFERENCE.md)
