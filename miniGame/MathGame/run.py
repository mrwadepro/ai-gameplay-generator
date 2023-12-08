
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display variables
WIN_WIDTH = 600
WIN_HEIGHT = 600
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))   # creating game screen

# Set up asset files
BUTTON_IMAGE = pygame.image.load('button.png')  # button image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load('background.jpg'), (WIN_WIDTH,WIN_HEIGHT))   # background image scaled to window size

class Button:   # class for button
    def __init__(self, image, position):
        self.rect = pygame.Rect(position[0], position[1], image.get_width(), image.get_height())  # position of button
        self.image = image    # image of the button

    def draw(self, win):     # Draw button on screen
        win.blit(self.image, (self.rect.x, self.rect.y))

    def is_over(self, pos):   # Checks if the mouse position is over the button
        return self.rect.collidepoint(pos)

def main():
    clock = pygame.time.Clock()

    run = True
    while run:    # game loop
        for event in pygame.event.get():   # event loop
            if event.type == pygame.QUIT:   # quit event
                run = False   # stops the game loop
            
        mouse_pos = pygame.mouse.get_pos()  # gets the current mouse position

        option_button = Button(BUTTON_IMAGE, (200, 200))   # Create a button
        if option_button.is_over(mouse_pos):   # Checks if mouse is over the button
            print("You have hovered over the button")
            if pygame.mouse.get_pressed()[0]:   # Checks if mouse is clicked
                print("You have clicked the button")

        
        redraw_window(option_button)   # Redraw the window
        clock.tick(60)   # Limits the game to running at 60 frames per second

    pygame.quit()   # quits pygame
    sys.exit()   # exits the program

def redraw_window(option_button):
    win.blit(BACKGROUND_IMAGE, (0,0))   # Draws background image
    option_button.draw(win)   # Draws the button
    pygame.display.update()   # Updates the display with all drawn elements

main()   # Run the game
