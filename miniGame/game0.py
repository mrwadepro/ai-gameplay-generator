from iter_game import iter_game
import pygame
import random

class animal_game(iter_game):
    def __init__(self, window_width=800, window_height=600):
        super().__init__(window_width, window_height)
        self.animal_list = ['cow', 'sheep', 'pig', 'chicken', 'horse', 'dog', 'cat']
        self.animal_origin = {
            'cow': 'South Asia and East Asia',
            'sheep': 'Southwest Asia',
            'pig': 'Eurasia',
            'chicken': 'Southeast Asia',
            'horse': 'Eurasia',
            'dog': 'Eurasia',
            'cat': 'Africa'
        }
        self.animal_domestication = {
            'cow': 'Used for milk, meat and as draft animals',
            'sheep': 'Used for wool, meat and milk',
            'pig': 'Used for meat',
            'chicken': 'Used for meat and eggs',
            'horse': 'Used for transportation, work and meat',
            'dog': 'Used for hunting, guarding and companionship',
            'cat': 'Used for hunting vermin and companionship'
        }
        self.animal_distribution = {
            'cow': 'Worldwide',
            'sheep': 'Worldwide',
            'pig': 'Worldwide',
            'chicken': 'Worldwide',
            'horse': 'Worldwide',
            'dog': 'Worldwide',
            'cat': 'Worldwide'
        }
        self.current_animal = random.choice(self.animal_list)
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render('Animal: ' + self.current_animal, True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.window_width // 2, self.window_height // 2)

    def next(self, pygame, events, screen, dt, data):
        if self.fin:
            data.game_num = 0
            return
        for event in events:
            if event.type == pygame.QUIT:
                self.fin = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.current_animal = random.choice(self.animal_list)
                    self.text = self.font.render('Animal: ' + self.current_animal, True, (255, 255, 255))
        screen.fill((0, 0, 0))
        screen.blit(self.text, self.textRect)
        pygame.display.flip()

    def get_animal_info(self, animal):
        return self.animal_origin[animal], self.animal_domestication[animal], self.animal_distribution[animal]
