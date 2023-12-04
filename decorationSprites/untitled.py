import pygame
import random
import time

image_dict = {
    'forest_health': 'plant (32).png',
    'soil_health': 'furniture (40).png',
    'water_level': 'food (2).png',
    'farm_area': 'deco (36).png'
}

def draw_game(game_state):
    # Clear the screen
    screen.fill((0, 0, 0))  
    # Define the max health
    max_health = 100
    # Define the padding and initial positions
    padding = 20
    y_position = padding
    # Define the size of the bar
    bar_width = 200
    bar_height = 20

    # Retrieve images based on game state
    forest_img = get_img(image_dict['forest_health'])
    soil_img = get_img(image_dict['soil_health'])
    water_img = get_img(image_dict['water_level'])
    farm_img = get_img(image_dict['farm_area'])

    # Get the values from game state
    forest_health, soil_health, water_level, farm_area = game_state

    # Draw the images and health bars
    screen.blit(forest_img, (padding, y_position))
    pygame.draw.rect(screen, (34, 139, 34), (padding * 2 + icon_size, y_position, (forest_health / max_health) * bar_width, bar_height))
    
    y_position += icon_size + padding
    screen.blit(soil_img, (padding, y_position))
    pygame.draw.rect(screen, (160, 82, 45), (padding * 2 + icon_size, y_position, (soil_health / max_health) * bar_width, bar_height))

    y_position += icon_size + padding
    screen.blit(water_img, (padding, y_position))
    pygame.draw.rect(screen, (0, 191, 255), (padding * 2 + icon_size, y_position, (water_level / max_health) * bar_width, bar_height))

    y_position += icon_size + padding
    for i in range(farm_area):
        screen.blit(farm_img, ((padding * 2 + icon_size) * i + padding, y_position))

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
    i = pygame.image.load('images/All/'+filename)
    return pygame.transform.scale(i, (icon_size, icon_size))
import pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
import time

print("Welcome to the Eco-Farmer game!\
In this game, you will learn the impact of farming practices on nature.\
Your goal is to run a farm without causing much harm to the environment.")

# setup game variables
forest_health = 100
soil_health = 100
water_level = 100
farm_area = 1

# game actions
actions = ["Plant crops", "Expand farm", "Irrigate land", "Check environment status"]

# game loop
while True:
    print("\
--------------------------")
    print("Actions: ")
    for i, action in enumerate(actions):
        print(f"{i + 1}. {action}")
    choice = int(input("Choose action by typing a number: "))
    
    if choice == 1:
        # planting crops reduces soil health
        soil_health -= 5
        print("Crops planted. Soil health decreased by 5.")
    elif choice == 2:
        # expanding farm reduces forest health and increases farm area
        forest_health -= 10
        farm_area += 1
        print("Farm expanded. Forest health decreased by 10.")
    elif choice == 3:
        # irrigating land reduces water level
        water_level -= 15
        print("Water used for irrigation. Water level decreased by 15.")
    elif choice == 4:
        # checking environmental status
        print("\
===== Evironmental Status ========")
        print("Forest Health:", forest_health)
        print("Soil Health:", soil_health)
        print("Water Level:", water_level)
    else:
        print("Invalid action. Please, choose available ones.")

    
    # checking game over conditions
    if forest_health <= 0:
        print("*** Game Over: The forest has been completely destroyed! ***")
        break
    elif soil_health <= 0:
        print("*** Game Over: The soil has gone sterile! ***")
        break
    elif water_level <= 0:
        print("*** Game Over: The water level is too low! ***")
        break
    draw_game((forest_health,soil_health,water_level,farm_area))
    # let player rest between each action
    time.sleep(2)
