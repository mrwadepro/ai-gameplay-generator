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
        return self.status()

    def irrigate(self, amount):
        self.water -= amount
        self.soil += 0.5 * amount
        self.money += 1
        return self.status()

    def pesticide(self, amount):
        self.insects -= amount
        self.air -= amount
        self.money += 1
        return self.status()

    def status(self):
        return (f"Water: {self.water}\nAir: {self.air}\nSoil: {self.soil}\nPlants: {self.plants}\nInsects: {self.insects}\nMoney: {self.money}\n")


def display_notifications(screen, font, notifications):
    notification_y = 30
    for notification in notifications:
        text_notification = font.render(notification, True, (0, 0, 0))
        screen.blit(text_notification, (220, notification_y))
        notification_y += 30


def game():
    farm = Farm()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Farm Game')

    background = pygame.image.load('testgame/background2.jpg')  # Replace 'your_background_image.jpg' with your image file
    background = pygame.transform.scale(background, (800, 600))  # Adjust the size if needed

    font = pygame.font.Font(None, 24)
    notifications = []

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
                    notifications.append(farm.fertilize(20))
                elif irrigate_button.collidepoint(mouse_pos):
                    notifications.append(farm.irrigate(20))
                elif pesticide_button.collidepoint(mouse_pos):
                    notifications.append(farm.pesticide(20))

        screen.blit(background, (0, 0))  # Display background image

        pygame.draw.rect(screen, (0, 255, 0), fertilize_button)
        pygame.draw.rect(screen, (0, 0, 255), irrigate_button)
        pygame.draw.rect(screen, (255, 0, 0), pesticide_button)

        text_fertilize = font.render('Fertilize', True, (0, 0, 0))
        text_irrigate = font.render('Irrigate', True, (0, 0, 0))
        text_pesticide = font.render('Pesticide', True, (0, 0, 0))

        screen.blit(text_fertilize, (60, 60))
        screen.blit(text_irrigate, (60, 130))
        screen.blit(text_pesticide, (60, 200))

        # Display notifications in the game window
        display_notifications(screen, font, notifications)

        pygame.display.flip()

    else:
        notifications.append("Game over. The farm's environment has collapsed due to mismanagement.")

        # Display final notifications before quitting
        display_notifications(screen, font, notifications)
        pygame.display.flip()

        # Wait for a few seconds before exiting
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game()