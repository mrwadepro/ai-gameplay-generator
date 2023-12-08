
# Import necessary modules and initialize Pygame
import pygame
import sys
import os
pygame.init()

# Set game window properties
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define some colors for use later
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Load the background image from the assets folder
bg = pygame.image.load(os.path.join('miniGame/games/farm.jpg'))

# Load icons for the organic farming and pesticide farming options, and scale them to appropriate size
organic_icon = pygame.transform.scale(pygame.image.load(os.path.join('decorationSprites/images/Plants/plant (1).png')), (50, 50))
pesticide_icon = pygame.transform.scale(pygame.image.load(os.path.join('decorationSprites/images/Plants/plant (5).png')), (50, 50))

# Initialize the in-game variables
gold = 100
environment = 100
turn = 0

# Prepare the font for text display
font = pygame.font.Font('freesansbold.ttf', 32)

# Function to check the end of the game after 5 turns
def game_over():
    if turn >= 5:
        return True
    return False

# Function to render and display text anywhere on the game screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Main game function
def game():
    running = True
    clock = pygame.time.Clock()

    # Define the clickable areas for the organic farming and pesticide farming options
    organic_button = pygame.Rect(100, 50, 200, 50)
    pesticide_button = pygame.Rect(500, 50, 200, 50)

    # Main game loop
    while running:
        screen.blit(bg, (0, 0)) # Draw the background on each frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check when the mouse is clicked on the organic farming button or pesticide farming button 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if organic_button.collidepoint(mouse_pos):
                    if gold >= 10:  # Check if player has enough gold
                        gold -= 10
                        environment += 10 # Increase the environmental health 
                    turn += 1
                elif pesticide_button.collidepoint(mouse_pos):
                    if gold >= 5: # Check if player has enough gold
                        gold -= 5
                        environment -= 10 # Decrease the environmental health
                    turn += 1

        # Check if the game is over after 5 turns and display the message
        if game_over():
            draw_text('GAME OVER', font, white, screen, 20, 20)
            pygame.display.update()
            pygame.time.wait(3000)
            running = False

        # Draw the in-game variable statistics
        draw_text('Gold: ' + str(gold), font, white, screen, 20, 570)
        draw_text('Environment: ' + str(environment), font, white, screen, 350, 570)
        draw_text('Turn: ' + str(turn), font, white, screen, 680, 570)

        pygame.draw.rect(screen, (0, 0, 0), organic_button)
        screen.blit(organic_icon, (organic_button.x + 75, organic_button.y + 10))

        pygame.draw.rect(screen, (0, 0, 0), pesticide_button)
        screen.blit(pesticide_icon, (pesticide_button.x + 75, pesticide_button.y + 10))

        pygame.display.update() # Update the display on each frame
        clock.tick(60) # Cap the game at 60 frames per second

# Run the game
if __name__ == "__main__":
    game()
