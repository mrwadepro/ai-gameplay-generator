import pygame
import random
import time

pygame.init()

# set the pygame window name
pygame.display.set_caption('Green-Saver Quest')

size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

class Ecosystem:
    def __init__(self):
        self.forest = 100
        self.soil = 100
        self.water = 100

    def decrease_forest(self, decrement):
        self.forest -= decrement
        self.check_values()

    def decrease_soil(self, decrement):
        self.soil -= decrement
        self.check_values()

    def decrease_water(self, decrement):
        self.water -= decrement
        self.check_values()

    def increase_forest(self, increment):
        self.forest += increment
        self.check_values()

    def increase_soil(self, increment):
        self.soil += increment
        self.check_values()

    def increase_water(self, increment):
        self.water += increment
        self.check_values()

    def check_values(self):
        if self.forest <= 0 or self.soil <= 0 or self.water <= 0:
            return False
        return True

def quest(ecosystem):
    quests_types = ["forest", "soil", "water"]
    quest_type = random.choice(quests_types)
    if quest_type == "forest":
        decrement = random.randint(10, 25)
        ecosystem.decrease_forest(decrement)
        return f'Forest decreased by {decrement}'
    elif quest_type == "soil":
        increment = random.randint(5, 15)
        ecosystem.increase_soil(increment)
        return f'Soil increased by {increment}'
    elif quest_type == "water":
        decrement = random.randint(10, 25)
        ecosystem.decrease_water(decrement)
        return f'Water decreased by {decrement}'

def print_status(ecosystem):
    return f"Current status: Forest={ecosystem.forest}, Soil={ecosystem.soil}, Water={ecosystem.water}"

def game():
    ecosystem = Ecosystem()
    message = ''
    while ecosystem.check_values():
        message = print_status(ecosystem)
        text = font.render(message, True, (0, 0, 0))
        screen.blit(text, (10, 10))
        pygame.display.flip()

        message = quest(ecosystem)
        text = font.render(message, True, (0, 0, 0))
        screen.blit(text, (10, 40))
        pygame.display.flip()
        
        time.sleep(1)
        screen.fill((255,255,255))
    
    message = 'Your island became uninhabitable. Please restart your adventure.'
    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    end_time = time.time() + 2
    while time.time() < end_time:
        clock.tick(60)

game()
pygame.quit()