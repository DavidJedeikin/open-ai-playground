from openai.types.responses import tool
import requests


def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


def get_activity(city: str, temperature: int) -> str:
    if city == "Cape Town":
        return f"When it's {temperature} in {city}, you should go to Clifton beach"
    if city == "London":
        return f"When it's {temperature} in {city}, you should go to London fields"
    if city == "New York":
        return f"When it's {temperature} in {city}, you should go to Central Park"
    return f"I haven't heard of: {city}"


tool_descriptions = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for provided coordinates in celsius.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {"type": "number"},
                "longitude": {"type": "number"},
            },
            "required": ["latitude", "longitude"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_activity",
        "description": "Get the best activity to do in a city given the weather.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"},
                "temperature": {"type": "number"},
            },
            "required": ["city", "temperature"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]
