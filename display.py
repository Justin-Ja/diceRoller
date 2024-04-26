import tkinter as tk
import tkinter.ttk as ttk
from typing import Final
from functools import partial
import RNG
import middleware

EXTERNAL_FRAME_PADDING: Final[int] = 5
BUTTON_PADX: Final[int] = 5
BUTTON_PADY: Final[int] = 10

DICE_SIDES = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20,
    "d100": 100,
}

def launchGUI():
    window = createWindow()
    middlewareInstance = middleware.Middleware(0, 0)
    
    #Leave padding as is for now, and once funcitonality is fully implemented (or mostly) then make the app look nice
    #TODO: Move items around to a new function (such as init for the GUI) or file to clean up code

    frameHeader = tk.Frame(master=window, relief=tk.RAISED, width=100, height=75, bg="red")
    frameHeader.grid(row=0, column=0, sticky="ew", columnspan=3, padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    frameButtons = tk.Frame(master=window, bg="lime")
    frameButtons.grid(row=1, column=0, sticky="nsw", pady=EXTERNAL_FRAME_PADDING, padx=EXTERNAL_FRAME_PADDING)

    frameRollResult = tk.Frame(master=window, bg="blue")
    frameRollResult.grid(row=1, column=2, sticky="nesw", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    frameRollDice = tk.Frame(master=window, bg="yellow")
    frameRollDice.grid(row=1, column=1, sticky="nsw", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    labelHeader = tk.Label(master=frameHeader, text="Dice Roller App")
    labelHeader.pack(pady=10)

    labelDisplayTotalRoll = tk.Label(master=frameRollResult, text="You rolled: ")
    labelDisplayTotalRoll.pack(expand=True)

    #Creates and binds each button to roll 
    #TODO: Can we move this out to its own thing? should it be moved?
    idx = 0
    for idx, (text, sides) in enumerate(DICE_SIDES.items(), start=1):
        button = tk.Button(master=frameButtons, text=f"Add {text}")
        button.grid(row=idx, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
        button.bind("<Button-1>", partial(handleAddDiceToRoll, sides=sides, middleware=middlewareInstance))
    
    idx = idx + 1
    resetButton = tk.Button(master=frameButtons, text="Reset roll")
    resetButton.grid(row=idx, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
    resetButton.bind("<Button-1>", partial(handleClearDiceToRoll, middleware=middlewareInstance))

    rollButton = tk.Button(master=frameRollDice, text="Roll dice")
    rollButton.grid(row=0, column=0, pady=BUTTON_PADY)
    rollButton.bind("<Button-1>", partial(handleRollDice, labelTotalRolls=labelDisplayTotalRoll, middleware=middlewareInstance))

    window.mainloop()


def createWindow():
    window = tk.Tk()

    window.geometry("700x475")
    window.rowconfigure(0, weight=0) 
    window.rowconfigure(1, weight=1) 
    window.columnconfigure(0, weight=0)
    window.columnconfigure(1, weight=1) 
    window.columnconfigure(2, weight=2)     
    
    return window


#Below are all the button event handlers. They call on the middleware to handle updating the logic/values of the program
#TODO: Add a new label to keep track of total number of dice to be rolled for visual feedback
def handleAddDiceToRoll(event, sides, middleware):
    middleware.totalDice = middleware.totalDice + 1
    middleware.diceToRoll[str(sides)] = middleware.diceToRoll[str(sides)] + 1

def handleClearDiceToRoll(event, middleware):
    middleware.clearDiceToRoll()

def handleRollDice(event, labelTotalRolls, middleware):
    allDiceRolled = middleware.getRolledDiceValues()
    print("DICE ROLLED:")
    print(allDiceRolled)

    sum = middleware.getSummedValues(allDiceRolled)
    labelTotalRolls["text"] = f"You Rolled: {sum}"

if __name__ == "__main__":
    launchGUI()
    