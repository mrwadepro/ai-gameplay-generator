
# Importing necessary modules
import pygame
from pygame.locals import *

# A class to define the initial farm's state and all possible actions
class Farm:
    def __init__(self):
        self.resources = 100  # Setting initial resources
        self.productivity = 50  # Setting initial productivity
        self.environment = 50  # Setting initial environment health
        self.font = pygame.font.Font(None, 35)  # Font for displaying text 

    # Function to display text on the screen
    def draw_text(self, text, surface, x, y):
        text_obj = self.font.render(text, 1, (0, 0, 0))  # Creating a text object
        text_rect = text_obj.get_rect()  # Creating a rectangle for the text
        text_rect.topleft = (x, y)  # Positioning the text
        surface.blit(text_obj, text_rect)  # Blitting the text onto the screen

    # Function to simulate planting of crop: resources decrease, productivity increases, environment health decreases
    def plant_crop(self):
        self.resources -= 10
        self.productivity += 20
        self.environment -= 5

    # Function to simulate raising of livestock: resources decrease, productivity increases, environment health decreases
    def raise_livestock(self):
        self.resources -= 20
        self.productivity += 30
        self.environment -= 15

    # Function to simulate fertilizing: resources decrease, productivity increases, environment health decreases
    def fertilize(self):
        self.resources -= 15
        self.productivity += 10
        self.environment -= 10

    # Function to simulate irrigation: resources decrease, productivity increases
    def irrigate(self):
        self.resources -= 10
        self.productivity += 10

    # Function to simulate conservation: resources decrease, environment health increases
    def conserve(self):
        self.resources -= 5
        self.environment += 20


# Initializing pygame and setting up the display window
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Farm Impact')

# Loading and scaling the background image
background = pygame.image.load('background.jpg').convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Loading and scaling the button images
buttons = {
    'plant_crop': pygame.image.load('crop.png').convert_alpha(),
    'raise_livestock': pygame.image.load('livestock.png').convert_alpha(),
    'fertilize': pygame.image.load('fertilizer.png').convert_alpha(),
    'irrigate': pygame.image.load('water_can.png').convert_alpha(),
    'conserve': pygame.image.load('conservation.png').convert_alpha()
}

for button in buttons.values():
    pygame.transform.scale(button, (100, 100))  # Assuming you want the buttons to be 100 * 100

# Setting the coordinates for button placement on the screen
BUTTONS_POS = [(10, 10), (10, 120), (10, 230), (10, 340), (10, 450)]  

# Creating an instance of the Farm class
farm = Farm()

# Game loop to continuously check for events 
while True:
    screen.blit(background, (0, 0))  # Blitting the background onto the screen
    for event in pygame.event.get():
        if event.type == QUIT:  # Quit the game if 'quit' event is detected
            pygame.quit()

        elif event.type == MOUSEBUTTONDOWN:  # Actions for mouse click events
            mouse_pos = event.pos
            if pygame.Rect(BUTTONS_POS[0], (100, 100)).collidepoint(mouse_pos):
                farm.plant_crop()
            elif pygame.Rect(BUTTONS_POS[1], (100, 100)).collidepoint(mouse_pos):
                farm.raise_livestock()
            elif pygame.Rect(BUTTONS_POS[2], (100, 100)).collidepoint(mouse_pos):
                farm.fertilize()
            elif pygame.Rect(BUTTONS_POS[3], (100, 100)).collidepoint(mouse_pos):
                farm.irrigate()
            elif pygame.Rect(BUTTONS_POS[4], (100, 100)).collidepoint(mouse_pos):
                farm.conserve()

    # Blitting buttons onto the screen
    for i, (button, pos) in enumerate(zip(buttons.values(), BUTTONS_POS)):
        screen.blit(button, pos)
    
    # Displaying text for resources, productivity and environment health   
    farm.draw_text('Resources: %d' % farm.resources, screen, 230, 100)
    farm.draw_text('Productivity: %d' % farm.productivity, screen, 230, 200)
    farm.draw_text('Environment: %d' % farm.environment, screen, 230, 300)

    pygame.display.flip()  # Updating the display
