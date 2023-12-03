import time
import random

class FarmagicalKingdom:
    def __init__(self):
        self.player = "young dweller"
        self.farms = ['fruits farm', 'vegetables farm', 'cereals farm', 'animal farm']
        self.activities = ['planting seeds', 'watering crops', 'pest control', 'harvesting crops']
        self.spells = []
        self.magic_power = 100
        self.role = "farm_consumer"
        self.game_on = True

    def start_game(self):
        self.game_instructions()
        while self.game_on:
            farm_to_visit = random.choice(self.farms)
            self.visit_farm(farm_to_visit)

    def game_instructions(self):
        print("\nWelcome to Farmagical Kingdom!")
        time.sleep(2)
        print("You are a", self.player, "in the Farmagical Kingdom.")
        time.sleep(3)
        print("Your role is:", self.role)
        time.sleep(2)
        print("Your goal is to ensure continuous food supply for the kingdom by exploring the mystical farms, learning new magic spells and aiding the crops with your magic!")
        time.sleep(5)

    def visit_farm(self, farm_to_visit):
        print("\nYou are visiting the", farm_to_visit)
        self.learn_spell()
        self.perform_activities()
        self.check_market_status()

    def learn_spell(self):
        new_spell = random.choice(self.activities)
        if new_spell not in self.spells:
            self.spells.append(new_spell)
            print("\nYou've learned a new spell of", new_spell)
            self.magic_power += 20
            print("Your magic power after learning new spell is", self.magic_power)

    def perform_activities(self):
        farm_activity = random.choice(self.activities)
        if farm_activity in self.spells:
            print("\nPerforming farm activity of", farm_activity)
            self.magic_power -= 10
            print("Your magic power after performing activity is", self.magic_power)
            if self.magic_power < 20:
                print("\nYou need to recover your magic powers, take some rest!")
                self.game_on = False
        else:
            print("\nYou don't know the required spell for", farm_activity, "activity. Keep exploring the farms!")

    def check_market_status(self):
        if self.magic_power >= 50:
            print("\nThe market is recovering, food items reappearing! Continue doing the good work!")
            if len(self.spells) == len(self.activities):
                print("\nCongratulations, you've learned all farming spells and restored the food supply of Kingdom!")
                print("Market is bustling again and dwellers living happily!")
                self.game_on = False
        else:
            print("\nWe need more food items in market, continue exploring and helping farms")

    
game = FarmagicalKingdom()
game.start_game()