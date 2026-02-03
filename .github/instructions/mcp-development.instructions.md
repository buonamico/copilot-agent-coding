---
description: "MCP server development focus guide"
applyTo: "**"
---

# MCP Development Focus

This project focuses on MCP (Model Context Protocol) server development using FastMCP, a modern Python framework for building protocol-compliant servers.

## Project Goals

- Demonstrate professional MCP server development practices
- Showcase integration of multiple APIs (OpenWeatherMap, OpenStreetMap)
- Model best practices in error handling, documentation, testing
- Serve as template for production MCP servers

## Development Workflow

### 1. Design Phase (Architect Agent)

- Plan tool architecture and schemas
- Define error handling strategy
- Validate against MCP protocol
- Plan scalability approach

### 2. Implementation Phase (Default Agent)

- Generate server scaffold
- Implement tools with best practices
- Integrate APIs
- Add comprehensive error handling

### 3. Testing Phase (MCP Testing Agent)

- Generate test suite
- Aim for 80%+ coverage
- Test error scenarios
- Verify performance

### 4. Review Phase (MCP Code Review Agent)

- Security audit
- Code quality assessment
- Error handling verification
- Performance analysis

### 5. Documentation Phase (MCP Documentation Agent)

- Generate API reference
- Create usage examples
- Document error codes
- Plan integration examples

### 6. Deployment Phase (MCP Deployment Agent)

- Pre-deployment validation
- Environment setup
- Health verification
- Monitoring setup

## Key Files & What They Do

### Server Code

- `src/server/index.py` - FastMCP server with 5 tools

### Configuration & Context

- `.github/copilot-instructions.md` - Project-wide guidelines
- `.github/instructions/` - Language/task-specific rules
- `.github/copilot/` - Reference documentation

### Development Helpers

- `.copilot/skills/` - 4 specialized skills for MCP development
- `prompts/` - 6 slash commands for common workflows
- `agents/` - MCP Architect specialized agent

## Using Copilot with This Project

### For Architecture Questions

Use MCP Architect Agent:

- Design decisions
- Scalability planning
- Protocol compliance

### For Code Generation

Use Prompts (slash commands):

- `/scaffold-mcp-server` - Generate server structure
- `/generate-mcp-tests` - Create test suite
- `/review-tool-quality` - Code review
- `/document-mcp-tool` - Generate docs
- `/validate-mcp-schema` - Protocol validation
- `/deploy-mcp-server` - Deployment planning

### For Specialized Help

Use Skills:

- `mcp-code-review` - Comprehensive code audit
- `mcp-testing` - Test generation and coverage
- `mcp-documentation` - Professional documentation
- `mcp-deployment` - Production deployment

### For General Development

Use Custom Instructions:

- `.github/instructions/mcp-server.instructions.md` - Tool design patterns
- `.github/instructions/testing.instructions.md` - Testing strategies

## Quality Standards

### Tool Quality

- All tools: 8+/10 quality score
- Documentation: 100% coverage
- Tests: 80%+ code coverage
- Performance: <5s response time

### Code Standards

- Type hints on all parameters
- Comprehensive error handling
- Clear variable naming
- Single responsibility per function

### Testing Standards

- Happy path + error cases
- Parameter validation tests
- Integration tests for combinations
- Performance benchmarks

### Documentation Standards

- Complete docstrings
- Usage examples
- API reference
- Integration guides
