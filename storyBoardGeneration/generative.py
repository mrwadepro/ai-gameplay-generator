import openai
import base64
import os

testKey = "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"
openai.api_key = testKey
file = open("result.txt", "r")
#story = ""
for i,a in enumerate(file.readlines()):
    completion = openai.ChatCompletion.create(
    model='gpt-4',
    messages=[
        {"role": "system", "content": "your job is to provide concise, vivid descriptions of the given storyboard point to make an optimal prompt for an AI image generator like DALL-E. Make sure to make the prompt generates a panel with a top down view of a cute pixel art styled video game."},
        {"role" : "user", "content" : a}
    ]
    )
    story= completion.choices[0].message.content[0:1000]
    print(i, story)
    #breakpoint()
    images = openai.Image.create(
        prompt=story,
        n=3,
        size="1024x1024",
        response_format = "b64_json",
    )
    #print(type(images.data[0].b64_json))
    #breakpoint()
    path = './images/image_' + str(i)
    if not os.path.exists(path):
        os.mkdir(path)
        #print("Folder %s created!" % path)
    promptFile = open("./images/image_" + str(i) + "/prompt.txt", 'w')
    promptFile.write(a+"better prompt: " + story)
    
    for j,x in enumerate(images.data):  
        decodedData = base64.b64decode(x.b64_json)
        
        fileName = "./images/image_" + str(i) + "/image_"+ str(j) + ".png"
        imgFile = open(fileName, 'wb')
        imgFile.write(decodedData)
        imgFile.close()
        
        # newImage = openai.Image.create_edit(
        #     image=open(fileName, "rb"),
        #     prompt="pixel art version of the image",
        #     mask=open("./tt.png", "rb"),
        #     n=1,
        #     size="1024x1024",
        #     response_format = "b64_json",
        # )
        # newFileName = "./images/image_" + str(i) + "/pixel_image_"+ str(j) + ".png"
        # pimgFile = open(newFileName, 'wb')
        # pimgFile.write(base64.b64decode(newImage.data[0].b64_json))
        # pimgFile.close()
        # Write Image from Base64 File
        


