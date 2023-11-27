import random

# Initial conditions
water_quality = 100
air_quality = 100
soil_quality = 100
biodiversity = 100
farm_health = 100
money = 10000
seasons = ["Spring", "Summer", "Autumn", "Winter"]

# Actions and outcomes
actions = {
    "Plant drought-resistant crops": {"water_quality": 5, "farm_health": -10, "money": -2000 },
    "Use a large amount of pesticides": {"biodiversity": -30, "soil_quality": -20, "farm_health": 30, "money": -3000},
    # more actions...
}

# Run the game
for season in seasons:
    print(f"\nIt's now {season}. Here are the current stats:")
    print("Water quality:", water_quality)
    print("Air quality:", air_quality)
    print("Soil quality:", soil_quality)
    print("Biodiversity:", biodiversity)
    print("Farm health:", farm_health)
    print("Money:", money)

    print("\nHere are the actions you can take:")
    for i, action in enumerate(actions.keys(), start=1):
        print(f"{i}. {action}")

    choice = input("\nWhat do you want to do? Enter the number of your choice: ")
    action = list(actions.keys())[int(choice) - 1]

    results = actions[action]
    water_quality += results.get("water_quality", 0)
    air_quality += results.get("air_quality", 0)
    soil_quality += results.get("soil_quality", 0)
    biodiversity += results.get("biodiversity", 0)
    farm_health += results.get("farm_health", 0)
    money += results.get("money", 0)

    # Random events
    event_chance = random.randint(1, 100)
    if event_chance <= 10:
        print("\nOh no, a pest invasion! Your farm health decreases.")
        farm_health -= 20
    elif event_chance <= 20:
        print("\nGreat weather this season! Your farm health increases.")
        farm_health += 10

    # Ensure no stats go below 0 or above 100
    water_quality = max(0, min(water_quality, 100))
    air_quality = max(0, min(air_quality, 100))
    soil_quality = max(0, min(soil_quality, 100))
    biodiversity = max(0, min(biodiversity, 100))
    farm_health = max(0, min(farm_health, 100))
    money = max(0, money)