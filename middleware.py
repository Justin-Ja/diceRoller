from typing import Final
from functools import partial
import RNG

DICE_SIDES_KEYS = [
    "4",
    "6",
    "8",
    "10",
    "12",
    "20",
    "100"
]

class Middleware:

    def __init__(self, totalDice, diceToRoll):
        self.totalDice = totalDice
        #Create a dictionary with keys of DICE_SIDES_KEYS and values of diceToRoll (which in our case will always be 0)
        self.diceToRoll = {key: diceToRoll for key in DICE_SIDES_KEYS}

    #sets all values in the dict to 0, simulates a reset of what the user wants to roll
    def clearDiceToRoll(self):
        self.totalDice = 0
        self.diceToRoll = {key: 0 for key in DICE_SIDES_KEYS}

    #Get all values for each dice being rolled and pass that info back to display/the event handler that called it
    def getRolledDiceValues(self):
        print("WIP")
    