# OpenAI Playground

[Full API Reference](https://platform.openai.com/docs/api-reference/responses)

## Save responses as json

```python
from openai import OpenAI
import json

client = OpenAI()


response = client.responses.create(
    model="gpt-4.1",
    instructions="You are a super engineer",
    input="What is your favorite most elegant function?",
    temperature=0.7,
    top_p=0.9,
)

# Save to file
with open("respnse.json", "w") as f:
    json.dump(response.model_dump()["output"], f, indent=4)
```

## Notes

- Prompts > 1024 tokens are automatically cached when dynamics parts are placed at the end.
- Use markdown or xml to help the model understand the structure of the prompt.
- Few-shot learning:
  - Models can learn from examples in the prompt
  - Typically, you will provide examples as part of a developer message
  - Try to show a diverse range of possible inputs with the desired outputs.

## Response API (Interesting values)

- `temperature` (Defaults to 1) What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both.
- `top_p` (Defaults to 1) An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.
