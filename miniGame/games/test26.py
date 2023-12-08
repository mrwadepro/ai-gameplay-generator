
import pygame
import sys

from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

# Initializing the display window with a particular resolution.
screen = pygame.display.set_mode((screen_width, screen_height))

# Open an image file for the background and scale it to fit the screen.
background = pygame.image.load('farm.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height))

# Open an image file for the button and scale it to the desired size.
button_image = pygame.image.load('button.jpg')
button_width = 200
button_height = 70
button_image = pygame.transform.scale(button_image, (button_width, button_height))

# Set the font type and size.
font = pygame.font.Font(None, 36)

# Initialize the game state.
game_state = {"land": 30, "forest": 80, "water": 70, "crop_yield": 0}

# Define possible actions.
actions = ["Research", "Plant new crop", "Fertilize", "Pest control", "Harvest"]

# Define buttons and their positions on the screen.
buttons = [pygame.Rect((screen_width - button_width) // 2, i * button_height, button_width, button_height) for i in range(1, len(actions) * 2, 2)]

while True:
    for event in pygame.event.get():
        # If user clicked on the close icon, quit the game.
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # If user clicked on a mouse button, perform the corresponding action.
        if event.type == MOUSEBUTTONUP:
            for i, button in enumerate(buttons):
                # If the button is clicked, perform action and update the game state.
                if button.collidepoint(event.pos):
                    take_action(i)
                    print_state(game_state)  
                    check_game_state_conditions(game_state)

    # Draw the background on the screen.
    screen.blit(background, (0, 0))

    # Draw each button on the screen.
    for i, button in enumerate(buttons):
        screen.blit(button_image, (button.left, button.top))
        draw_text(actions[i], font, (255, 255, 255), screen, button.centerx, button.centery)

    # Update the visuals of the game.
    pygame.display.flip()
