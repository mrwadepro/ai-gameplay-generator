from openai import OpenAI
import os
import time
import re

testKey = os.environ.get("API_KEY")
# in your terminal, please add export API_KEY=<api key>
def extract_and_save(text, filename):
    # Use a regular expression to find text between triple backticks
    match = re.search(r'```(?:Python|python)(.*?)```', text, re.DOTALL)
    
    if match:
        extracted_text = match.group(1).strip()
        pattern = r'\\n'

# Replace '\\n' with '\n' to format the string correctly
        converted_code = re.sub(pattern, '\n', extracted_text)
        # Save the extracted text to a file
        with open(filename, 'w') as file:
            file.write(converted_code)
    else:
        print("No triple backticks found in the input text.")

client = OpenAI()
game_designer = client.beta.assistants.retrieve("asst_ppZYfGoyh6ISVvD5XyLI6Ayu")
game_architect = client.beta.assistants.retrieve("asst_l5YcB1wAlvvVIjlzm4Ky7898")
game_developer = client.beta.assistants.retrieve("asst_WgenLJkZXnbFoIfFzpB80eiW")
software_developer = client.beta.assistants.retrieve("asst_TzwMLh8i8hnVeqDMl9iLhhd6")
code_reviewer = client.beta.assistants.retrieve("asst_bYXkG2Gy5i1s2lk3d6qpfU1C")
programmer = client.beta.assistants.retrieve("asst_CjPnvsrPNP3MtpTp2LrY61rd")
gui_maker = client.beta.assistants.retrieve("asst_gSQVFmwMH76z8lmh0sNgMNTX")
game_artist = client.beta.assistants.retrieve("asst_h9lHWtay2uBPdUW7HbjJWDJe")
documenter = client.beta.assistants.retrieve("asst_zXvoSL8n0hnvDYj3EQWTG1ls")

#Start with game designer
userInput = input("Please enter in your initial learning standard\n")
main_thread = client.beta.threads.create()
thread_message = client.beta.threads.messages.create(
  main_thread.id,
  role="user",
  content="Please design a simple mini game for this standard: " + userInput,
)

run = client.beta.threads.runs.create(
  thread_id= main_thread.id,
  assistant_id= game_designer.id
)

waitTime = 3
t = 0
while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    
    print(t, "game designer ", run.status)
    time.sleep(waitTime)
    t+= waitTime

#Then game architect
thread_message = client.beta.threads.messages.create(
  main_thread.id,
  role="user",
  content="Please use the above design ideas to create a simple game architecture according to your instructions.",
)

run = client.beta.threads.runs.create(
    thread_id= main_thread.id,
    assistant_id= game_architect.id
    )

while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    print(t , "game architect ",run.status)
    time.sleep(waitTime)
    t+= waitTime

#Then game developer
thread_message = client.beta.threads.messages.create(
  main_thread.id,
  role="user",
  content="Please use the above architecture and design to create a simple game according to your instructions.",
)

run = client.beta.threads.runs.create(
  thread_id= main_thread.id,
  assistant_id= game_developer.id
)

while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    print(t , "game developer ",run.status)
    time.sleep(waitTime)
    t+= waitTime

#Then gui maker
run = client.beta.threads.runs.create(
  thread_id= main_thread.id,
  assistant_id= gui_maker.id
)

while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    print(t , "gui maker ",run.status)
    time.sleep(waitTime)
    t+= waitTime

#Then programmer
thread_message = client.beta.threads.messages.create(
  main_thread.id,
  role="user",
  content="Use the above instructions to modify the code and create a working GUI game. Be sure to include art for the background and the buttons in the game.  The art and icons should all be scaled so that they show up as the correct size in the GUI.",
)

run = client.beta.threads.runs.create(
  thread_id= main_thread.id,
  assistant_id= programmer.id
)

while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    print(t , "programmer ",run.status)
    time.sleep(waitTime)
    t+= waitTime


#Then game artist
thread_message = client.beta.threads.messages.create(
  main_thread.id,
  role="user",
  content="Check the above code for any art that is needed and create the prompts as per your instructions.  Answer only with the prompts themselves, one per line.",
)

run = client.beta.threads.runs.create(
  thread_id= main_thread.id,
  assistant_id= game_artist.id
)

while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    print(t , "game artist ",run.status)
    time.sleep(waitTime)
    t+= waitTime

# Print the output of the game artist
thread_messages = client.beta.threads.messages.list(main_thread.id)
print(thread_messages.data[0].content)

#Then documenter
thread_message = client.beta.threads.messages.create(
  main_thread.id,
  role="user",
  content="Please document the code from earlier as per your instructions.",
)

run = client.beta.threads.runs.create(
    thread_id= main_thread.id,
    assistant_id= documenter.id
)

while (run.status != "completed"):
    run = client.beta.threads.runs.retrieve(
        thread_id= main_thread.id,
        run_id= run.id
    )
    print(t , "documenter ",run.status)
    time.sleep(waitTime)
    t+= waitTime



#print(run)
final_messages = client.beta.threads.messages.list(main_thread.id)
print(final_messages.data[0].content)
fileName = input("please enter game file name")
extract_and_save(str(final_messages.data[0].content[0]), fileName)






#thread = openai.
