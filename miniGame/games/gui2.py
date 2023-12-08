
import pygame
import sys

pygame.init()

# window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600 

# color settings
WHITE = (255, 255, 255)

# Creating a display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Define a class for the game button
class Button:
    def __init__(self, x, y, image):
        self.image = pygame.image.load(image)  # Load the image for the button
        self.rect = self.image.get_rect()  # Get the rectangular area (rect object) of the image
        self.rect.topleft = (x, y)  # Set the position of the rect object

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the button image on the screen

# Define a class for the game state
class GameState:
    def __init__(self):
        # Initializing game variables
        self.farmland_state = 0  # Initially no agricultural practice
        self.environment_state = {"forest": 100, "soil": 100, "water": 100}  # Initialize the health of forest, soil and water
        self.balance_indicator = 100  # Initialize the balance indicator
        self.game_status = "running"  # Initial status of the game is running

    def update_game(self, farmland_state, environment_state):
        self.farmland_state = farmland_state  # Update the agricultural practice
        for key in self.environment_state:
            self.environment_state[key] -= environment_state[key]  # Update the health values for forest, soil and water
            self.balance_indicator -= environment_state[key]  # Update the balance indicator
        # If the balance indicator becomes less than or equal to zero or greater than or equal to 200, finish the game
        if self.balance_indicator <= 0 or self.balance_indicator >= 200:
            self.game_status = "finished"

def main():
    clock = pygame.time.Clock()  # Set up a clock to control the frame rate
    game = GameState()
    bg = pygame.image.load(\'background.png\')  # Load the background image

    # Create game buttons. The Button\'s argument: x, y coordinates and image file
    buttons = [
        Button(100, 200, "btn_till.png"), 
        Button(100, 300, "btn_irrigate.png"),
        Button(100, 400, "btn_grazing.png"), 
        Button(500, 200, "btn_crop_rotation.png"),
        Button(500, 300, "btn_agroforestry.png")
    ]

    running = True  
    # Game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicked on close button, stop the game loop
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:  # If a mouse button is pressed
                # Get the position of the mouse cursor
                mouse_pos = pygame.mouse.get_pos()
                # Traverse through all buttons and check if a button was clicked
                for i, button in enumerate(buttons):
                    # The collidpoint() function of pygame.Rect checks if a point is inside the rectangular area
                    if button.rect.collidepoint(mouse_pos): 
                        # Depending on which button is clicked, the corresponding update is performed in the GameState
                        if i==0:
                            game.update_game(1, {"forest": 0, "soil": 20, "water": 0})
                        elif i==1:
                            game.update_game(2, {"forest": 0, "soil": 0, "water": 20})
                        elif i==2:
                            game.update_game(3, {"forest": 20, "soil": 0, "water": 0})
                        elif i==3:
                            game.update_game(4, {"forest": 0, "soil": -10, "water": 0})
                        elif i==4:
                            game.update_game(5, {"forest": -10, "soil": 0, "water": 0})
        
        # Draw the background
        screen.blit(bg, (0, 0))

        # Draw the buttons
        for button in buttons:
            button.draw(screen)

        pygame.display.flip()  # Update the full display Surface to the screen
        clock.tick(60)  # Limit the game loop to a maximum of 60 times per second

    pygame.quit()  # Shuts down PyGame.
    sys.exit()  # Exits Python interpreter

if __name__ == \'__main__\':
    main()
