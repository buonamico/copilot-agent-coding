---
description: "High-quality MCP tool examples to emulate"
---

# Code Exemplars

## High-Quality Tool Examples

These are reference implementations showing the quality bar for MCP tools in this project.

### Exemplar 1: The Complete Tool (get_current_weather)

```python
@mcp.tool()
async def get_current_weather(lat: float, lon: float, units: str = "metric") -> dict:
    """
    Get current weather for coordinates.

    Fetches real-time weather data from OpenWeatherMap API
    for any latitude/longitude on Earth.

    Args:
        lat: Latitude coordinate, range -90 to 90 (required)
        lon: Longitude coordinate, range -180 to 180 (required)
        units: Temperature unit system (default: metric)
               - "metric": Celsius, m/s
               - "imperial": Fahrenheit, mph

    Returns:
        Dictionary containing:
        - location: City name from API
        - temperature: Current temperature in specified units
        - feels_like: "Feels like" temperature
        - condition: Main weather condition (e.g., "Cloudy")
        - description: Detailed weather description
        - humidity: Relative humidity percentage (0-100)
        - pressure: Atmospheric pressure (hPa)
        - wind_speed: Wind speed in specified units
        - units: Units used in response

    Example return:
        {
            "location": "London",
            "temperature": 15.2,
            "feels_like": 14.8,
            "condition": "Cloudy",
            "description": "overcast clouds",
            "humidity": 72,
            "pressure": 1013,
            "wind_speed": 3.5,
            "units": "metric"
        }
    """
    # Validate parameters
    if not (-90 <= lat <= 90):
        return {"error": "Latitude must be between -90 and 90", "provided": lat}
    if not (-180 <= lon <= 180):
        return {"error": "Longitude must be between -180 and 180", "provided": lon}
    if units not in ["metric", "imperial"]:
        return {"error": "Units must be 'metric' or 'imperial'", "provided": units}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{WEATHER_BASE_URL}/weather",
                params={"lat": lat, "lon": lon, "units": units, "appid": WEATHER_API_KEY},
                timeout=30
            )
            response.raise_for_status()
            data = response.json()

            # Parse and structure response
            return {
                "location": data.get("name", "Unknown"),
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "condition": data["weather"][0]["main"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "wind_speed": data["wind"]["speed"],
                "units": units
            }
    except httpx.TimeoutException:
        return {
            "error": "Weather API request timed out",
            "code": "TIMEOUT",
            "retry": True
        }
    except httpx.HTTPStatusError as e:
        return {
            "error": f"Weather API returned error {e.response.status_code}",
            "code": "API_ERROR",
            "status_code": e.response.status_code
        }
    except Exception as e:
        return {
            "error": f"Failed to fetch weather: {str(e)}",
            "code": "UNKNOWN_ERROR",
            "lat": lat,
            "lon": lon
        }
```

**Why this is exemplary:**

- ✅ Complete docstring with all details
- ✅ Type hints on parameters and return
- ✅ Input validation with meaningful errors
- ✅ Structured success response
- ✅ Specific error handling (timeout, HTTP errors, generic)
- ✅ Helpful error context (code, retry flag, coordinates)
- ✅ Async for I/O
- ✅ Timeout configuration (30s)
- ✅ Consistent field naming (snake_case)
- ✅ Returns dict, never raises exceptions

### Exemplar 2: The Search Tool (search_location)

```python
@mcp.tool()
async def search_location(query: str, limit: int = 5) -> list:
    """
    Search for location coordinates by name or address.

    Uses OpenStreetMap Nominatim API to find geographic coordinates
    for place names and addresses.

    Args:
        query: Location name or address to search for
               Examples: "London", "Eiffel Tower", "10 Downing Street, London"
               (required)
        limit: Maximum number of results to return, range 1-50
               (default: 5)

    Returns:
        List of matching locations, each containing:
        - name: Full display name/address from OpenStreetMap
        - latitude: Geographic latitude
        - longitude: Geographic longitude
        - type: Location type (city, county, etc.)
        - importance: Relevance score (0-1, higher = more important)

    Example return:
        [
            {
                "name": "London, England, United Kingdom",
                "latitude": 51.5085,
                "longitude": -0.1257,
                "type": "city",
                "importance": 0.9
            },
            {
                "name": "London, Ohio, United States",
                "latitude": 39.8859,
                "longitude": -83.4477,
                "type": "city",
                "importance": 0.3
            }
        ]
    """
    # Validate parameters
    if not query or len(query.strip()) == 0:
        return [{"error": "Query cannot be empty"}]
    if not isinstance(limit, int) or limit < 1 or limit > 50:
        return [{"error": "Limit must be integer between 1 and 50", "provided": limit}]

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{OSM_BASE_URL}/search",
                params={"q": query, "format": "json", "limit": limit},
                headers={"User-Agent": "MCP-Weather-Demo/1.0"},
                timeout=30
            )
            response.raise_for_status()
            results = response.json()

            # Transform results to consistent format
            return [
                {
                    "name": r.get("display_name", ""),
                    "latitude": float(r["lat"]),
                    "longitude": float(r["lon"]),
                    "type": r.get("type", ""),
                    "importance": r.get("importance", 0)
                }
                for r in results
            ]
    except httpx.TimeoutException:
        return [{"error": "Search API timed out", "code": "TIMEOUT"}]
    except Exception as e:
        return [{"error": f"Search failed: {str(e)}", "query": query}]
```

