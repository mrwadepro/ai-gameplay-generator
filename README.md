# Generative Mini-Game Maker
- We have developed a tool to make **educational** mini-games utilizing Open AI's generative AI tools. 
- To get started, please run this command to install the required libraries:
	- ```pip install -r requirements.txt ```
- After that, you have to set the OPENAI API key environment variable, without this, the script will not run. You can run the below command in your terminal
	-```export API_KEY=<api key>```
- To start running the script, please execute this command:
	- ```python ./miniGame/assistants4.py```
- While running the script, you will be greeted with a prompt to enter in your learning standard, please enter in the learning standard that the game will be based off of
- Next, you will be prompted to enter the name of the minigame you want to create. This will be the name of the folder that will contain all the files for the game
- Once a game is successfully saved, you can run it by navigating to the folder of the name that you input beforehand and running
	- ```python run.py```
- Enjoy!

# Possible Errors and Fixes
- Every three seconds, the console will output a status update. If there has been no update for a while, it is possible that the API is not responding. In this case, please restart the script.
- The games that are generated can possibly have bugs and/or not work. If this is ever encountered, please do a cursory pass through the source code the developer created to check for any obvious bugs. Sometimes its best to simply try again. This is something that we wish to improve in the future.