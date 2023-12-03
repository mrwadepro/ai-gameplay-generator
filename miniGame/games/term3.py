import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set the window dimensions
WIDTH = 1920
HEIGHT = 1080

# Load farm images and icons
farm_land_img = pygame.image.load("farm_land.jpg")  # Example image file names, please replace with your own
water_img = pygame.image.load("water_img.jpg")
forest_img = pygame.image.load("forest_img.jpg")
conventional_icon = pygame.image.load("conventional_icon.jpg")
organic_icon = pygame.image.load("organic_icon.jpg")
crop_rotation_icon = pygame.image.load("crop_rotation_icon.jpg")
anti_deforestation_icon = pygame.image.load("anti_deforestation_icon.jpg")

# Scale icons and images
farm_land_img = pygame.transform.scale(farm_land_img, (800, 600))
water_img = pygame.transform.scale(water_img, (200, 200))
forest_img = pygame.transform.scale(forest_img, (400, 300))
conventional_icon = pygame.transform.scale(conventional_icon, (100, 100))
organic_icon = pygame.transform.scale(organic_icon, (100, 100))
crop_rotation_icon = pygame.transform.scale(crop_rotation_icon, (100, 100))
anti_deforestation_icon = pygame.transform.scale(anti_deforestation_icon, (100, 100))

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Wisdom")

# Game variables
soil_health = 100
water_quality = 100
air_quality = 100
insect_population = 100
money = 0
crop_cycles = 0

# Function to update the game state
def update_game_state(farm_activity_choice, sustainable_practice_choice):
    global soil_health, water_quality, air_quality, insect_population, money, crop_cycles

    # Perform farming activity
    if farm_activity_choice == 1:
        soil_health -= random.randint(5, 25)
        water_quality -= random.randint(5, 25)
        air_quality -= 3
        insect_population -= random.randint(1, 5)
        money += random.randint(50, 200)
    elif farm_activity_choice == 2:
        soil_health -= 1
        water_quality -= 1
        air_quality -= 1
        money += random.randint(20, 100)

    # Implement a sustainable practice
    if sustainable_practice_choice == 1:
        soil_health += random.randint(5, 15)
        water_quality += random.randint(5, 15)
        air_quality += 3
    elif sustainable_practice_choice == 2:
        soil_health += 3
        water_quality += 3
        air_quality += 3
    
    crop_cycles += 1

# Function to display game status
def display_game_status():
    global soil_health, water_quality, air_quality, insect_population, money, crop_cycles

    # Clear the previous display
    window.fill((255, 255, 255))

    # Display farm images
    window.blit(farm_land_img, (50, 100))
    window.blit(water_img, (1200, 100))
    window.blit(forest_img, (1400, 100))

    # Display icons for farming activities
    window.blit(conventional_icon, (200, 800))
    window.blit(organic_icon, (400, 800))

    # Display icons for sustainable practices
    window.blit(crop_rotation_icon, (1400, 800))
    window.blit(anti_deforestation_icon, (1600, 800))

    # Display game status text
    font = pygame.font.Font(None, 50)
    text = font.render("Soil Health: " + str(soil_health), True, (0, 0, 0))
    window.blit(text, (50, 700))
    text = font.render("Water Quality: " + str(water_quality), True, (0, 0, 0))
    window.blit(text, (50, 750))
    text = font.render("Air Quality: " + str(air_quality), True, (0, 0, 0))
    window.blit(text, (1200, 700))
    text = font.render("Insect Population: " + str(insect_population), True, (0, 0, 0))
    window.blit(text, (1200, 750))
    text = font.render("Money: " + str(money), True, (0, 0, 0))
    window.blit(text, (1400, 700))
    text = font.render("Crop Cycles: " + str(crop_cycles), True, (0, 0, 0))
    window.blit(text, (1400, 750))

    # Update the display
    pygame.display.flip()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            
            # Check if the player clicked on the icons for farming activities
            if 200 <= position[0] <= 300 and 800 <= position[1] <= 900:
                update_game_state(1, 0)
            elif 400 <= position[0] <= 500 and 800 <= position[1] <= 900:
                update_game_state(2, 0)
            
            # Check if the player clicked on the icons for sustainable practices
            elif 1400 <= position[0] <= 1500 and 800 <= position[1] <= 900:
                update_game_state(0, 1)
            elif 1600 <= position[0] <= 1700 and 800 <= position[1] <= 900:
                update_game_state(0, 2)
    
    # Render the game status
    display_game_status()

# Quit pygame
pygame.quit()