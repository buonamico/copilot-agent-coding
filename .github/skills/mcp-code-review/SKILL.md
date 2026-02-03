---
name: "mcp-code-review"
description: "Perform comprehensive code review of MCP tools focusing on security, reliability, and best practices"
---

# MCP Code Review Skill

## Overview

The MCP Code Review Skill performs expert-level code analysis on Model Context Protocol tools. It evaluates tool implementations against MCP best practices, security standards, performance benchmarks, and reliability patterns.

## When to Use This Skill

- **Scenario 1**: Reviewing tool code before committing to production
- **Scenario 2**: Auditing existing tools for security vulnerabilities
- **Scenario 3**: Ensuring code follows MCP and project standards
- **Scenario 4**: Mentoring developers on tool implementation best practices
- **Scenario 5**: Pre-deployment quality gates

## Key Capabilities

### 1. Code Quality Analysis

- Function complexity and size assessment
- Code duplication detection
- Logic clarity and maintainability evaluation
- Naming convention compliance
- Design pattern alignment with project standards

### 2. Error Handling Audit

- Comprehensive exception handling verification
- Error response consistency checking
- Error message quality assessment
- Failure path coverage analysis
- Recovery strategy evaluation

### 3. Security Review

- API key and credential handling verification
- Input validation completeness check
- Data sanitization assessment
- Sensitive data logging detection
- Rate limiting compliance verification

### 4. Performance Analysis

- API call optimization identification
- Timeout configuration review
- Resource efficiency evaluation
- Concurrency readiness assessment
- Response time benchmarking

### 5. Documentation Assessment

- Docstring completeness verification
- Type hint coverage analysis
- Example accuracy checking
- Parameter documentation quality
- Return structure clarity evaluation

## Quick Start

### Basic Usage

```
Request: "Review this MCP tool for code quality"
[Provide tool code or file path]
Skill: Analyzes code across all dimensions
Output: Detailed review with scores and recommendations
```

### Advanced Usage

```
Request: "Security audit of weather tools"
[Provide multiple tools]
Skill: Performs cross-tool security analysis
Output: Security findings with fix recommendations
```

## Review Dimensions

### Code Quality (Max 10 points)

- Size: Functions under 50 lines = +2
- Clarity: Logic is easy to follow = +2
- DRY: No code duplication = +2
- Naming: Clear, descriptive names = +2
- Comments: "Why" documented = +2

### Error Handling (Max 10 points)

- Coverage: All paths handled = +3
- Specificity: Specific exception types = +2
- Messaging: Descriptive error messages = +3
- Recovery: Graceful degradation = +2

### Security (Max 10 points)

- Secrets: Proper env var usage = +4
- Input: Comprehensive validation = +3
- Data: No sensitive leaks = +2
- Access: Rate limiting respected = +1

### Performance (Max 10 points)

- Efficiency: No N+1 API calls = +3
- Timeouts: Configured appropriately = +3
- Async: Proper async/await usage = +2
- Resources: No memory leaks = +2

### Documentation (Max 10 points)

- Docstrings: Complete and accurate = +3
- Types: All parameters typed = +3
- Examples: Present and correct = +2
- Clarity: Well-explained and jargon-free = +2

## Scoring System

| Score | Rating    | Status                            |
| ----- | --------- | --------------------------------- |
| 45-50 | Exemplary | Production-Ready ✓                |
| 40-44 | Excellent | Production-Ready with Suggestions |
| 35-39 | Good      | Ready with Improvements           |
| 30-34 | Fair      | Needs Attention                   |
| <30   | Poor      | Requires Rework                   |

## Review Output Format

```
CODE REVIEW REPORT: get_current_weather
═══════════════════════════════════════════════════════════════

📊 SCORES BY CATEGORY
  Code Quality ........... 9/10 ✅
  Error Handling ......... 8/10 ✅
  Security .............. 9/10 ✅
  Performance ............ 8/10 ✅
  Documentation .......... 9/10 ✅
  ─────────────────────────────────
  TOTAL SCORE ........... 43/50 ⭐⭐⭐⭐

✅ STRENGTHS
• Excellent error handling with specific exception types
• Comprehensive input validation (lat/lon ranges, units)
• Proper async/await implementation for I/O
• Clear, well-structured docstring with examples
• Appropriate timeout configuration (30s)

💡 IMPROVEMENTS (Non-blocking)
• Could add caching for frequently requested coordinates
• Error messages could include suggested fixes
• Consider adding retry logic for transient failures

⚠️ FINDINGS
[None - Code is production-ready]

🎯 RECOMMENDATION: APPROVED FOR PRODUCTION ✓
Quality gate passed. Ready to deploy.
```

