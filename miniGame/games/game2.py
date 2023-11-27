import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = {
    "crops": [],
    "water": 100,
    "air": 100,
    "soil": 100,
    "plants": 100,
    "insects": 100
}

def draw_board():
    # Colors
    WHITE = (255, 255, 255)
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw stats on the board
    font = pygame.font.Font(None, 25)
    text = font.render('Water: '+str(player['water']), True, (0, 0, 0))
    screen.blit(text, [5, 5])
    # Similarly add for air, soil, plants, insects, and other data that needs to be displayed.

    # Visuals like trees and water bodies can be represented with rectangles or circles for now
    blue = (0, 0, 255)
    green = (0, 255, 0)
    pygame.draw.rect(screen, green, [50, 50, 50, 50])  # Draw a green rectangle to represent a tree
    pygame.draw.rect(screen, blue, [150, 150, 60, 60])  # Draw a blue rectangle to represent a water body

    # Always call this after drawing everything
    pygame.display.flip()

def get_crop_water_usage(choice):
    if choice == 'crop1':
        return 10
    elif choice == 'crop2':
        return 20 
    else:
        return 5  # return a default value for other crops

def get_crop_pest_usage(choice):
    if choice == 'crop1':
        return 15
    elif choice == 'crop2':
        return 10
    else:
        return 5  # return a default value for other crops

def plant_crops(player, choice):
    player["crops"].append(choice)
    water_use = get_crop_water_usage(choice)
    player["water"] -= water_use if water_use is not None else 0
    pest_use = get_crop_pest_usage(choice)
    player["insects"] -= pest_use if pest_use is not None else 0

def calc_positive_impact(player):
    positive_impact = sum(player.values())
    return positive_impact

def calc_negative_impact(player):
    negative_impact = 600 - sum(player.values())
    return negative_impact

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()

        draw_board()
        # Implement game-logic her