from openai import OpenAI
import json
from pydantic import BaseModel
import time

client = OpenAI()


class Person(BaseModel):
    name: str
    age: int
    profession: str
    height: float
    is_married: bool


for i in range(10):
    ts = time.time()
    person = client.responses.parse(
        model="gpt-4.0",
        input=[
            {"role": "system", "content": "You are a playwright"},
            {
                "role": "user",
                "content": "Invent a person",
            },
        ],
        text_format=Person,
        temperature=0.2,
    )
    print("=========================================================")
    print(f"Introducting: {person.output_parsed.name},  Time taken: {time.time() - ts}")
    print(json.dumps(person.output_parsed.model_dump(), indent=4))
