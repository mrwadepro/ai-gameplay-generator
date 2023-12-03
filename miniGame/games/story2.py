import random

print("Welcome to Terminal Trader!")
print("Buy low, sell high, and become the wealthiest trader.")
print("Enter 'Trade' to trade, 'Travel' to change cities, 'Check' to check status.")

# Initialize game state variables
cities = ["Boston", "New York", "Chicago"]
commodities = ["Gold", "Silver", "Diamond"]
player_commodities = {commodity: 0 for commodity in commodities}
player_wealth = 1000.0
current_city = random.choice(cities)
market_prices = {commodity: random.uniform(10.0, 100.0) for commodity in commodities}
days = 0

def trade():
    global player_wealth
    print("Enter commodity name and quantity (e.g., 'Gold 10'). Enter 'Done' to finish trading.")
    while True:
        command = input('> ').split()
        if command[0].capitalize() == 'Done':
            break
        commodity, quantity = command[0], int(command[1])
        cost = market_prices[commodity] * quantity
        if cost > player_wealth:
            print("You can't afford this.")
        else:
            player_commodities[commodity] += quantity
            player_wealth -= cost

def travel():
    global current_city, market_prices, days
    print("Enter city name to travel (e.g., 'New York').")
    city = input('> ')
    if city.capitalize() in cities:
        current_city = city.capitalize()
        print("Traveling to", city,"...")
        days += 1
        # Update market prices
        for commodity in commodities:
            market_prices[commodity] = random.uniform(10.0, 100.0)
    else:
        print("City not in database. Please check the spelling")

def check_status():
    print("Wealth:", player_wealth)
    print("Commodities:", player_commodities)
    print("Current City:", current_city)
    print("Days:", days)

actions = {"Trade": trade, "Travel": travel, "Check": check_status}

while True:
    print("\nEnter command (Trade/Travel/Check/Quit):")
    command = input('> ')
    if command.capitalize() == 'Quit':
        break
    elif command.capitalize() in actions:
        actions[command.capitalize()]()
    else:
        print("Unknown command.")