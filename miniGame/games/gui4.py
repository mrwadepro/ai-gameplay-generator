
import tkinter as tk
from tkinter import messagebox

class Commodity:
    """ A simple class representing farm commodities """

    def __init__(self, name, water_need, labor_need):
        self.name = name
        self.water_need = water_need
        self.labor_need = labor_need


class Region:
    """ A class representing a geographical region """

    def __init__(self, name):
        self.name = name
        self.commodities = []

    def add_commodity(self, commodity):
        self.commodities.append(commodity)

class Player:
    """ A class representing a player """

    def __init__(self, water, labor):
        self.score = 0
        self.water = water
        self.labor = labor

class GameWindow(tk.Tk):
    """ Main class for the Game GUI window """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Georgia\'s Bounty Hunt')
        
        # Initialize game variables
        # Assigns player with initial resources of 100 units of water and labor each
        self.player = Player(water=100, labor=100)
        
        # Variable that holds all available commodities with their respective needs
        self.commodities = [Commodity("Peanuts",20,10), Commodity("Cotton",15,20), Commodity("Poultry",30,40), Commodity("Corn",25, 15)]

        # Variable that holds all Georgian regions
        self.regions = [Region("Coastal Plains"), Region("Piedmont"), Region("Blue Ridge"), Region("Ridge and Valley"), Region("Appalachian Plateau")]

        # Initialize controls
        # Create listboxes for selecting commodities and regions
        self.commoditySelect = tk.Listbox(self, exportselection=0)
        for c in self.commodities: self.commoditySelect.insert(tk.END, c.name)
        self.regionSelect = tk.Listbox(self, exportselection=0)
        for r in self.regions: self.regionSelect.insert(tk.END, r.name)
        
        # Button to confirm the selection of commodities and their placement
        self.playButton = tk.Button(self, text="Play", command=self.play)

        # Label to display the current resources of the player
        self.statsLabel = tk.Label(self, text="Water: 100, Labor: 100")

        # Place controls
        # Adding widgets to the window
        self.commoditySelect.pack(padx=10, pady=10)
        self.regionSelect.pack(padx=10, pady=10)
        self.playButton.pack(padx=10, pady=10)
        self.statsLabel.pack(padx=10, pady=10)

    def play(self):
        """ The main function that runs the game logic upon clicking the 'play' button """
      
        # Get user choices
        # Extract selected items from the listboxes
        cIdx = self.commoditySelect.curselection()
        rIdx = self.regionSelect.curselection()

        # Check if a commodity and region have been selected. If not, display an error message.
        if len(cIdx) == 0 or len(rIdx) == 0: 
            messagebox.showinfo('Error', 'You need to select both a commodity and a region.')
            return

        commodity = self.commodities[cIdx[0]]
        region = self.regions[rIdx[0]]

        # Check if user has enough resources
        # If not, the game ends.
        if self.player.water < commodity.water_need or self.player.labor < commodity.labor_need:
            messagebox.showinfo('Game Over', 'You have run out of resources.')
            self.quit()
            return

        # If yes, deduce needs of placed commodity from player resources.
        self.player.water -= commodity.water_need
        self.player.labor -= commodity.labor_need

        # place the selected commodity on the selected region
        region.add_commodity(commodity)

        # Update Resources label.
        self.statsLabel.config(text=f"Water: {self.player.water}, Labor: {self.player.labor}")

# Create and run the game window
window = GameWindow()
window.mainloop()
