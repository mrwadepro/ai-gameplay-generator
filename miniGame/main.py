import openai
import os
import pandas as pd

testKey = ""
openai.api_key = testKey

data = pd.read_csv('testData.csv')
del data["Domain"]

competencies = data["Competency Code"] + " " + data["Competency Description"]
competencies = dict.fromkeys(competencies)

microCompetencies = data["Micro-competency"] + " " + data["Micro-competency Description"]

prompt = "You will create educational minigames based off the learning goals. The learning goals are what the student should learn by the end of the minigame. Each learning goal has a minigame. Each learning goal will have sub-goals. The student must have learned every sub-goal associated with it's learning goal to be considered having learned the learning goal. Each sub-goal must be covered in a minigame. The minigame for each learning goal must include each subgoal. Each minigame should have the learning goal code, a description, game mechanics, and a game flow that goes through what the player does, and the sub-goals."
learningGoals = "The learning goals are: \n" + "\n".join(competencies.keys())
subGoals = "\nThe sub-goals are: \n" + "\n".join(microCompetencies)

response = openai.ChatCompletion.create(
  model='gpt-4',
  messages=[
    # {"role": "system", "content": "You are an educational mini-game generator."},
    {"role": "user", "content": prompt},
    {"role": "user", "content": learningGoals},
    {"role": "user", "content": subGoals}
  ]
)

file = open("response.txt","w")
file.write(response.choices[0].message.content)
