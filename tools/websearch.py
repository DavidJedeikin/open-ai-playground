from openai import OpenAI

client = OpenAI()

response_with = client.responses.create(
    model="gpt-4.1",
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
)

response_without = client.responses.create(
    model="gpt-4.1", input="What was a positive news story from today?"
)

print("<<<<<<<<<<<<<<<<<<< With websearch >>>>>>>>>>>>>>>>>>")
print(response_with.output_text)

print("\n\n")
print("<<<<<<<<<<<<<<<<<<< Without websearch >>>>>>>>>>>>>>>>>>")
print(response_without.output_text)
