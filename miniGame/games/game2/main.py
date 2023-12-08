
# Import the necessary module for game development.
import pygame

# Initialize the pygame module.
pygame.init()

# Define some colors that we will use later.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create a game display that is 500 pixels by 500 pixels.
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set a title for the game window.
pygame.display.set_caption("Eco Farmer")

# Create a font object for rendering text.
font = pygame.font.Font(None, 32)

# Create text surface objects for each button.
text_conventional = font.render("1. Conventional", True, WHITE, BLUE)
text_organic = font.render("2. Organic", True, WHITE, GREEN)
text_integrated = font.render("3. Integrated", True, WHITE, RED)
text_permaculture = font.render("4. Permaculture", True, WHITE, BLACK)

# Enter the game loop, which will run as long as the game is active.
while True:

    # Clear the screen to white.
    display_surface.fill((WHITE))

    # Draw a button for each farming mode.
    pygame.draw.rect(display_surface, BLUE, (50, 100, 200, 50))  # Conventional button
    display_surface.blit(text_conventional, (60, 110))

    pygame.draw.rect(display_surface, GREEN, (50, 200, 200, 50))  # Organic button
    display_surface.blit(text_organic, (60, 210))

    pygame.draw.rect(display_surface, RED, (50, 300, 200, 50))  # Integrated button
    display_surface.blit(text_integrated, (60, 310))

    pygame.draw.rect(display_surface, BLACK, (50, 400, 200, 50))  # Permaculture button
    display_surface.blit(text_permaculture, (60, 410))

    # Event loop to capture game events such as pressing the close button ('X') on the window.
    for event in pygame.event.get():

        # If the close button was pressed, exit the game.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the game display.
    pygame.display.update()
