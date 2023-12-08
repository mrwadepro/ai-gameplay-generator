
# Import necessary pygame libraries
import pygame
import sys

# Set up your pygame environment and necessary variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the dimensions of each button
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50

# Define color constants
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define rectangles for health bars for the farm and the forest
FARM_RECT = pygame.Rect(50, 500, 300, 50)
FOREST_RECT = pygame.Rect(450, 500, 300, 50)

# Rectangles for buttons representing game actions
PLANT_BTN = pygame.Rect(50, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
IRRIGATE_BTN = pygame.Rect(250, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
FERTILIZERS_BTN = pygame.Rect(450, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
HARVEST_BTN = pygame.Rect(650, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

# Function to draw game window and its components
def draw_window():
    WIN.fill(WHITE)  # Fill the entire window with white

    # Draw health bars
    pygame.draw.rect(WIN, GREEN if FARM_RECT.width > 0 else RED, FARM_RECT)
    pygame.draw.rect(WIN, GREEN if FOREST_RECT.width > 0 else RED, FOREST_RECT)

    # Draw buttons for game actions
    pygame.draw.rect(WIN, GREEN, PLANT_BTN)
    pygame.draw.rect(WIN, GREEN, IRRIGATE_BTN)
    pygame.draw.rect(WIN, GREEN, FERTILIZERS_BTN)
    pygame.draw.rect(WIN, GREEN, HARVEST_BTN)

    # Add instruction text
    font = pygame.font.Font(None, 36)
    text = font.render("Click buttons to perform actions. Maintain farm and forest health.", 1, (10, 10, 10))
    WIN.blit(text, (50, 50))

# Function to decrease health bars
def decrease_health(rect, amount):
    rect.width = max(0, rect.width - amount)  # Decrease width but ensure it does not go below 0

# Function to increase health bars
def increase_health(rect, amount):
    rect.width = min(300, rect.width + amount)  # Increase width but ensure it does not go beyond 300

# Function encapsulating main game loop
def main():
    clock = pygame.time.Clock()  # Clock to regulate FPS

    # The game continues running until this is set false
    running = True

    while running:  # The game loop
        for event in pygame.event.get():  # Checking each event in the event queue
            if event.type == pygame.QUIT:  # If the 'Close Window' button was pressed
                running = False  # Terminate the game loop

            # Mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # Get x, y position of the mouse click
                # Action 'Plant' if the mouse clicked the 'Plant' button
                if PLANT_BTN.collidepoint(mouse_pos):  
                    increase_health(FARM_RECT, 10)  # Increase farm health
                    decrease_health(FOREST_RECT, 20)  # Decrease forest health
                # Similar actions for other buttons
                elif IRRIGATE_BTN.collidepoint(mouse_pos):
                    increase_health(FARM_RECT, 5)
                    decrease_health(FOREST_RECT, 20)
                elif FERTILIZERS_BTN.collidepoint(mouse_pos):
                    increase_health(FARM_RECT, 5)
                    decrease_health(FOREST_RECT, 35)
                elif HARVEST_BTN.collidepoint(mouse_pos):
                    increase_health(FARM_RECT, 15)
                    increase_health(FOREST_RECT, 10)

        draw_window()  # Draw the game window with the updated game state

        pygame.display.flip()  # Update the entire display

        clock.tick(60)  # Set FPS to 60

    pygame.quit()  # Quit game as soon as game loop ends

if __name__ == "__main__":
    pygame.init()  # Initialize all imported pygame modules
    main()  # Run the main function 
