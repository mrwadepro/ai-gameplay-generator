
import random

class Region:
    def __init__(self, name, environment, crops):
        self.name = name
        self.environment = environment
        self.crops = crops

regions = [
    Region("Coastal Plains", "Hot and humid climate", ["Peanuts", "Onions", "Cabbage"]),
    Region("Piedmont", "Mild climate with rich soil", ["Peaches", "Apples", "Wheat"]),
    Region("Blue Ridge", "Cool climate with high rainfall", ["Potatoes", "Peppers", "Tomatoes"])
]

class Player:
    def __init__(self, money):
        self.money = money

player = Player(1000) #starting money

def main():
    print("Welcome to Georgia Growers!")
    print("In this game, you will choose a region in Georgia to farm. Based on the region\'s environment,"
          " you\'ll select the crops to cultivate. Your goal is to make as much money as possible."
          " Let\'s begin!")

    for i, region in enumerate(regions, 1):
        print(f"{i}. {region.name} ({region.environment})")

    choice = int(input("Which region do you want to farm in? ")) - 1
    selected_region = regions[choice]

    print(f"You have chosen {selected_region.name}. Here are the crops you can grow: {','.join(selected_region.crops)}")
    crop = input("Which crop do you want to grow? ")

    if crop not in selected_region.crops:
        print("Invalid crop choice, please choose from the list!")
        return

    cost = random.randint(50, 100) #random cost for crop
    if player.money < cost:
        print("You do not have enough money to grow this crop.")
        return

    player.money -= cost

    print(f"You have chosen to grow {crop}. It cost you {cost} to plant. Let\'s see how it grows!")
    random_event(selected_region, crop)

def random_event(region, crop):
    events = ["drought", "flood", "normal"]
    event = random.choice(events)

    if event == "drought" and region.environment == "Hot and humid climate":
        print("There was a drought. Your crop did not do well.")
        player.money -= 50
    elif event == "flood" and region.environment == "Cool climate with high rainfall":
        print("There was a flood. Your crop did not do well.")
        player.money -= 50
    else:
        print("The weather was good for your crops. You made a profit!")
        player.money += 200

    print(f"Game Over! Your final balance is {player.money}.")

if __name__ == "__main__":
    main()
