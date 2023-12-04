
# The code imports two required libraries: pygame for GUI and sys for system specific parameters and functions.
import pygame
import sys


# This line initializes all imported pygame modules.
pygame.init()

# This creates a display Surface object with specified width and height.
screen = pygame.display.set_mode((800, 600))

# These lines load images from the specified file paths for game background and buttons. You can replace 'background.jpg' and 'button.png' with your own images.
background_image = pygame.image.load('background.jpg')
button_image = pygame.image.load('button.png')

# If images are not in a required size, pygame's transform module can be used for image scaling. Here, we're scaling the images to (800, 600) for background and (100, 50) for button.
background_image = pygame.transform.scale(background_image, (800, 600))
button_image = pygame.transform.scale(button_image, (100, 50))

# This creates a Rect object for the button image which later can be used for positioning the button and checking if it's clicked.
button_rect = button_image.get_rect()

# Sets the top left coordinate of the button
button_rect.topleft = (50, 50)

# The main game loop starts. This loop will run until the 'Quit' event occurs (e.g., closing the game window).
running = True
while running:
    # It goes through all the events currently in the event queue.
    for event in pygame.event.get():
        # The conditional checks if the 'Quit' event is in the queue, if true the loop terminates.
        if event.type == pygame.QUIT:
            running = False
        # The code checks if a mouse button down event has happened. If it has, and it happened while the cursor was on the button, the associated action can be performed.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Action to be performed when button is clicked
                pass

    # This line fills the screen with the background image.
    screen.blit(background_image, (0, 0))
    # This line draws the button on the screen at its defined coordinates.
    screen.blit(button_image, button_rect.topleft)

    # It updates the full display Surface to the screen, ensuring that the recent draws are visible in the screen
    pygame.display.flip()

# Once the main loop terminates (game ends), pygame is de-initialized
pygame.quit()
