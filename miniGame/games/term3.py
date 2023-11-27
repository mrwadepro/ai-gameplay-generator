
import time

print("Welcome to the Eco-Farmer game!\
In this game, you will learn the impact of farming practices on nature.\
Your goal is to run a farm without causing much harm to the environment.")

# setup game variables
forest_health = 100
soil_health = 100
water_level = 100
farm_area = 1

# game actions
actions = ["Plant crops", "Expand farm", "Irrigate land", "Check environment status"]

# game loop
while True:
    print("\
--------------------------")
    print("Actions: ")
    for i, action in enumerate(actions):
        print(f"{i + 1}. {action}")
    choice = int(input("Choose action by typing a number: "))
    
    if choice == 1:
        # planting crops reduces soil health
        soil_health -= 5
        print("Crops planted. Soil health decreased by 5.")
    elif choice == 2:
        # expanding farm reduces forest health and increases farm area
        forest_health -= 10
        farm_area += 1
        print("Farm expanded. Forest health decreased by 10.")
    elif choice == 3:
        # irrigating land reduces water level
        water_level -= 15
        print("Water used for irrigation. Water level decreased by 15.")
    elif choice == 4:
        # checking environmental status
        print("\
===== Evironmental Status ========")
        print("Forest Health:", forest_health)
        print("Soil Health:", soil_health)
        print("Water Level:", water_level)
    else:
        print("Invalid action. Please, choose available ones.")

    
    # checking game over conditions
    if forest_health <= 0:
        print("*** Game Over: The forest has been completely destroyed! ***")
        break
    elif soil_health <= 0:
        print("*** Game Over: The soil has gone sterile! ***")
        break
    elif water_level <= 0:
        print("*** Game Over: The water level is too low! ***")
        break
    
    # let player rest between each action
    time.sleep(2)
