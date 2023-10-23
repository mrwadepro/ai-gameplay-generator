import openai


testKey = "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"
openai.api_key = testKey

URL = "https://api.openai.com/v1/chat/completions/"

file = open("decorationSprites/prompt.txt", "r")
prompt = ""
for a in file.readlines():
    prompt+= a + ""

print (prompt)
completion = openai.ChatCompletion.create(
  model='gpt-4',
  messages=[
    {"role": "system", "content": prompt}
  ]
)

print(completion.choices[0].message.content)