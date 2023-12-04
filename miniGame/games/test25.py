
# Start by importing pygame library
import pygame

# This class represent the game state
class SeasonSpin:
    def __init__(self):
        self.position = 0  # Position of Earth in its orbit
        self.speed = 1  # Speed of Earth\'s orbit
        self.seasons = ['Spring', 'Summer', 'Autumn', 'Winter']  # List of seasons
        self.current_season = self.seasons[0]  # Starting season

    # Function to update current season based on position
    def update_season(self):
        self.current_season = self.seasons[self.position // 25 % 4]

    # Function to move Earth forward in its orbit
    def move_forward(self):
        self.position = (self.position + self.speed) % 100
        self.update_season()

    def move_backward(self):
        self.position = (self.position - self.speed) % 100
        self.update_season()

    # Function to increase speed of orbit
    def speed_up(self):
        self.speed = min(10, self.speed+1)

    # Function to decrease speed of orbit
    def slow_down(self):
        self.speed = max(1, self.speed-1)


# Initializing the Pygame library
pygame.init()

# Setting up the display size
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading images/assets for background, earth, and sun
bg = pygame.image.load('miniGame/games/farm.jpg')
earth = pygame.image.load('decorationSprites/images/Furniture/furniture (3).png')
sun = pygame.image.load('decorationSprites/images/Furniture/furniture (4).png')

# Creating an instance of the game state
game = SeasonSpin()

# Main game loop
run = True
while run:
    pygame.time.delay(1000)  # FPS limiting / game speed 

    # Event handling 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Check if click is on Increase speed button
            if 50 <= x <= 150 and 50 <= y <= 100:  
                game.speed_up()
            # Check if click is on Decrease speed button
            elif 50 <= x <= 150 and 150 <= y <= 200:
                game.slow_down()
    
    # Update Game State
    game.move_forward()

    # Drawing the background, sun and earth on the window
    win.blit(bg, (0,0))
    win.blit(sun, (WIDTH//2, HEIGHT//2))
    win.blit(earth, (WIDTH//2 + game.position, HEIGHT//2))  

    # Draw buttons for increasing and decreasing speed
    pygame.draw.rect(win, (0,0,255), pygame.Rect(50, 50, 100, 50)) # Increase speed button
    pygame.draw.rect(win, (255,0, 0), pygame.Rect(50, 150, 100, 50)) # Decrease speed button

    # Updating the whole window
    pygame.display.update()

    # Check if game ends
    if game.current_season == 'Winter' and game.position == 99:
        print("Congratulations, you've completed one full orbit!")
        break

# Quit pygame
pygame.quit()
