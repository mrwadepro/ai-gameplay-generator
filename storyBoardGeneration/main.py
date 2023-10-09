import openai


testKey = "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"
openai.api_key = testKey

URL = "https://api.openai.com/v1/chat/completions/"

file = open("prompt.txt", "r")
prompt = ""
for a in file.readlines():
    prompt+= a + ""

file = open("course_description.txt", "r")
course = ""
for a in file.readlines():
    course+= a + ""

file = open("guidelines.txt", "r")
guidelines = ""
for a in file.readlines():
    guidelines+= a + ""

print (prompt)
completion = openai.ChatCompletion.create(
  model='gpt-4',
  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": course},
    {"role": "user", "content": guidelines},
  ]
)

print(completion.choices[0].message.content)