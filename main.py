from openai import OpenAI

client = OpenAI()

PROMPT = "Write haiku about king david"

response = client.responses.create(model="gpt-4o-mini", input=PROMPT)

print(response.output_text)
