
# Import necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Define game window size
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

# Define icon sizes
icon_size = 60

# Create dictionaries for each region with its respective commodities, image, and coordinates on screen
regions = [
    {'name': 'Region1', 'commodities': ['peanuts', 'cotton'], 'icon': pygame.image.load('region1.jpg'), 'coords': (100, 100)},
    {'name': 'Region2', 'commodities': ['poultry', 'peaches'], 'icon': pygame.image.load('region2.jpg'), 'coords': (300, 200)},
    {'name': 'Region3', 'commodities': ['peaches'], 'icon': pygame.image.load('region3.jpg'), 'coords': (500, 300)},
    {'name': 'Region4', 'commodities': ['poultry'], 'icon': pygame.image.load('region4.jpg'), 'coords': (700, 200)},
    {'name': 'Region5', 'commodities': ['peanuts'], 'icon': pygame.image.load('region5.jpg'), 'coords': (500, 400)},
]

# Create dictionaries for each commodity with its image
commodities = [
    {'name': 'peanuts', 'icon': pygame.image.load('peanuts.jpg')},
    {'name': 'cotton', 'icon': pygame.image.load('cotton.jpg')},
    {'name': 'poultry', 'icon': pygame.image.load('poultry.jpg')},
    {'name': 'peaches', 'icon': pygame.image.load('peaches.jpg')},
]

# Scale images to fit icon size
for region in regions:
    region['icon'] = pygame.transform.scale(region['icon'], (icon_size, icon_size))
for commodity in commodities:
    commodity['icon'] = pygame.transform.scale(commodity['icon'], (icon_size, icon_size))

# Draw game frame
def draw_game():
    # Draw each regional icon on screen
    for region in regions:
        screen.blit(region['icon'], region['coords'])

    # Draw each commodity icon on screen
    y = 10
    for commodity in commodities:
        screen.blit(commodity['icon'], (10, y))
        y += icon_size + 10
    # Update display to show new frame
    pygame.display.flip()

# Check if selected region is correct for the given commodity
def check_correct_region(commodity, region):
    return commodity['name'] in region['commodities']

# Main game function
def play_game():
    score = 0
    running = True
    while running:
        # Randomly select a commodity
        commodity = random.choice(commodities)
        print(f'Your commodity is {commodity["name"]}')
        draw_game()
        # Check for events (user actions)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: # Check for mouse click event
                x, y = pygame.mouse.get_pos()  # Get mouse click position
                # Go through each region to find which one was clicked
                for region in regions:
                    coords = region['coords']
                    # Check if mouse click was within the region's icon
                    if coords[0] <= x <= coords[0] + icon_size and coords[1] <= y <= coords[1] + icon_size:
                        # Check if selected region is correct for the commodity
                        if check_correct_region(commodity, region):
                            score += 10
                            print(f'Good job! This commodity grows well in {region["name"]}. Your score: {score}\
')
                        # If the region is not correct, end the game
                        else:
                            running = False
                            print(f'Oops... This commodity does not grow well in {region["name"]}. Your score: {score}\
')

# Start the game
if __name__ == "__main__":
    play_game()
