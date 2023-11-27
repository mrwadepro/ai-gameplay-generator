import pygame
import sys

class FarmGame:
    def __init__(self):
        self.money = 1000
        self.soil_health = 100
        self.water_quality = 100
        self.forest_resources = 100
        self.crop = ""
        self.game_over = False

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Enviro-Farm Game')

        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Load fonts
        self.font = pygame.font.SysFont(None, 32)

        # Define buttons
        self.buttons = {
            1: pygame.Rect(50, 100, 200, 50),
            2: pygame.Rect(50, 200, 200, 50),
            3: pygame.Rect(50, 300, 200, 50)
        }
        self.button_texts = {
            1: 'Buy crops or livestock',
            2: 'Invest in sustainability',
            3: 'Check farm status'
        }

    def draw_buttons(self):
        for key, rect in self.buttons.items():
            pygame.draw.rect(self.screen, self.GREEN, rect)
            text = self.font.render(self.button_texts[key], True, self.BLACK)
            self.screen.blit(text, (rect.x + 10, rect.y + 10))

    def buy_crops(self):
        # Implement the logic for buying crops in GUI
        cost = int(input("\nEnter the cost of the crops or livestock you want to buy: "))
        if cost > self.money:
            print("Sorry, you don\'t have enough money to buy this.")
        else:
            self.money -= cost
            self.soil_health -= 10
            self.water_quality -= 5
            print("You purchased new crops/livestock.")

    def invest_in_sustainability(self):
        # Implement the logic for investing in sustainability in GUI
        cost = int(input("\nEnter the cost of the sustainable agricultural practices you want to invest in: "))
        if cost > self.money:
            print("Sorry, you don\'t have enough money to invest in this.")
        else:
            self.money -= cost
            self.soil_health += 10
            self.water_quality += 5
            print("You invested in sustainable agricultural practices.")

    def check_farm_status(self):
        # Implement the logic for checking farm status in GUI
        print("\\nFarm Status:")
        print("Money: $", self.money)
        print("Soil Health:", self.soil_health, "%")
        print("Water Quality:", self.water_quality, "%")
        print("Forest Resources:", self.forest_resources, "%")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for key, rect in self.buttons.items():
                        if rect.collidepoint(pos):
                            if key == 1:
                                self.buy_crops()
                            elif key == 2:
                                self.invest_in_sustainability()
                            elif key == 3:
                                self.check_farm_status()

    def update_display(self):
        self.screen.fill(self.WHITE)
        self.draw_buttons()
        pygame.display.flip()

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update_display()

if __name__ == '__main__':
    FarmGame().run()
