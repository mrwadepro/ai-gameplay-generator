# Import necessary packages
import pygame
import pygame_gui
import os

# Define the height and width of the screen
HEIGHT = 600
WIDTH = 800
WHITE = (255, 255, 255)  # RGB color code for white

pygame.init()  # Initialize Pygame

pygame.display.set_caption("Farmageddon: Regrowth")  # Title of the game
window_surface = pygame.display.set_mode((WIDTH, HEIGHT))  # Initialize window

# GameState class includes all elements related to the game status and interface
class GameState:
    def __init__(self):
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT))  # Create an instance of Pygame GUI Manager

        # Define buttons for different actions in the game
        self.plant = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 200), (100, 50)),
                                                  text='Plant Crops',
                                                  manager=self.manager)
        self.harvest = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 200), (100, 50)),
                                                    text='Harvest Crops',
                                                    manager=self.manager)
        self.fertilize = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 200), (100, 50)),
                                                      text='Use Fertilizer',
                                                      manager=self.manager)
        self.water = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 200), (100, 50)),
                                                  text='Use Water',
                                                  manager=self.manager)

        self.year = 1  # Initialize game parameters
        self.soil_health = 100
        self.animals = 100

    # Define a method inside the class to draw state on the screen
    def draw_state(self):
        font = pygame.font.Font('freesansbold.ttf', 32)  # Define font for text in the game
        window_surface.blit(font.render(f"Year: {self.year}", True, WHITE), (50, 50))
        window_surface.blit(font.render(f"Soil Health: {self.soil_health}", True, WHITE), (50, 90))
        window_surface.blit(font.render(f"Animals in Forest: {self.animals}", True, WHITE), (50, 130))

    # Define a method inside the class to process events
    def process_events(self, event):
        if event.type == pygame.USEREVENT:  # Check for event of button press
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.plant:  # If 'Plant Crops' button is pressed
                    self.soil_health += 1
                    if self.soil_health > 100:
                        self.soil_health = 100
                if event.ui_element == self.harvest:  # If 'Harvest Crops' button is pressed
                    self.soil_health -= 1
                    if self.soil_health < 0:
                        self.soil_health = 0
                if event.ui_element == self.fertilize:  # If 'Use Fertilizer' button is pressed
                    self.animals += 1
                    if self.animals > 100:
                        self.animals = 100
                if event.ui_element == self.water:  # If 'Use Water' button is pressed
                    self.animals -= 1
                    if self.animals < 0:
                        self.animals = 0

        self.manager.process_events(event)  # Pass the event to the GUI manager

game_state = GameState()  # Initialize GameState
background = pygame.image.load(os.path.join(os.path.dirname(__file__), 'farm.jpg'))  # Load background image

clock = pygame.time.Clock()  # Define clock object to manage frame rate
while True:  # Main game loop
    time_delta = clock.tick(60) / 1000.0  # Keep frame rate constant

    window_surface.blit(background, (0, 0))  # Display the background picture

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit game if QUIT event
            pygame.quit()

        game_state.process_events(event)  # Game state processes user events

    game_state.draw_state()  # Draw current game state on the screen
    game_state.manager.update(time_delta)  # Update the game state
    game_state.manager.draw_ui(window_surface)  # Draw user interface

    pygame.display.update()  # Update screen display after each iteration
