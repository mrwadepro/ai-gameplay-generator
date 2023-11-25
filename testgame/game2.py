from tkinter import font
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The Daily Harvest")

# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
running = True
farm_products = {'wheat': False, 'corn': False}
store_inventory = []

font = pygame.font.SysFont(None, 24)
# Load images
# wheat_img = pygame.image.load('wheat.png')  # Placeholder for actual game assets

# New game variable to keep track of sales
sales_goal = {'wheat': 5, 'corn': 5}
current_sales = {'wheat': 0, 'corn': 0}

def check_win_condition():
    # Check if current sales have reached the goal for both products
    for product in sales_goal.keys():
        if current_sales[product] < sales_goal[product]:
            return False
    return True

def draw_farm_side():
    wheat_color = (242, 221, 107)  # Lighter color representing wheat
    corn_color = (255, 255, 0)  # Yellow color representing corn
    
    farm_wheat_area = pygame.Rect(0, 0, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    farm_corn_area = pygame.Rect(0, SCREEN_HEIGHT//2, SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    pygame.draw.rect(screen, wheat_color, farm_wheat_area)
    pygame.draw.rect(screen, corn_color, farm_corn_area)
    
    # Draw labels for wheat and corn areas
    wheat_text = font.render('Wheat Area', True, WHITE)
    corn_text = font.render('Corn Area', True, WHITE)
    
    # Calculate center position for the text labels
    wheat_text_rect = wheat_text.get_rect(center=(SCREEN_WIDTH//4, SCREEN_HEIGHT//4))
    corn_text_rect = corn_text.get_rect(center=(SCREEN_WIDTH//4, 3*SCREEN_HEIGHT//4))
    
    # Blit the text labels on screen
    screen.blit(wheat_text, wheat_text_rect)
    screen.blit(corn_text, corn_text_rect)

def draw_town_side():
    town_side = pygame.Rect(SCREEN_WIDTH//2, 0, SCREEN_WIDTH//2, SCREEN_HEIGHT)
    pygame.draw.rect(screen, BLUE, town_side)
    # More detailed town drawing would go here

def draw_store_inventory():
    y_offset = 0
    for item in store_inventory:
        text = font.render(item, True, WHITE)
        screen.blit(text, (SCREEN_WIDTH//2 + 10, 10 + y_offset))
        y_offset += 30

def handle_farm_interaction(x, y):
    # Check which part of the farm was clicked
    # Assume the left half of the screen is split into top half for wheat and bottom half for corn
    farm_height = SCREEN_HEIGHT
    wheat_area = pygame.Rect(0, 0, SCREEN_WIDTH//2, farm_height/2)
    corn_area = pygame.Rect(0, farm_height/2, SCREEN_WIDTH//2, farm_height/2)
    
    if wheat_area.collidepoint(x, y):
        # The user clicked on the wheat area
        farm_products['wheat'] = True  # The wheat is now harvested
    elif corn_area.collidepoint(x, y):
        # The user clicked on the corn area
        farm_products['corn'] = True  # The corn is now harvested


def handle_town_interaction(x, y):
    town_height = SCREEN_HEIGHT
    store_wheat_area = pygame.Rect(SCREEN_WIDTH/2, 0, SCREEN_WIDTH/2, town_height/2)
    store_corn_area = pygame.Rect(SCREEN_WIDTH/2, town_height/2, SCREEN_WIDTH/2, town_height/2)
    
    if store_wheat_area.collidepoint(x, y) and farm_products['wheat']:
        store_inventory.append('wheat')
        farm_products['wheat'] = False
        current_sales['wheat'] += 1  # Increment wheat sales
    elif store_corn_area.collidepoint(x, y) and farm_products['corn']:
        store_inventory.append('corn')    
        farm_products['corn'] = False
        current_sales['corn'] += 1  # Increment corn sales

clock = pygame.time.Clock()
# Main game loop
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x < SCREEN_WIDTH // 2:
                print("farm")
                # The user clicked on the farm side
                handle_farm_interaction(x, y)
            else:
                print("town")
                # The user clicked on the town side
                handle_town_interaction(x, y)
    
    draw_farm_side()
    draw_town_side()
    draw_store_inventory()
    
    if check_win_condition():
        print("Congratulations, you have met the sales goal for all products!")  # You can replace this with a proper in-game message or screen.
        running = False
    
    pygame.display.update()
    
    # Limit the frame rate to 60 frames per second
    clock.tick(60)

pygame.quit()
sys.exit()