**Why this is exemplary:**

- ✅ Clear purpose and use cases in docstring
- ✅ Parameter constraints documented (1-50 range)
- ✅ Example return values shown
- ✅ Validation with meaningful feedback
- ✅ Proper User-Agent header for politeness
- ✅ Type conversion (float for coordinates)
- ✅ Consistent response structure across all results
- ✅ Handles edge cases (empty query, invalid limit)

### Exemplar 3: The Composite Tool (weather_for_location)

```python
@mcp.tool()
async def weather_for_location(location_name: str, units: str = "metric") -> dict:
    """
    Get current weather for a location by name.

    Combines location search and weather retrieval in a single
    convenient tool for user-friendly queries like
    "What's the weather in Paris?"

    Args:
        location_name: Name of location to get weather for
                      (e.g., "London", "Paris, France", "Tokyo")
        units: Temperature units - "metric" or "imperial" (default: metric)

    Returns:
        Combined response from search and weather:
        - All fields from get_current_weather (temperature, condition, etc.)
        - Plus searched_as: The original search query
        - Plus location: The matched location name

    Example:
        Input: location_name="London"
        Output: {
            "location": "London",
            "temperature": 15.2,
            "condition": "Cloudy",
            "description": "overcast clouds",
            "humidity": 72,
            "pressure": 1013,
            "wind_speed": 3.5,
            "units": "metric",
            "searched_as": "London"
        }
    """
    # Search for location first
    locations = await search_location(location_name, limit=1)

    # Check for search errors
    if not locations or "error" in locations[0]:
        return {
            "error": f"Could not find location: {location_name}",
            "code": "LOCATION_NOT_FOUND",
            "searched_for": location_name
        }

    # Get weather for first result
    loc = locations[0]
    weather = await get_current_weather(
        loc["latitude"],
        loc["longitude"],
        units
    )

    # Check for weather API errors
    if "error" in weather:
        return weather

    # Combine results
    return {
        **weather,
        "searched_as": location_name
    }
```

**Why this is exemplary:**

- ✅ Composes smaller tools effectively
- ✅ Handles error from composed tools gracefully
- ✅ Clear use case for agents
- ✅ Returns predictable structure
- ✅ Documents the combination strategy

## Patterns to Follow

### Pattern: Input Validation First

```python
# Always validate before API calls
if not validate(param):
    return {"error": "validation message"}

# Then proceed with I/O
result = await expensive_operation()
```

### Pattern: Consistent Error Responses

```python
# All errors have structure
{"error": "descriptive message", "code": "ERROR_CODE", "context": "relevant data"}
```

### Pattern: Type Conversion

```python
# Convert strings from APIs to proper types
"latitude": float(api_response["lat"]),
"temperature": int(api_response["temp"])
```

### Pattern: Default Values

```python
# Use sensible defaults
def search_location(query: str, limit: int = 5):  # Default to 5 results
def get_current_weather(lat: float, lon: float, units: str = "metric"):  # Default to metric
```

## Anti-Patterns to Avoid

### ❌ Missing or Vague Docstrings

```python
# BAD
async def tool(a, b):
    return result

# GOOD
async def tool(a: int, b: str) -> dict:
    """Clear description of what, when, and how."""
```

### ❌ Raising Exceptions

```python
# BAD
if error:
    raise ValueError("Something went wrong")

# GOOD
if error:
    return {"error": "Descriptive error message"}
```

### ❌ Inconsistent Error Handling

```python
# BAD - Sometimes returns error dict, sometimes raises
if param_error:
    return {"error": "..."}
if api_error:
    raise Exception("...")

# GOOD - Always return error dict
if param_error:
    return {"error": "..."}
try:
    result = await api_call()
except Exception:
    return {"error": "..."}
```

### ❌ Synchronous I/O

```python
# BAD
def get_weather(lat, lon):  # Not async
    response = requests.get(...)  # Blocking

# GOOD
async def get_weather(lat: float, lon: float) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(...)
```

### ❌ No Parameter Validation

```python
# BAD
async def get_weather(lat: float, lon: float) -> dict:
    # Directly use lat, lon in API call
    response = await client.get(..., params={"lat": lat, "lon": lon})

# GOOD
async def get_weather(lat: float, lon: float) -> dict:
    if not (-90 <= lat <= 90):
        return {"error": "Invalid latitude"}
    if not (-180 <= lon <= 180):
        return {"error": "Invalid longitude"}
    response = await client.get(...)
```

### ❌ Inconsistent Return Structures

```python
# BAD - Different structure for different calls
return {"temp": 20}  # First call
return {"temperature": 20, "condition": "sunny"}  # Second call

# GOOD - Consistent structure
return {"temperature": 20, "condition": "sunny", "humidity": 65, ...}
```
