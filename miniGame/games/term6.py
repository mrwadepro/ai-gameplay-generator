

import time

class Farm:
    def __init__(self, name, region):
        self.name = name
        self.region = region
        self.soil_health = 100
        self.water = 100
        self.air_quality = 100
        self.insects = 100
        self.money = 100
        self.crop = ""

    def print_status(self):
        print(f"\
Status of {self.name}:")
        print(f"Soil Health: {self.soil_health}")
        print(f"Water: {self.water}")
        print(f"Air Quality: {self.air_quality}")
        print(f"Insects: {self.insects}")
        print(f"Money: {self.money}")
        print(f"Crop: {self.crop}")

    def plant_crop(self, crop):
        if self.crop:
            print("\
You\'ve already planted a crop this season. Harvest it before planting a new one.")
        else:
            self.crop = crop
            print(f"\
You\'ve planted {crop}. Good luck!")
            self.soil_health -= 10
            self.water -= 10

    def use_pesticide(self):
        if not self.crop:
            print("\
Plant a crop first before using pesticide.")
        else:
            print("\
You\'ve used pesticide. Your crop yield will increase but it could harm the ecosystem.")
            self.insects -= 15
            self.air_quality -= 10

    def harvest_crop(self):
        if not self.crop:
            print("\
There is nothing to harvest.")
        else:
            print(f"\
You\'ve harvested {self.crop}. Time to sell!")
            if self.insects > 50 and self.water > 50:
                self.money += 20
            else:
                self.money += 10
            self.crop = ""

    def check_balance(self):
        if self.water <= 0 or self.soil_health <= 0 or self.insects <= 0:
            print("\
Your farm is out of balance! Game Over.")
            return False
        return True


def main():
    print("\
Welcome to EcoCrop! Maintain the balance of your farm by managing your resources wisely.")
  
    name = input("\
Enter your farm name: ")
    region = input("Choose your farming region: ")
    farm = Farm(name, region)

    while True:
        farm.print_status()
        print("\
Choose an action: ")
        print("1. Plant Crop")
        print("2. Use Pesticide")
        print("3. Harvest Crop")
        choice = input("Enter your choice: ")

        if choice == "1":
            crop = input("Enter the type of crop to plant: ")
            farm.plant_crop(crop)
        elif choice == "2":
            farm.use_pesticide()
        elif choice == "3":
            farm.harvest_crop()

        if not farm.check_balance():
            break

if __name__ == "__main__":
    main()
