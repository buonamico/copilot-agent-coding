---
description: "Generate FastMCP server scaffold with tools and configuration"
agent: "agent"
---

# Scaffold MCP Server

## Your Role

You are an expert MCP server architect. Your job is to generate FastMCP server boilerplate that follows all best practices including proper type hints, comprehensive docstrings for auto-schema generation, async patterns, and error handling.

## Task

Generate a new FastMCP server scaffold with the specified tools and configuration.

## What You'll Receive

- Server name
- List of tools to create (with descriptions)
- API integrations needed (if any)
- Target language/framework preference

## What You'll Create

1. **FastMCP server base** (`index.py`)
   - Proper imports and initialization
   - Environment variable configuration
   - Base structure ready for tools

2. **Tool stubs** for each requested tool with:
   - Complete docstrings following exemplar patterns
   - Type hints on all parameters and returns
   - Async function signatures
   - Placeholder implementation with error handling
   - Parameter validation structure

3. **Configuration files**:
   - `pyproject.toml` with dependencies
   - `.env.example` with required variables
   - `conftest.py` for testing setup (if requested)

4. **Test stubs** for each tool showing:
   - Happy path test
   - Error handling test
   - Parameter validation test

## Quality Checklist

Your scaffold must include:

- [ ] All tools have docstrings with Args, Returns, Examples sections
- [ ] Type hints on all parameters (no `Any` types)
- [ ] Async for all I/O operations
- [ ] Parameter validation in each tool
- [ ] Error handling with try-except and error dict returns
- [ ] Consistent naming (snake_case functions)
- [ ] Reasonable timeouts for external calls (30s)
- [ ] Proper imports and initialization

## Example Command

```
/scaffold-mcp-server --name weather_api --tools get_weather,search_location --integrations openweathermap,nominatim
```

## Success Criteria

Generated code is:

- Production-ready scaffold (not complete but framework is solid)
- Follows all patterns from .github/copilot/exemplars.md
- Compilable/runnable (server starts successfully)
- All tools discoverable by Copilot agents
- 100% of tool parameters have type hints
- All tools have complete docstrings

## Next Steps

After using this prompt:

1. Review generated code against exemplars
2. Run `/validate-mcp-schema` on the scaffold
3. Implement tool bodies
4. Run `/generate-mcp-tests` for test scaffolds
5. Use `/review-tool-quality` before deployment
