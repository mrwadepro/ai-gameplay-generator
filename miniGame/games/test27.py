
import random

# This is the main class for our game
class FarmDefender:

    # We set the initial values of farm conditions in the constructor
    def __init__(self):
        # Initial farm conditions
        self.soil_fertility = 100
        self.forest_health = 100
        self.water_resources = 100
        self.carbon_footprint = 0
        self.wealth = 100
        self.turn = 0
        self.game_over = False
        self.action_dict = {}
        self.possible_crops = ['Corn', 'Wheat', 'Rice']
        self.weather_patterns = ['drought', 'normal', 'rainy']

    # This function displays the current status of the farm
    def display_status(self):
        print(f"\nTURN: {self.turn}")
        print(f"Wealth: {self.wealth}")
        print(f"Soil Fertility: {self.soil_fertility}")
        print(f"Forest Health: {self.forest_health}")
        print(f"Water Resources: {self.water_resources}")
        print(f"Carbon Footprint: {self.carbon_footprint}\n")

    # This function lets the player choose an action from a set of options
    def choose_action(self, options):
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        choice = int(input("Enter your choice: "))
        action = options[choice-1]
        return action

    # This function carries out the chosen action
    def resolve_action(self, action):
        if action == 'Plant Corn':
            self.soil_fertility -= 10
            self.water_resources -= 20
            self.carbon_footprint += 5
        elif action == 'Plant Wheat':
            self.soil_fertility -= 5
            self.water_resources -= 10
            self.carbon_footprint += 5
        elif action == 'Plant Rice':
            self.soil_fertility -= 15
            self.water_resources -= 25
            self.carbon_footprint += 18
        else:
            self.soil_fertility += 5
            self.forest_health += 5
            self.water_resources += 5
            self.carbon_footprint -= 10

    # This function runs the start phase of the game
    def game_start(self):
        print("Welcome to Farm Defender!")
        print("Your goal is to maintain a profitable farm without over-exploiting natural resources.")
        print("Choose your actions wisely and monitor your farm's stats!")

    # This function checks the conditions for the game to end
    def game_end_check(self):
        if self.soil_fertility == 0 or self.water_resources == 0 or self.forest_health == 0 or self.carbon_footprint >= 150 or self.turn == 10:
            return True
        return False
        
    # This function contains the main game loop     
    def play_game(self):
        # Display initial game message
        self.game_start()
        # Run game until game over conditions are met
        while self.game_over == False:
            self.turn += 1
            print(f'\nStarting turn {self.turn}')
            self.display_status()  # Display current status
            
            print("\nChoose your action:")
            # Define what actions occur at each game turn
            if self.turn == 1:
                self.action_dict["planting"] = self.choose_action(self.possible_crops)
                self.action_dict["weather"] = random.choice(self.weather_patterns)
            else:
                self.action_dict["planting"] = self.choose_action(['Continue Planting Same Crop', 'Change Crop'])
                self.action_dict["weather"] = random.choice(self.weather_patterns)
            
            if self.action_dict["planting"] == 'Change Crop':
                self.action_dict["planting"] = f'Plant {self.choose_action(self.possible_crops)}'

            self.resolve_action(self.action_dict['planting'])

            print("\nYour farm after this turn:")
            self.display_status()  # Display status after performing actions

            # Check if game end conditions are met
            if self.game_end_check():
                print("\n---- Game Over ----")
                self.game_over = True

        self.display_status()


# Initialize and play Farm Defender game
game = FarmDefender()
game.play_game()