## Findings Categories

### 🔴 Critical Issues (Must Fix)

- Security vulnerabilities
- Unhandled exceptions that propagate
- Missing required error handling
- Type safety violations
- Resource leaks

### 🟠 High Priority Issues

- Incomplete error handling
- Performance problems
- Missing validation
- Poor documentation
- Non-async I/O

### 🟡 Medium Priority

- Code style deviations
- Redundant logic
- Unclear naming
- Missing examples
- Optimization opportunities

### 🟢 Low Priority (Suggestions)

- Comment improvements
- Test coverage gaps
- Minor optimizations
- Documentation enhancements

## Examples of Review Findings

### Example 1: Strong Code

```
Finding: Parameter validation is comprehensive
Current: Validates lat (-90 to 90) and lon (-180 to 180)
Why Good: Prevents invalid API calls upfront
Score Impact: +3 points (Security and Reliability)
```

### Example 2: Improvement Area

```
Finding: Could use specific exception types
Current: Generic `except Exception` clause
Suggested: `except (httpx.TimeoutException, httpx.HTTPStatusError) as e`
Why Matters: Better error handling and debugging
Score Impact: -1 point (Error Handling)
Difficulty: Low (quick fix)
```

### Example 3: Critical Issue

```
Finding: API key in source code
Current: api_key = "sk_live_1234567890"  # Hardcoded
Critical: 🔴 SECURITY RISK
Suggested: api_key = os.getenv("OPENWEATHERMAP_API_KEY")
Impact: Code cannot be released until fixed
Score Impact: Tool fails security gate
```

## Best Practices Checked

### Tool Design

- [ ] Single responsibility principle
- [ ] Async for I/O operations
- [ ] Clear parameter validation
- [ ] Consistent return structures

### Error Handling

- [ ] All external calls wrapped in try-catch
- [ ] Specific exception types
- [ ] Error dict returns (never throw exceptions)
- [ ] Meaningful error context

### Documentation

- [ ] Complete docstrings
- [ ] Type hints on all parameters
- [ ] Return type documented
- [ ] Examples provided

### Security

- [ ] No hardcoded secrets
- [ ] Input validation comprehensive
- [ ] Rate limits respected
- [ ] Sensitive data not logged

## Common Issues Found & Fixes

| Issue              | Finding            | Fix                                            |
| ------------------ | ------------------ | ---------------------------------------------- |
| Generic exceptions | `except Exception` | Catch specific types: `httpx.TimeoutException` |
| Missing validation | No range checks    | Add: `if not (-90 <= lat <= 90): return error` |
| Sync I/O           | `requests.get()`   | Change to: `async with httpx.AsyncClient()`    |
| Hardcoded secrets  | `api_key = "..."`  | Use: `os.getenv("API_KEY")`                    |
| No docstring       | Missing docs       | Add complete docstring with Args, Returns      |

## Review Workflow

1. **Request Code Review**
   - Provide tool code or file path
   - Specify any special concerns

2. **Skill Analyzes** (5 dimensions)
   - Code Quality
   - Error Handling
   - Security
   - Performance
   - Documentation

3. **Skill Produces Report**
   - Dimension scores
   - Strengths highlighted
   - Issues categorized by priority
   - Specific recommendations
   - Overall score and recommendation

4. **Developer Takes Action**
   - Address critical issues
   - Implement improvements
   - Request follow-up review if desired

5. **Approve & Deploy**
   - Code passes quality gates
   - Ready for production
   - Deploy with confidence

## FAQ

**Q: What's the difference between this and linting?**
A: Linting checks syntax/style. This skill reviews architectural quality, error handling, security patterns, and reliability - the human aspects.

**Q: Can this catch bugs?**
A: Yes, patterns like missing error handling, unvalidated inputs, and sync I/O issues are caught.

**Q: How long does a review take?**
A: Typical tool review: 2-3 minutes. Comprehensive multi-tool audit: 5-10 minutes.

**Q: What if I disagree with feedback?**
A: Findings are suggestions based on MCP best practices. You can override with justification, but critical security findings must be addressed.

## Reference Materials

- `.github/copilot/exemplars.md` - Example implementations
- `.github/copilot/architecture.md` - Architecture patterns
- `.github/instructions/mcp-server.instructions.md` - Best practices
