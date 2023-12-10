
import pygame
import random
import os

# Initialize pygame
pygame.init()

# Constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 30

# Set up the display
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Farm Matching Game')
clock = pygame.time.Clock()

# Load images
image_filenames = [
    "cow.png", "pig.png", "chicken.png", "goat.png",
    "moo.png", "oink.png", "cluck.png", "bleat.png"
]

images = {}
for filename in image_filenames:
    image_name = os.path.splitext(filename)[0]  # Remove file extension
    images[image_name] = pygame.image.load(filename)

# Game state
game_state = {
    "score": 0,
    "matches_found": 0,
    "animal_sounds": {
        "cow": "moo",
        "pig": "oink",
        "chicken": "cluck",
        "goat": "bleat"
    },
    "revealed_tiles": {}
}

def draw_game():
    """
    Function to draw the game state on the screen.
    """
    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the revealed tiles on the screen
    for i, animal_name in enumerate(game_state["animal_sounds"].keys()):
        if animal_name in game_state["revealed_tiles"].values():
            animal_image = images[animal_name]
            sound_image = images[game_state["animal_sounds"][animal_name]]
            screen.blit(animal_image, (i * 140 + 50, 100))
            screen.blit(sound_image, (i * 140 + 50, 300))
    
    # Draw the score on the screen
    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {game_state["score"]}', True, (0, 0, 0))
    screen.blit(text, (30, 30))

    # Update the display
    pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_game()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
