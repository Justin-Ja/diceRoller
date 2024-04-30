from typing import Final
import RNG

DICE_SIDES_KEYS: Final  = [
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
        self.diceToRoll = {key: diceToRoll for key in DICE_SIDES_KEYS}

    #For debugging purposes
    def __str__(self):
        print("Total dice: " + str(self.totalDice))
        print("Dice to roll: " + str(self.diceToRoll))

    #Sets all values in the dict to 0 and totalDice to roll to 0
    def clearDiceToRoll(self):
        self.totalDice = 0
        self.diceToRoll = {key: 0 for key in DICE_SIDES_KEYS}

    #Get all values for each dice being rolled and pass that info back to display/the event handler that called it
    def getRolledDiceValues(self):
        listOfAllRolls = []

        for key in self.diceToRoll:
            value = self.diceToRoll[str(key)]
            listOfAllRolls.append(RNG.generateNumbers(int(key), value))

        self.clearDiceToRoll()
        return listOfAllRolls

    #Takes a list of lists and sums all values in it.
    #Have to assume a list of lists due to allowing multiple different dice to be rolled, the consequence of how getRolledDiceValues is built
    def getSummedValues(self, valuesToSum):
        sum = int(0)
        for values in valuesToSum:
            sum = sum + RNG.calcTotalRoll(values)

        return sum        

    