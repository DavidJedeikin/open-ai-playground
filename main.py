from openai import OpenAI
from prompt import SUPER_SOFTWARE_ENGINEER
import json


class OpenAIUsageEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)


client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    instructions="SUPER_SOFTWARE_ENGINEER",
    input="What is your favorite most elegant function?",
    temperature=0.7,
    top_p=0.9,
)

for i in range(10):
    # Print the usage details
    print("\nUsage details:")
    print(json.dumps(response.usage, indent=2, cls=OpenAIUsageEncoder))
