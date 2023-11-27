import pygame
from pygame.locals import *
import pygame.font

# Game constants
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FRAMES_PER_SEC = 30
BUTTON_HEIGHT, BUTTON_WIDTH = 200, 70

class GameState:
    def __init__(self):
        # Start with initial values for farm and forest health
        self.farm_health = 100
        self.forest_health = 100
        # and so on...

    def update(self, action):
        if action == "conventional":
            # decrease forest health and increase farm health due to aggressive farming
            self.farm_health += 10
            self.forest_health -= 20
        elif action == "organic":
            # Increase or maintain both because of sustainable farming
            self.farm_health += 2
            self.forest_health -= 2

class GameButton:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)  # Draw the button's rectangle
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, 1, (10, 10, 10))  # Render the text
        textpos = text.get_rect(centerx=self.rect.centerx, centery=self.rect.centery)  # Center the text position
        surface.blit(text, textpos)  # Draw the text

def game_loop():
    pygame.init()
    clock = pygame.time.Clock()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Farm-o-Forest")
    
    # Load assets
    farm_img = pygame.image.load("farm.jpg")  # Farm image
    forest_img = pygame.image.load("farm.jpg")  # Forest image

    state = GameState()  # Initialize game state
    
    # Create some game buttons
    button_conventional = GameButton(10, 10, "Conventional Farming")
    button_organic = GameButton(10, BUTTON_HEIGHT + 20, "Organic Farming")
    # and so forth...
    
    running = True
    while running:
        action = None
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
               
            # Here's how you could handle a button click
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if button_conventional.rect.collidepoint(pos):
                    action = "conventional"
                    state.update(action)
                    action = None
                elif button_organic.rect.collidepoint(pos):
                    action = "organic"
                    state.update(action)
                    action = None

        # Render game state
        display_surface.fill((255, 255, 255))  # Fill background with white
        display_surface.blit(farm_img, (0, 0))  # Blit the farm image onto the display surface
        display_surface.blit(forest_img, (WINDOW_WIDTH // 2, 0))  # Blit the forest image onto the display surface
        
        # Render buttons
        button_conventional.draw(display_surface)
        button_organic.draw(display_surface)

        pygame.display.update()  # Display the next frame
        clock.tick(FRAMES_PER_SEC)
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()