# Generative Mini-Game Maker
- We have developed a tool to make **educational** mini-games utilizing Open AI's generative AI tools. 
- To get started, please run this command to install the required libraries:
	- ```pip install -r requirements.txt ```
- To run the script, please execute this command:
	- ```python ./minigame/assistants4.py```
- While running the script, you will be greeted with a prompt to enter in your learning standard, please enter in the learning standard that the game will be based off of
- Next, you will be prompted to enter the name of the minigame you want to create. This will be the name of the folder that will contain all the files for the game
- Once a game is successfully saved, you can run it by navigating to the folder of the name that you input beforehand and running
	- ```python run.py```
- Enjoy!

# Possible Errors and Fixes
- Every three seconds, the console will output a status update. If there has been no update for a while, it is possible that the API is not responding. In this case, please restart the script.