
import pygame
import sys
import os

# Initial setup
pygame.init()

# Sets the window title
pygame.display.set_caption('The Star\'s Journey')

# Sets the screen size
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)

# Load the background image. Assumes the image is in the 'assets' directory.
background = pygame.image.load(os.path.join('assets', 'background.png'))
background = pygame.transform.scale(background, screenSize)  # Scale it to fit our window.

class Button:
    # Load button images, assuming they are in 'assets' directory
    idle = pygame.image.load(os.path.join('assets', 'button_idle.png'))
    hover = pygame.image.load(os.path.join('assets', 'button_hover.png'))
    click = pygame.image.load(os.path.join('assets', 'button_click.png'))

    def __init__(self, text, pos):
        """Initializes a Button."""
        self.text = text
        self.pos = pos
        self.image = Button.idle
        self.rect = self.image.get_rect(center=pos)
        self.font = pygame.font.Font(None, 36)  # Change the font to suit your needs.

    def draw(self, screen):
        """Draws the button and text on the screen."""
        screen.blit(self.image, self.rect)
        screen.blit(self.font.render(self.text, True, (0, 0, 0)), (self.pos[0] - 45, self.pos[1] - 10))

    def handle_event(self, event):        
        """Handles mouse events and changes button image accordingly."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.image = Button.click
            else:
                self.image = Button.hover
        else:
            self.image = Button.idle
        return self.image == Button.click


class StarsLifecycle:
    def __init__(self):         
        """Initializes the Star's lifecycle game."""
        self.stage = 0  # 0 - Start, 1 - Red SuperGiant, 2 - Supernova, 3 - Black Hole
        self.stages = ['Star', 'Red SuperGiant', 'Supernova', 'Black Hole']
        self.buttons = [Button(self.stages[i], (400, 150 * i + 50)) for i in range(1, 4)]

    def draw(self, screen):
        """Draws the current game state on the screen."""
        screen.blit(background, (0, 0)) # draws the background
        for button in self.buttons:
            button.draw(screen)

    def handle_event(self, event):   
        """Handles the logic for buttons clicked."""
        for i, button in enumerate(self.buttons, 1):
            if button.handle_event(event):
                if (self.stage == 0 and i == 1) or (self.stage == 1 and i == 2) or (self.stage == 2 and i == 3):
                    self.stage += 1
                    if self.stage == 3:
                        pygame.quit()
                        sys.exit() # if the game stages have been successfully navigated, the game ends
                else:
                    pygame.quit()
                    sys.exit() # if the button clicked does not align with the game stages, the game ends


game = StarsLifecycle()

# Game Loop
while True:
    """The main game loop."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            game.handle_event(event)
            
    game.draw(screen)
    pygame.display.flip()  # updates the contents of the entire display
