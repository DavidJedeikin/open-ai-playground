from openai import OpenAI
import json
from tools import tool_descriptions, get_weather, get_activity


def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    if name == "get_activity":
        return get_activity(**args)


def use_tools(tool_calls, input_msgs):
    for tool_call in tool_calls:
        # Use the tool
        if tool_call.type != "function_call":
            print(f"{tool_call.name} is not a function call")
            continue
        name = tool_call.name
        args = json.loads(tool_call.arguments)
        print(f"Request to use tool: {name}, with: {args}")
        result = call_function(name, args)

        # Update the input messages for the future call
        input_msgs.append(tool_call)
        input_msgs.append(
            {
                "type": "function_call_output",
                "call_id": tool_call.call_id,
                "output": str(result),
            }
        )


def get_recommendation(city) -> str:
    client = OpenAI()
    input_msgs = [
        {"role": "developer", "content": "You are a concise travel advisor"},
        {"role": "user", "content": f"What should I do in {city} today?"},
    ]

    while True:
        response = client.responses.create(
            model="gpt-4.1",
            input=input_msgs,
            tools=tool_descriptions,
        )
        if response.output[0].type == "function_call":
            use_tools(response.output, input_msgs)

        elif response.output[0].type != "output_text":
            return response.output_text

        else:
            print(f"Received an unhandled reponse: \n{response}")
            sys.exit(1)


if __name__ == "__main__":
    print(get_recommendation("Cape Town"))
