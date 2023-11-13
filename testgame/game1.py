import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("The Sustainable Outlaw Mini-game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
LIGHT_BROWN = (160, 82, 45)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Setup game variables
forest_area = 200  # Initial forest area
farm_area = 200    # Initial farmable area
sustainability_score = 50  # Initial sustainability score

# Add a global variable to control whether a pop-up is displayed
display_popup = False 
popup_message = ""

def show_sustainability_tip(action):
    global display_popup, popup_message
    tips = {
        'plant': "Planting diverse crops can prevent soil depletion and reduce pest outbreaks.",
        'deforest': "Deforesting too much can lead to soil erosion and loss of biodiversity."
    }
    popup_message = tips.get(action, "")
    display_popup = True

def draw_popup():
    global display_popup, popup_message
    if display_popup:
        # Draw the popup background
        popup_rect = pygame.Rect(100, 100, 600, 400)
        pygame.draw.rect(screen, WHITE, popup_rect)
        pygame.draw.rect(screen, BLACK, popup_rect, 3)  # Border
        
        # Split message into lines to display within the popup
        words = popup_message.split(' ')
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) < 30:  # Simple logic to avoid very long lines
                current_line += word + " "
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)  # Add the last line
        
        # Render the text lines and blit them to the screen
        y_offset = 120
        for line in lines:
            rendered_text = font.render(line, True, BLACK)
            screen.blit(rendered_text, (120, y_offset))
            y_offset += 40
            
def dismiss_popup():
    global display_popup, popup_message
    display_popup = False
    popup_message = ""

def draw_buttons():
    # Plant crops button
    pygame.draw.rect(screen, GREEN, (600, 50, 150, 50))
    plant_text = font.render('Plant Crops', True, WHITE)
    #draw the plant sprite
    plant_sprite = pygame.image.load('decorationSprites/images/Tools/tool (1).png')
    plant_sprite = pygame.transform.scale(plant_sprite, (30, 30))
    screen.blit(plant_sprite, (700, 50))
    screen.blit(plant_text, (610, 60))

    # Deforest button
    pygame.draw.rect(screen, BROWN, (600, 150, 150, 50))
    deforest_text = font.render('Deforest', True, WHITE)
    #draw the deforest sprite
    deforest_sprite = pygame.image.load('decorationSprites/images/Tools/tool (5).png')
    deforest_sprite = pygame.transform.scale(deforest_sprite, (30, 30))
    screen.blit(deforest_sprite, (700, 150))
    screen.blit(deforest_text, (620, 160))

# Check if a position is within a rect
def is_within_pos(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    return (rx <= x <= rx+rw) and (ry <= y <= ry+rh)

plant_button_area = pygame.Rect(600, 50, 150, 50)
deforest_button_area = pygame.Rect(600, 150, 150, 50)

SUSTAINABILITY_THRESHOLD = 30
def check_sustainability_warning():
    global sustainability_score, display_popup, popup_message
    if sustainability_score < SUSTAINABILITY_THRESHOLD and not display_popup:
        # Show a warning message about sustainability
        popup_message = "Warning! Sustainability is low. Consider more eco-friendly practices."
        display_popup = True

seeds = 100
water = 100
money = 1000  # Start with a certain amount of money

# Define the costs and yields
seed_cost = 2  # Cost for planting one area unit of crops
water_cost = 1  # Cost for watering one area unit of crops
crop_yield = 4  # Money earned per area unit of crops harvested

# Update button click functions to include resource management
def plant_crops():
    global seeds, water, money, farm_area, sustainability_score
    if seeds >= seed_cost and water >= water_cost:
        farm_area += 10
        sustainability_score += 2
        seeds -= seed_cost
        water -= water_cost
        # Implement logic to grow crops and eventually harvest for money
        # ...

def deforest():
    global forest_area, sustainability_score, money
    forest_area -= 10
    sustainability_score -= 5
    # Assuming deforestation provides some money
    money += 20
    # ...

# Revise the button_click function
def button_click(pos):
    if plant_button_area.collidepoint(pos):
        plant_crops()
    elif deforest_button_area.collidepoint(pos):
        deforest()
    check_sustainability_warning()


# Optional: Add a draw_resources function to display resources on the screen
def draw_resources():
    # Display the current amount of resources
    seeds_text = font.render(f'Seeds: {seeds}', True, BLACK)
    water_text = font.render(f'Water: {water}', True, BLACK)
    money_text = font.render(f'Money: ${money}', True, BLACK)
    
    screen.blit(seeds_text, (50, 500))
    screen.blit(water_text, (200, 500))
    screen.blit(money_text, (350, 500))


def draw_environment():
    # Draw the background image
    background = pygame.image.load('testgame/background.jpg')
    background = pygame.transform.scale(background, (800, 600))
    screen.blit(background, (0, 0))
    # Draw the forest area
    # Change color based on the forest_area to simulate forest health
    # A full forest is lush and dark green, whereas a small forest could be brownish
    forest_health_color = (min(255, 100 + (forest_area // 2)), 
                           min(100 + (forest_area // 2), 255), 
                           50)
    pygame.draw.rect(screen, forest_health_color, (50, 50, forest_area, 100))

    # Draw the farm area with a similar feedback logic
    # A healthy farm area is a vibrant yellow-green, an overused area is pale
    farm_health = max(farm_area, 100)  # Farm cannot be 0, to prevent division by zero
    farm_health_color = (max(150 - (farm_area * 100 // farm_health), 100), 
                         min(250, 200 + (farm_area * 55 // farm_health)), 
                         50)
    pygame.draw.rect(screen, farm_health_color, (50, 200, farm_area, 100))
# Main game loop
def game_loop():
    global farm_area, forest_area, sustainability_score, display_popup
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if display_popup:
                    dismiss_popup()
                else:
                    button_click(pos)

        # Draw the environment
        screen.fill(WHITE)
        # ... [drawing code from the previous snippet] ...
        draw_buttons()
        screen.fill(WHITE)

        # Draw indicators for various areas
        pygame.draw.rect(screen, DARK_GREEN, (50, 50, forest_area, 100))
        pygame.draw.rect(screen, LIGHT_BROWN, (50, 200, farm_area, 100))
        pygame.draw.rect(screen, BLUE, (50, 350, farm_area, 100))
        
        # Displaying the sustainability score
        score_text = font.render(f'Sustainability Score: {sustainability_score}', True, BLACK)
        screen.blit(score_text, (50, 10))
         
         
        draw_environment()
         # Draw pop-up if necessary
        draw_popup()
        draw_resources()  # Show the resources on the screen
        # Draw buttons with updated logic
        draw_buttons()
        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)




# Clock to manage frame rate
clock = pygame.time.Clock()

# Run the game loop
game_loop()

# Quit the game
pygame.quit()
sys.exit()