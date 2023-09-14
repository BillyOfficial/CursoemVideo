import os
import openai

key = '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'
openai.api_key = key

openai.api_key = os.getenv("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")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
