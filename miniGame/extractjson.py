import re
import json

def extractJSON(text):
    # Take only the text from the 53rd index to the 17th to last index
    text = text[52:-16]
    # Replace any escaped newlines with actual newlines
    text = text.replace("\\n", "\n")
    print(text)
    # Convert the text to a JSON object
    text = json.loads(text)
    # Return the JSON object
    return text

text = ""

with open("extractablejson.txt", 'r') as file:
    text = file.read()

labels = extractJSON(text)

print(labels)