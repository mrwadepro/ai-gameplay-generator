import pygame
import random

###INSERT CODE HERE

def draw_game(game_state):

###
    pygame.display.flip()

# Initialize Pygame
pygame.init()
# Define game window size
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# Define game window size
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
# Define icon sizes
icon_size = 60
icon_size = 60
image_dir = "images/All/"
def get_img(filename):
    i = pygame.image.load(filename)
    return pygame.transform.scale(i, (icon_size, icon_size))
import pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


import random

class Game:

    def __init__(self):
        self.regions = {"Coastal Plains": "peaches", "Piedmont": "blueberries", "Appalachian Mountains": "apples"}
        self.user_region = None
        self.user_crop = None
        draw_game(self)

    def intro_message(self):
        print("Welcome to Harvest Time in Georgia!")
        print("In this game, you will manage a farm in a region of Georgia.")
        print("Your goal is to produce the appropriate crops for your region.")
        draw_game(self)

    def choose_region(self):
        region = input("Choose your region: Coastal Plains, Piedmont, or Appalachian Mountains.\
")
        if region in self.regions:
            self.user_region = region
            self.user_crop = self.regions[region]
            print(f"You chose {region}. You will be growing {self.user_crop}.")
        else:
            print("Please choose a valid region.")
            self.choose_region()
        draw_game(self)

    def start_season(self):
        environmental_factor = random.choice(["rain", "drought", "pests", "perfect conditions"])
        print(f"This season, your farm is experiencing {environmental_factor}.")

        if environmental_factor == "rain":
            print("Your crops are drowning! Reduce watering.")
        elif environmental_factor == "drought":
            print("Your crops are thirsty! Increase watering.")
        elif environmental_factor == "pests":
            print("Your crops are being eaten by pests! Use some natural repellents.")
        elif environmental_factor == "perfect conditions":
            print("The conditions are perfect! Your crops are thriving.")
            draw_game(self)
    
    def end_season(self):
        market_price = random.randint(1,10)
        print(f"The market price for {self.user_crop} is ${market_price} per kilo.")
        yield_kilos = random.randint(10,20)
        print(f"You have yielded {yield_kilos} kilos.")
        earnings = market_price * yield_kilos
        print(f"You have earned a total of ${earnings} this season.")
        draw_game(self)

game = Game()
game.intro_message()
game.choose_region()
game.start_season()
game.end_season()
