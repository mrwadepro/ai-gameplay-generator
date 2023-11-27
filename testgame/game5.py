import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sustainable Farmville')

# Load a custom background image
background_image = pygame.image.load('testgame/background2.jpg')  # Replace 'your_image_path.jpg' with your image file path

# Font settings
font = pygame.font.Font(None, 36)

class Farm:
    # Your existing Farm class remains unchanged

    def __init__(self):
        self.soil_health = 100
        self.forest_health = 100
        self.money = 0
        self.crops = []
        self.livestock = []

    def plant_crop(self, crop_type):
        if crop_type == "Organic":
            self.crops.append(crop_type)
            self.soil_health -= 5
        elif crop_type == "Cash":
            self.crops.append(crop_type)
            self.soil_health -= 15
        elif crop_type == "Traditional":
            self.crops.append(crop_type)
            self.soil_health -= 10

    def rear_animals(self, animal_type):
        if animal_type == "Sheep":
            self.livestock.append(animal_type)
            self.soil_health -= 2
        elif animal_type == "Cows":
            self.livestock.append(animal_type)
            self.soil_health -= 5

    def harvest(self):
        for crop in self.crops:
            if crop == "Organic":
                self.money += 100
            elif crop == "Cash":
                self.money += 200
            elif crop == "Traditional":
                self.money += 150

        for animal in self.livestock:
            if animal == "Sheep":
                self.money += 50
            elif animal == "Cows":
                self.money += 100

        self.crops = []
        self.livestock = []

    def end_of_the_year(self):
        print(f"End of the year! Your farm made ${self.money} this year. Soil health is at {self.soil_health} and forest health at {self.forest_health}")
        if self.soil_health < 30 or self.forest_health < 30:
            print("However, your farming practices have seriously damaged the environment :( Please make more sustainable choices next year!")

    def get_status_text(self):
        return f"Money: ${self.money} | Soil Health: {self.soil_health} | Forest Health: {self.forest_health}"

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
    return text_rect

def main():
    running = True
    clock = pygame.time.Clock()

    my_farm = Farm()

    # Button positions and sizes (kept the same as before)
    button_width, button_height = 200, 50
    button_x, button_y = 50, 100
    button_spacing = 20

    # Define button rectangles (kept the same as before)
    plant_crop_button = pygame.Rect(button_x, button_y, button_width, button_height)
    rear_animals_button = pygame.Rect(button_x, button_y + button_height + button_spacing, button_width, button_height)
    do_nothing_button = pygame.Rect(button_x, button_y + 2 * (button_height + button_spacing), button_width, button_height)

    while running:
        screen.blit(background_image, (0, 0))  # Blit the background image onto the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if plant_crop_button.collidepoint(mouse_pos):
                    crop = random.choice(["Organic", "Cash", "Traditional"])
                    my_farm.plant_crop(crop)
                elif rear_animals_button.collidepoint(mouse_pos):
                    animal = random.choice(["Sheep", "Cows"])
                    my_farm.rear_animals(animal)
                elif do_nothing_button.collidepoint(mouse_pos):
                    pass

        # Draw buttons (kept the same as before)
        pygame.draw.rect(screen, (0, 255, 0), plant_crop_button)
        draw_text("Plant Crop", font, (0, 0, 0), screen, button_x + 20, button_y + 10)

        pygame.draw.rect(screen, (255, 0, 0), rear_animals_button)
        draw_text("Rear Animals", font, (0, 0, 0), screen, button_x + 20, button_y + button_height + button_spacing + 10)

        pygame.draw.rect(screen, (200, 200, 200), do_nothing_button)
        draw_text("Do Nothing", font, (0, 0, 0), screen, button_x + 20, button_y + 2 * (button_height + button_spacing) + 10)

        # Display farm status text (kept the same as before)
        status_text = my_farm.get_status_text()
        status_rect = draw_text(status_text, font, (0, 0, 0), screen, 20, 20)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
