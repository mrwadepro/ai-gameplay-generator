
# Relevant import statements
import pygame
import sys

# Setting up screen size and button properties
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 80, 40
FONT_SIZE = 32
FPS = 60

# Defining color templates
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initiating Pygame
pygame.init()

# Setting up game display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Green Thumb")
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)

# Defining Button Class
class Button:
    def __init__(self, x, y, text, callback):
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT) # rectangle for each button
        self.text = text # text to be displayed on the button
        self.callback = callback # callback function when the button is clicked

    # Method to draw button on Pygame window
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        text_surface = font.render(self.text, True, BLACK) # set the button text
        text_rect = text_surface.get_rect(center=self.rect.center) # position for the text
        screen.blit(text_surface, text_rect) # placing the text on button

    # On-click event handler
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

class Game:
    def __init__(self):
        # Initiate game parameters
        self.field_health = 100
        self.crop_yield = 0
        self.forest_health = 100
        self.soil_fertility = 100
        self.lake_purity = 100
        self.research_points = 100
        self.season = 0

        # Initialize all buttons
        self.buttons = [
            Button(20, 500, "Research", self.research),
            Button(120, 500, "Plant", self.plant_crops),
            Button(220, 500, "Fertilize", self.use_fertilizer),
            Button(320, 500, "Irrigate", self.irrigate),
            Button(420, 500, "Manage Waste", self.manage_waste),
        ]

    # Method to display text on screen
    def draw_text(self, text, x, y):
        text_surface = font.render(text, True, WHITE) # set the text
        text_rect = text_surface.get_rect(midtop=(x, y)) # position on screen
        screen.blit(text_surface, text_rect) # placing the text on screen

    # Method to draw objects on the Pygame window
    def draw(self):
        screen.fill(BLACK) # screen color
        self.draw_text(f"Season {self.season}", SCREEN_WIDTH // 2, 20) # display season
        # Display game parameters
        self.draw_text(f"Field Health: {self.field_health}", 20, 100)
        self.draw_text(f"Crop Yield: {self.crop_yield}", 20, 140)
        self.draw_text(f"Forest Health: {self.forest_health}", 20, 180)
        self.draw_text(f"Soil Fertility: {self.soil_fertility}", 20, 220)
        self.draw_text(f"Lake Purity: {self.lake_purity}", 20, 260)
        for button in self.buttons:
            button.draw(screen)

    # Event handler for each button
    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    # Method to update game state
    def update(self):
        if self.season >= 20:
            print(f"Final Score: {self.field_health + self.crop_yield + self.forest_health + self.soil_fertility + self.lake_purity}")
            sys.exit()

    # Game action methods: research, planting crops, fertilizer usage, irrigation and waste management
    def research(self):
        self.research_points -= 5
        self.field_health += 5
        self.forest_health += 5
        self.soil_fertility += 5
        self.lake_purity += 5
        self.season += 1

    def plant_crops(self):
        self.field_health -= 20
        self.crop_yield += 50
        self.season += 1

    def use_fertilizer(self):
        self.field_health += 10
        self.forest_health -= 5
        self.soil_fertility -= 5
        self.lake_purity -= 5
        self.season += 1

    def irrigate(self):
        self.field_health += 5
        self.soil_fertility += 5
        self.season += 1

    def manage_waste(self):
        self.lake_purity += 5
        self.season += 1

# Main function with game loop
def main():
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_event(event)

        game.update()
        game.draw()
        # Updating the display and maintaining the game speed
        pygame.display.flip()
        clock.tick(FPS)

# Start the Pygame
if __name__ == "__main__":
    main()

