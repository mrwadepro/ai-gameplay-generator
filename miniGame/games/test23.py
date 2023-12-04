
# Import the needed module to initialize pygame and to handle system-specific parameters and functions
import pygame 
import sys

# Initialize all imported pygame modules
pygame.init()

# Load your required graphic assets
# Replace "asset1.png" with the correct image file for the background 
bgImg = pygame.image.load("miniGame/games/farm.jpg")
# Replace "button.png" with the correct image file for the button 
buttonImg = pygame.image.load("decorationSprites/images/Tools/tool (1).png") 

# Class Button defines and initializes the button and its capabilities
class Button:
    def __init__(self, image, position):
        self.image = image  # Image for the button
        self.rect = self.image.get_rect(center=position)  # Generates a rectangle for positioning
        self.clicked = False  # Status of the button whether clicked or not

    # Function to draw the button image on the given screen position
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()  # Get position of the mouse

        # Check if the mouse pointer is on the button
        if self.rect.collidepoint(mouse_pos):
            # Check if the mouse is clicked while the pointer is on the button
            self.clicked = pygame.mouse.get_pressed()[0]

        # Draw the button on the screen
        screen.blit(self.image, self.rect)

    # Function to return the button status of whether it has been clicked or not
    def update(self):
        if self.clicked:
            return True

# Class Game defines and initializes the complete game and its function
class Game:
    def __init__(self, screen):
        self.screen = screen  # The main game screen
        self.farming_button = Button(buttonImg, (300, 200))  # The button for farming action
        self.farm_productivity = 100  # The productivity element of the farm
        self.environment_health = 100  # The health element of the environment
        self.years_passed = 0  # Game score or level
  
    # Function to run the complete game and handle its actions
    def run(self):
        # Use the game clock
        clock = pygame.time.Clock()

        # Game loop
        while True:
            # Handling the game events
            for event in pygame.event.get():
                # Quitting the game if the user wants to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Drawing the background
            self.screen.blit(bgImg, (0,0))
   
            # Load the font
            font = pygame.font.Font(None, 36)

            # Draw the game status on the screen
            self.screen.blit(font.render(f"Farm productivity: {self.farm_productivity}", True, (0, 0, 0)), (20, 20))
            self.screen.blit(font.render(f"Environment health: {self.environment_health}", True, (0, 0, 0)), (20, 60))
            self.screen.blit(font.render(f"Year: {self.years_passed}", True, (0, 0, 0)), (20, 100))
 
            # Draw the farming button
            self.farming_button.draw(self.screen)
         
            # Update the button, farm productivity, environmental health and year status if the button is clicked
            if self.farming_button.update():
                self.farm_productivity += 20
                self.environment_health -= 30
                self.years_passed += 1
                self.farming_button.clicked = False

            # Update the contents of the entire display
            pygame.display.flip()
            # Control the game speed
            clock.tick(60)

# Main function to start the game
def main():
    # Initialize the game screen size
    screen = pygame.display.set_mode((800, 600))
    game = Game(screen)
    game.run()

# Running the main function
if __name__ == "__main__":
    main()
