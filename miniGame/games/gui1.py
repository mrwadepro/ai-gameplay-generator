import pygame
import random

pygame.init()


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


def game():
    # set the pygame window name
    pygame.display.set_caption('Green-Saver Quest')

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    font_small = pygame.font.Font(None, 25)
    font_large = pygame.font.Font(None, 55)

    btn_font = pygame.font.Font(None, 35)
    btn_color = (0, 255, 255)

    background = pygame.image.load('farm.jpg')
    btn_image = pygame.Surface((120, 40))

    ecosystem = Ecosystem()

    running = True

    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if ecosystem.check_values():
            status_msg = "Current status: Forest={}, Soil={}, Water={}".format(
                ecosystem.forest, ecosystem.soil, ecosystem.water)
            quest_msg = "A new quest just arrived!"

            status_text = font_small.render(status_msg, True, (255, 255, 255))
            quest_text = font_large.render(quest_msg, True, (255, 255, 255))

            # Draw buttons
            btn_image.fill(btn_color)
            screen.blit(btn_image, (40, 350))
            screen.blit(btn_image, (180, 350))
            screen.blit(btn_font.render('Button 1', True, (0, 0, 0)), (50, 350))

            screen.blit(status_text, (20, 20))
            screen.blit(quest_text, (20, 60))

            pygame.display.flip()

        else:
            over_msg = "Your island became uninhabitable. Please restart your adventure."
            over_text = font_large.render(over_msg, True, (255, 255, 255))
            screen.blit(over_text, (20, 250))
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False

    pygame.quit()


game()