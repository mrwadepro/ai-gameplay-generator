
# Import the required modules
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Define the window's width and height
WIDTH = 800
HEIGHT = 600

# Define the dimensions of the button
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the images for the background and the button
# Replace the paths with the paths to your images
background = pygame.image.load('background.png')
button_img = pygame.image.load('button.png')

# Create a rectangle for the button
# The rectangle is defined by its top-left corner's coordinates and its dimensions
button_rect = pygame.Rect(50, 50, BUTTON_WIDTH, BUTTON_HEIGHT)

# Start the game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        # If the QUIT event is triggered (e.g. the window's X button is clicked), stop the game
        if event.type == QUIT:
            running = False

        # If the mouse button is clicked
        if event.type == MOUSEBUTTONDOWN:
            # If the mouse's position is within the button's rectangle
            # then the button was clicked
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    # Draw the background image at position (0,0)
    screen.blit(background, (0, 0))

    # Draw the button image at the top-left corner of the button rectangle
    screen.blit(button_img, button_rect.topleft)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
