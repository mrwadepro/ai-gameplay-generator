
import random
import time

def display_intro():
    print("\
Welcome to Farm Impact.")
    print("Your mission is to manage a farm, balancing the highest productivity and the minimal environmental impact.")
    print("You will take decisions that impacts water, air, soil, crops and insects.")
    print("But be cautious, you need to make wise choices in order to prevent an environment collapse.")
    print("Good luck!\
")

def farming_season(money, productivity, environment):
    print("New season starts. You currently have $"+str(money))
    
    print("1. Invest in crops ($10). This will increase productivity but might reduce environment score.")
    print("2. Invest in livestock ($20). This could increase productivity but might reduce environment score.")
    print("3. Build water reservoir ($30). This reduces your risk against drought and minimizes water consumption.")
    print("4. Plant more trees ($10). This will increase environment score but won’t increase productivity.")
    print("5. Consider not farming this season (let the land rest, $0). This will not increase productivity but might increase environment score.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        money -= 10
        productivity += random.randint(1,5)
        environment -= random.randint(1,3)
    elif choice == 2:
        money -= 20
        productivity += random.randint(5,10)
        environment -= random.randint(3,7)
    elif choice == 3:
        money -= 30
        environment += 10
    elif choice == 4:
        money -= 10
        environment += random.randint(1,3)
    elif choice == 5:
        environment += random.randint(1,3)
    else:
        print("Invalid choice!")

    return money, productivity, environment

# Main game

display_intro()
money = 100
productivity = 0
environment = 50

for _season in range(10):
    money, productivity, environment = farming_season(money, productivity, environment)

    print("At the end of the season, Your money is now $"+str(money))
    print("Productivity Score: "+str(productivity))
    print("Environment Score: "+str(environment))

    print("Next season is about to start. Please wait...")
    time.sleep(2)

print("Game Over. Your final productivity Score: "+str(productivity))
print("Your final environment score: "+str(environment))
