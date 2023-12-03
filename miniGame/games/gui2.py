import pygame
import sys
import random
from pygame.locals import *

# Width and Height of the display screen
WIDTH, HEIGHT = 1000, 600

FPS = 60

# Colors you can use
WHITE = (255, 255, 255)

class Region:
    def __init__(self, name, environment, crops):
        self.name = name
        self.environment = environment
        self.crops = crops

regions = [
    Region("Coastal Plains", "Hot and humid climate", ["Peanuts", "Onions", "Cabbage"]),
    Region("Piedmont", "Mild climate with rich soil", ["Peaches", "Apples", "Wheat"]),
    Region("Blue Ridge", "Cool climate with high rainfall", ["Potatoes", "Peppers", "Tomatoes"])
]

class Player:
    def __init__(self, money):
        self.money = money

player = Player(1000) #starting money

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Georgia Growers")
        self.font = pygame.font.Font(None, 25)
        self.input_box = pygame.Rect(WIDTH/2 - 50, HEIGHT/2, 140, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.window.blit(text_surface, text_rect)

    def main(self):
        while True:
            mouseClicked = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    mouseClicked = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        mouseClicked = True

            self.window.fill((30, 30, 30))

            # Handle inputs
            if self.input_box.collidepoint(pygame.mouse.get_pos()):
                self.color = self.color_active
                self.active = not self.active
            else:
                self.color = self.color_inactive

            if mouseClicked:
                i = 1
                for region in regions:
                    self.draw_text(f"{i}. {region.name} - {region.environment}", 20, WIDTH/2, HEIGHT/2 - (150 - i*30))
                    i += 1

            pygame.draw.rect(self.window, self.color, self.input_box, 2)

            txt_surface = self.font.render(self.text, True, self.color)
            self.window.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
            self.input_box.w = max(200, txt_surface.get_width()+10)

            pygame.display.flip()
            self.clock.tick(60)
    
if __name__ == "__main__":
    Game().main()