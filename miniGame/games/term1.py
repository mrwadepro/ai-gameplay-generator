import pygame
import sys
class Farm:
    def __init__(self, water=100, air=100, soil=100, plants=100, insects=100):
        self.water = water
        self.air = air
        self.soil = soil
        self.plants = plants
        self.insects = insects
        self.money = 0

    def fertilize(self, amount):
        self.soil -= amount
        self.water -= amount
        self.money += 1
        self.status()

    def irrigate(self, amount):
        self.water -= amount
        self.soil += 0.5 * amount
        self.money += 1
        self.status()

    def pesticide(self, amount):
        self.insects -= amount
        self.air -= amount
        self.money += 1
        self.status()

    def status(self):
        print(f"Water: {self.water}\nAir: {self.air}\nSoil: {self.soil}\nPlants: {self.plants}\nInsects: {self.insects}\nMoney: {self.money}\n")


def game():
    farm = Farm()
    while farm.water > 0 and farm.air > 0 and farm.soil > 0 and farm.insects > 0:
        print("Choose an action:\n1. Fertilize\n2. Irrigate\n3. Use pesticide\n")
        action = input()

        if action == "1":
            farm.fertilize(20)
        elif action == "2":
            farm.irrigate(20)
        elif action == "3":
            farm.pesticide(20)
        else:
            print("Invalid option. Try again.")
    else:
        print("Game over. The farm's environment has collapsed due to mismanagement.")

def game():
    farm = Farm()

    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Farm Game')

    font = pygame.font.Font(None, 36)
    fertilize_button = pygame.Rect(50, 50, 150, 50)
    irrigate_button = pygame.Rect(50, 120, 150, 50)
    pesticide_button = pygame.Rect(50, 190, 150, 50)

    while farm.water > 0 and farm.air > 0 and farm.soil > 0 and farm.insects > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if fertilize_button.collidepoint(mouse_pos):
                    farm.fertilize(20)
                elif irrigate_button.collidepoint(mouse_pos):
                    farm.irrigate(20)
                elif pesticide_button.collidepoint(mouse_pos):
                    farm.pesticide(20)

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (0, 255, 0), fertilize_button)
        pygame.draw.rect(screen, (0, 0, 255), irrigate_button)
        pygame.draw.rect(screen, (255, 0, 0), pesticide_button)

        text_fertilize = font.render('Fertilize', True, (0, 0, 0))
        text_irrigate = font.render('Irrigate', True, (0, 0, 0))
        text_pesticide = font.render('Pesticide', True, (0, 0, 0))

        screen.blit(text_fertilize, (60, 60))
        screen.blit(text_irrigate, (60, 130))
        screen.blit(text_pesticide, (60, 200))

        pygame.display.flip()

    else:
        print("Game over. The farm's environment has collapsed due to mismanagement.")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game()