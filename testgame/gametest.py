import random

def game_intro():    
    print("\n Welcome to Agriland Adventure! \n")
    print("You are a hero from a modern city, suddenly you are whisked away to Agriland, a realm where all agricultural products originate.")
    print("In this mini adventure, you will learn about farming techniques, grow crops and raise livestock, and see the impacts of your actions in your city.")
    print("Let's start your adventure!")

def game():
    # Game state
    game_state = {
        'city_status': 5,
        'farm_status': 2,
        'farm_value': 20  # This is how much farming value you've created so far.
    }

    game_intro()

    # Main game loop
    while True:
        # Show game state
        print("\nCurrent city status: ", game_state['city_status'])
        print("Farm status: ", game_state['farm_status'])
        print("Farming value: ", game_state['farm_value'], "\n")

        # If farm_status drops to 0, game over.
        if game_state['farm_status'] <= 0:
            print("Your farm is depleted. Game over!")
            break

        # If city_status drops to 0, game over.
        if game_state['city_status'] <= 0:
            print("The city's resources have been depleted. Game over!")
            break

        # If farming value reaches 100, you win!
        if game_state['farm_value'] >= 100:
            print("Congratulations! You successful balancing the city's demands with farming values. You are a true agricultural hero!")
            break

        # Every turn the city status decreases by 1 due to consumption
        game_state['city_status'] -= 1
        game_state['farm_status'] -= random.choice(range(1, 3))  # Farm status decreases due to arbitrary farming challenges

        action = input("\nWhat will you do this turn? (Farm, Nutrition, Rest): ")

        if action.lower() == 'farm':
            print("You worked hard on your farm!")
            game_state['farm_value'] += random.choice(range(5, 11))  # Adds between 5-10 farming value

        elif action.lower() == 'nutrition':
            print("You made a meal with what you've farmed!")
            game_state['city_status'] += random.choice(range(1, 3))  # Adds between 1-2 city status

        elif action.lower() == 'rest':
            print("You rested for the day. Your Farm status is improved slightly.")
            game_state['farm_status'] += 1

        else:
            print("Invalid action. Try Again.")

game()