
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30

# Colors
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Season Sort")

# Load images
image_dict = {
    "spring": pygame.image.load("plant (32).png"),   # Placeholder image for spring crops
    "summer": pygame.image.load("food (2).png"),      # Placeholder image for summer crops
    "fall": pygame.image.load("deco (3).png"),        # Placeholder image for fall crops
    "winter": pygame.image.load("furniture (83).png") # Placeholder image for winter crops
}

# Dictionary to store the game state
game_state = {
    "spring": [],   # List to store spring crops
    "summer": [],   # List to store summer crops
    "fall": [],     # List to store fall crops
    "winter": []    # List to store winter crops
}

# Function to draw the game
def draw_game():
    """
    Draws the current game state on the screen.
    """
    screen.fill(WHITE)  # Clear the screen with white color
    
    # Iterate over each season in the game state
    for index, season in enumerate(game_state):
        if game_state[season]:  # If season has crops
            # Iterate over each crop in the season
            for i, crop in enumerate(game_state[season]):
                image = image_dict[crop["name"]]                         # Get the image based on crop name
                screen.blit(image, (index * 200, i * 200))               # Draw the image on screen at appropriate position
    
    pygame.display.flip()   # Update the screen

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game
    draw_game()

    pygame.display.update()
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
