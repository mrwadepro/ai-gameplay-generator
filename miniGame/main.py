import openai
import os
import pandas as pd

testKey = os.environ.get("API_KEY")
openai.api_key = testKey

data = pd.read_csv('testData.csv')
data.dropna()
print(data)
del data["Domain"]

###### THIS IS GOING TO BE USER INPUT IN THE FRONT END ######
###### THIS IS INPUT IS ONLY FOR TESTING PURPOSES ########
setting = input("What setting would you like your game to be placed in?")

competencies = data["Competency Code"] + " " + data["Competency Description"]
competencies = dict.fromkeys(competencies)

microCompetencies = data["Micro-competency"] + " " + data["Micro-competency Description"]
microCompetencies.dropna(inplace=True)
prompt = "You will create educational minigames based off the learning goals. The minigame should have a " + setting + " setting. The learning goals are what the student should learn by the end of the minigame. Each learning goal has a minigame. Each learning goal will have sub-goals. The student must have learned every sub-goal associated with it's learning goal to be considered having learned the learning goal. Each sub-goal must be covered in a minigame. The minigame for each learning goal must include each subgoal. Each minigame should have the learning goal code, a description, game mechanics, a game flow that goes through what the player does, and the sub-goals."
learningGoals = "The learning goals are: \n" + "\n".join(competencies.keys())
print(microCompetencies)
subGoals = str("\nThe sub-goals are: \n" + "\n").join(microCompetencies)

response = openai.ChatCompletion.create(
  model='gpt-4',
  messages=[
    # {"role": "system", "content": "You are an educational mini-game generator."},
    {"role": "system", "content": prompt},
    {"role": "user", "content": learningGoals},
    {"role": "user", "content": subGoals},
    {"role" : "user", "content" : "Please format the learning goal code, description, game mechanics, game flow, and the sub-goals to be on seperate lines, each minigame should start with MINIGAME"}
  ]
)

file = open("response.txt","a")
file.write("prompt: "+prompt+"\n\n"+response.choices[0].message.content+ "\n\n") #appending to a response text file to look through the responses in the future
