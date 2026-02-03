# GitHub Copilot Configuration Demo

A baseline demonstration project showing how to configure GitHub Copilot for MCP (Model Context Protocol) server development using [FastMCP](https://gofastmcp.com/).

**Note**: This repository contains **configuration files only** - no actual implementation code. It serves as a template and reference for setting up GitHub Copilot to assist with MCP development.

## What's Included

### Custom Instructions (`.github/instructions/`)

Configuration files that guide Copilot on best practices:
- `mcp-development.instructions.md` - MCP server development focus guide
- `mcp-server.instructions.md` - Tool design patterns and FastMCP best practices
- `testing.instructions.md` - Testing strategies for MCP tools

### Prompt Files / Slash Commands (`.github/prompts/`)

Reusable slash commands for common MCP development tasks:
- `/scaffold-mcp-server` - Generate FastMCP server scaffold
- `/validate-mcp-schema` - Validate tool schemas for MCP compliance
- `/generate-mcp-tests` - Create comprehensive test suite
- `/review-tool-quality` - Code quality and security review
- `/document-mcp-tool` - Generate professional documentation
- `/deploy-mcp-server` - Plan and execute deployment

### Bundled Skills (`.github/skills/`)

Specialized skills that Copilot can invoke:
- `mcp-code-review/` - Comprehensive code audit skill
- `mcp-testing/` - Test generation and coverage management
- `mcp-documentation/` - Professional API documentation generation
- `mcp-deployment/` - Production deployment management

### Specialized Agents (`.github/agents/`)

Custom agents for specific MCP development needs:
- `mcp-architect.agent.md` - Architecture and design decisions
- `mcp-code-review.agent.md` - Code review specialist
- `mcp-documentation.agent.md` - Documentation specialist
- `mcp-testing.agent.md` - Testing specialist

### Reference Documentation (`.github/copilot/`)

Knowledge base for Copilot about MCP development:
- `tech-stack.md` - Technologies, versions, and dependencies
- `architecture.md` - MCP protocol concepts and patterns
- `exemplars.md` - High-quality code examples to emulate

### GitHub Templates (`.github/`)

- `ISSUE_TEMPLATE.md` - Issue template
- `PULL_REQUEST_TEMPLATE.md` - PR template
- `CODEOWNERS` - Code ownership configuration

## Quick Start

### 1. Scaffold a New MCP Server

Open Copilot Chat and use the slash command:

```
/scaffold-mcp-server --name my_weather_server --tools 3
```

Copilot will generate a complete FastMCP server structure based on the instructions and patterns in this repository.

### 2. Ask for Architecture Advice

Select the MCP Architect agent in Copilot Chat:

```
"Design an MCP server that combines weather and mapping APIs. 
What tools should I create and how should they interact?"
```

### 3. Generate Tests

After creating tools, generate comprehensive tests:

```
/generate-mcp-tests src/server/weather_tools.py
```

### 4. Review Code Quality

Get a detailed code review:

```
/review-tool-quality src/server/
```

## Project Structure

```
unboxing-ai-vscode-and-copilot-deep-dive-8016001/
├── .github/
│   ├── copilot-instructions.md          # Main Copilot configuration
│   ├── instructions/                    # Custom instruction files
│   │   ├── mcp-development.instructions.md
│   │   ├── mcp-server.instructions.md
│   │   └── testing.instructions.md
│   ├── copilot/                         # Reference documentation
│   │   ├── tech-stack.md
│   │   ├── architecture.md
│   │   └── exemplars.md
│   ├── prompts/                         # Slash command definitions
│   │   ├── scaffold-mcp-server.prompt.md
│   │   ├── validate-mcp-schema.prompt.md
│   │   ├── generate-mcp-tests.prompt.md
│   │   ├── review-tool-quality.prompt.md
│   │   ├── document-mcp-tool.prompt.md
│   │   └── deploy-mcp-server.prompt.md
│   ├── skills/                          # Bundled skills
│   │   ├── mcp-code-review/SKILL.md
│   │   ├── mcp-testing/SKILL.md
│   │   ├── mcp-documentation/SKILL.md
│   │   └── mcp-deployment/SKILL.md
│   ├── agents/                          # Specialized agents
│   │   ├── mcp-architect.agent.md
│   │   ├── mcp-code-review.agent.md
│   │   ├── mcp-documentation.agent.md
│   │   └── mcp-testing.agent.md
│   ├── ISSUE_TEMPLATE.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── CODEOWNERS
│   └── workflows/
│       └── main.yml
├── .vscode/
│   └── settings.json
├── CONTRIBUTING.md
├── EVENT_RUNDOWN.md
├── LICENSE
├── NOTICE
├── PROJECT_README.md
├── QUICK_REFERENCE.md
└── README.md
```

## How to Use This Repository

### As a Template

1. Clone or fork this repository
2. Customize the instruction files for your specific domain
3. Modify agents and prompts to match your workflow
4. Start building your MCP server with Copilot's help

### As a Reference

Browse the configuration files to understand:
- How to structure custom instructions for Copilot
- What makes effective slash commands
- How to create specialized agents
- Best practices for MCP tool development

### As a Learning Resource

Study the included documentation:
- [.github/copilot/architecture.md](.github/copilot/architecture.md) - Learn MCP concepts
- [.github/copilot/exemplars.md](.github/copilot/exemplars.md) - See quality code examples
- [.github/instructions/mcp-server.instructions.md](.github/instructions/mcp-server.instructions.md) - Understand tool patterns

## Key Features

### Custom Instructions

Copilot reads instruction files automatically and applies them to relevant contexts, ensuring consistent code quality and adherence to best practices.

### Slash Commands

Pre-built prompts accessible via `/command-name` syntax make common tasks one command away.

### Specialized Agents  
Custom agents provide expert-level assistance for architecture, testing, documentation, and code review.

### Knowledge Base

Reference documentation gives Copilot context about MCP protocols, FastMCP framework, and implementation patterns.

### Bundled Skills
Reusable skills can be invoked by Copilot to handle complex, multi-step tasks automatically.

## Suggested Prompts

### Using Custom Instructions

Try these prompts to see how custom instructions shape Copilot's responses:

**With `.github/instructions/mcp-server.instructions.md` active:**
```
What are best practices for error handling in MCP tools?
```
Notice how Copilot emphasizes async patterns, validation, and error dicts.

**With `.github/instructions/testing.instructions.md` active:**
```
What are best practices for error handling in MCP tools?
```
Notice how the same question now emphasizes testability and mock considerations.

### Using Slash Commands (Prompt Files)

**Scaffold a complete server:**
```
/scaffold-mcp-server --name weather_maps --tools 4
```
Generates a production-ready FastMCP server with 4 tool stubs, proper structure, type hints, and error handling.

**Validate tool schemas:**
```
/validate-mcp-schema src/server/weather_tools.py
```
Checks for MCP protocol compliance, missing docstrings, incorrect type hints, and provides actionable fixes.

**Generate comprehensive tests:**
```
/generate-mcp-tests src/server/index.py
```
Creates test suite with happy path, error cases, edge cases, and proper mocking for external APIs.

**Review code quality:**
```
/review-tool-quality get_current_weather
```
Performs comprehensive review with quality score, security analysis, and performance recommendations.

**Generate documentation:**
```
/document-mcp-tool get_current_weather
```
Creates professional API documentation with examples and usage guidance.

**Plan deployment:**
```
/deploy-mcp-server --environment production
```
Provides deployment planning, validation, and health check setup.

### Using Skills

**Request a security audit:**
```
Use the mcp-code-review skill to audit this tool for security
```
Skill analyzes code against quality, errors, security, performance, and documentation dimensions.

**Generate test coverage:**
```
Use the mcp-testing skill to create tests for this module
```
Creates comprehensive test suite with proper organization, mocking strategy, and coverage targets.

**Create documentation:**
```
Use the mcp-documentation skill to document this tool
```
Generates docstrings, README sections, and API reference documentation.

**Plan deployment:**
```
Use the mcp-deployment skill for pre-deployment validation
```
Performs validation, creates deployment plan, and sets up health checks.

### Using Specialized Agents

**Select the MCP Architect agent and ask:**
```
Design an MCP server that combines weather and mapping APIs. 
What tools should I create and how should they interact?
```
Get architecture-focused design recommendations and tool organization.

```
I need to design an MCP server handling real-time sensor data. 
How should I architect this for 1000 concurrent requests?
```
Get scalability and performance architecture guidance.

**Select the MCP Testing agent and ask:**
```
What test strategy should I use for tools that call external APIs?
```
Get specialized testing advice with mocking strategies and coverage goals.

**Select the MCP Documentation agent and ask:**
```
How should I document this MCP server for external developers?
```
Get documentation strategy including API reference, examples, and integration guides.

### Combining Features

**Architecture → Implementation → Testing workflow:**
1. Ask MCP Architect: "Design a weather/mapping MCP server"
2. Use handoff button to transition to Code Review
3. Implement with: `/scaffold-mcp-server --name weather_maps`
4. Generate tests: `/generate-mcp-tests`
5. Validate: `/review-tool-quality`
6. Document: `/document-mcp-tool`
7. Deploy: `/deploy-mcp-server`

**Context-aware development:**
```
Implement a weather tool with proper error handling
```
- With mcp-server instructions: Focus on MCP patterns, async, error dicts
- With testing instructions: Focus on testability, mocks, edge cases
- With architect agent: Focus on design and scalability considerations

## No Implementation Code

This repository intentionally contains **no actual source code** for MCP servers. Instead, it provides:
- Configuration for GitHub Copilot
- Instructions and patterns
- Templates and examples
- Documentation and references

Use these configurations to **generate** your own MCP server implementation with Copilot's assistance.

