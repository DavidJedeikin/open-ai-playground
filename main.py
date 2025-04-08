from openai import OpenAI

from api_key import API_KEY

client = OpenAI(api_key=API_KEY)

PROMPT = "Write a one-sentence bedtime story about a unicorn."
response = client.responses.create(model="gpt-4o-mini", input=PROMPT)

print(response.output_text)
