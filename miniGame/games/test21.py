
import random

class Game:
   def __init__(self):
       self.locations = {
           1: "Dairy Farm",
           2: "Fruit Farm",
           3: "Vegetable Farm",
           4: "Cotton Farm",
           5: "Sawmill"
       }

       self.quizzes = {
           "Dairy Farm": "What animal is typically found in a dairy farm? 1. Chicken 2. Cow",
           "Fruit Farm": "What kind of harvest is found in a fruit farm? 1. Wheat 2. Apples",
           "Vegetable Farm": "Can you name a typical vegetable? 1. Blueberry 2. Potato",
           "Cotton Farm": "Cotton is a 1. Fruit 2. Fiber",
           "Sawmill": "A sawmill is related to what type of product? 1. Wood 2. Vegetables"
       }

       self.answers = {
           "Dairy Farm": 2,
           "Fruit Farm": 2,
           "Vegetable Farm": 2,
           "Cotton Farm": 2,
           "Sawmill": 1
       }

   def play(self):
       print("Welcome to DailyHarvest, an agriculture-themed game. Make choices to gather items for your city apartment.")
       for i in range(1, 8):
           print(f"--------------- Day {i} -----------------")
           self.day()
           print("----------------------------------------")
       print("Congratulations! You have completed the game DailyHarvest.")

   def day(self):
       location = self.choose_location()
       print(f"You have chosen to visit {location}!")
       self.take_quiz(location)

   def choose_location(self):
       print("Here are the locations you can choose from:")
       for key, value in self.locations.items():
           print(f"{key}. {value}")
       return self.locations[int(input("Which location are you going to visit? (Enter the number corresponding to location): "))]

   def take_quiz(self, location):
       print("Now, let\'s test your knowledge.")
       print(self.quizzes[location])
       answer = int(input("What\'s your answer? (Enter the number corresponding to your answer): "))

       if answer == self.answers[location]:
           print("Correct! You\'ve learned something valuable today.")
       else:
           print("Oops, that\'s not correct. But you\'ll do better next time!")

game = Game()
game.play()
