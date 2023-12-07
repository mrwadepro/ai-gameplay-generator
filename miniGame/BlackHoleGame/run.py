
#Import libraries
import pygame
import sys
import os

# Initialize the Pygame module 
pygame.init()

# Set the size of the window or screen for display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
gameDisplay = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

# Set the window name 
pygame.display.set_caption('Black Hole Time Dilation Adventure')

# Load image files for the background, button and icon from disk. 
# Replace 'your_art_asset_path' with the path to your directory containing the images.
background = pygame.image.load(os.path.join('background.jpg'))
button = pygame.image.load(os.path.join('button.png')).convert_alpha()
icon = pygame.image.load(os.path.join('icon.png')).convert_alpha()

# Scale the loaded images to appropriate size.
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
button = pygame.transform.scale(button, (120, 60))  # size for a button
icon = pygame.transform.scale(icon, (100, 100))  # size for an icon

# Get the rectangle area of the icon and set its center position
icon_pos = icon.get_rect(center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//4))

# Define the main game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            # Exit event, clicking x on the window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Event to check if the button was clicked  
            if event.type == pygame.MOUSEBUTTONUP:
                if button.get_rect(topleft=(340, 250)).collidepoint(pygame.mouse.get_pos()): # If click position is within button area
                    print("Button clicked!") # Button action

        # Draw background image on the game display
        gameDisplay.blit(background, (0, 0))

        # Draw icon
        gameDisplay.blit(icon, icon_pos)

        # Draw button
        gameDisplay.blit(button, (340, 250))

        pygame.display.update() # Refresh display

# Call the game loop function to run the game
game_loop()
