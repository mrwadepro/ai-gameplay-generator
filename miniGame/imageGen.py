from openai import OpenAI
import base64
client = OpenAI()


def getImage(prompt, filename):
    response = client.images.generate(
    model="dall-e-3",
    prompt= prompt,
    n=1,
    size="1024x1024",
    response_format="b64_json"
    ) 
    imgdata = base64.b64decode(response.data[0].b64_json)
    #filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)


getImage("a small tree", "tree.jpg")