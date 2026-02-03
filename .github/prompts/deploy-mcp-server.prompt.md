---
description: "Deploy MCP server to production with validation and monitoring"
agent: "agent"
---

# Deploy MCP Server

## Your Role

You are a DevOps expert specializing in MCP server deployment. You ensure servers are production-ready, properly configured, and successfully deployed.

## Task

Prepare and deploy MCP server to production.

## Pre-Deployment Checklist

### 1. Code Quality

- [ ] All tests passing (pytest --cov, 80%+ coverage)
- [ ] No linting errors (pylint, black formatting)
- [ ] Type checking passes (mypy)
- [ ] Code reviewed and approved
- [ ] All tools have quality score 8+/10

### 2. Documentation

- [ ] All tools fully documented with examples
- [ ] README includes setup and usage instructions
- [ ] API reference complete
- [ ] Architecture documented
- [ ] Known limitations/constraints listed

### 3. Security

- [ ] No hardcoded secrets (all in env vars)
- [ ] API keys rotated if necessary
- [ ] .env file contains all required vars
- [ ] .env not committed to git
- [ ] Sensitive logs removed
- [ ] Rate limiting configured

### 4. Performance

- [ ] Load tested (can handle expected throughput)
- [ ] All tool response times acceptable (<5s with timeout)
- [ ] Memory usage is reasonable
- [ ] No resource leaks
- [ ] Timeout configurations appropriate

### 5. Reliability

- [ ] Error handling complete for all paths
- [ ] Retries configured for transient failures
- [ ] Circuit breakers for external APIs (if needed)
- [ ] Graceful degradation implemented
- [ ] No silent failures

### 6. Monitoring

- [ ] Logging configured (request/response logging)
- [ ] Error alerting configured
- [ ] Performance metrics captured
- [ ] Health check endpoint available
- [ ] Tool invocation metrics tracked

## Deployment Options

### Option 1: Local Deployment (for testing/demo)

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with actual API keys

# Start server
python src/server/index.py
```

### Option 2: Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/

ENV PYTHONUNBUFFERED=1
CMD ["python", "src/server/index.py"]
```

```bash
# Build and run
docker build -t mcp-weather:latest .
docker run -e OPENWEATHERMAP_API_KEY=your-key mcp-weather:latest
```

### Option 3: Prefect Horizon (Managed Hosting)

- Sign up at prefect.io
- Push code to GitHub
- Configure deployment via Prefect Cloud
- Automatic scaling and monitoring
- Free tier available

### Option 4: Cloud Functions (Serverless)

Adapt for AWS Lambda, Google Cloud Functions, etc.

## Configuration for Deployment

### Environment Variables Required

```bash
# OpenWeatherMap API
OPENWEATHERMAP_API_KEY=<your-api-key>

# Optional: Performance tuning
WEATHER_API_TIMEOUT=30
MAX_CONCURRENT_REQUESTS=10
```

### Deployment Validation

After deployment, verify:

- [ ] Server starts successfully
- [ ] Tools are discoverable (test tool discovery)
- [ ] Sample tool invocations work
- [ ] Error handling works (test with bad params)
- [ ] Logs are available
- [ ] Monitoring is recording metrics

## Deployment Validation Commands

```bash
# Test server connectivity
curl http://localhost:8000/health

# Test tool availability
mcp-cli list-tools

# Test tool invocation
mcp-cli invoke weather get_current_weather --lat 51.5 --lon -0.1

# Check logs
docker logs mcp-weather

# Monitor performance
docker stats mcp-weather
```

## Rollback Plan

If deployment fails:

1. Identify issue from logs/monitoring
2. Fix code or configuration
3. Re-deploy previous working version
4. Run validation tests again
5. Document the issue and fix

## Post-Deployment Steps

1. **Monitor**: Watch metrics and logs for first hour
2. **Test**: Run integration tests against live server
3. **Alert**: Ensure monitoring and alerting active
4. **Document**: Update deployment runbook with any custom steps
5. **Plan**: Schedule regular backups and updates

## Success Criteria

Deployment successful if:

- Server starts and runs for >5 minutes without errors
- All tools are discoverable and callable
- Response times acceptable
- Error handling works correctly
- Logs show normal operations
- Monitoring data is being collected
- Can handle at least 5 concurrent requests

## Rollback Procedure

If issues arise:

```bash
# Stop current deployment
docker stop mcp-weather

# Start previous version
docker run --name mcp-weather-v1 <previous-image>

# Investigate issue
# Check logs: docker logs mcp-weather
# Fix configuration or code
# Re-deploy with fixes
```

## Health Checks

Set up health endpoint to verify:

- Server is running
- External API connectivity (try a test call)
- Configuration is valid
- All required tools are loaded

## Maintenance Windows

- Schedule updates during low-traffic periods
- Communicate maintenance to users
- Perform backups before updates
- Have rollback plan ready
- Monitor after updates for issues

## Documentation for Operations Team

Provide:

- Deployment runbook
- Troubleshooting guide
- Monitoring dashboard instructions
- Alert escalation procedures
- Common issue resolutions
