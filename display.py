import tkinter as tk
from typing import Final
from functools import partial
import middleware

EXTERNAL_FRAME_PADDING: Final[int] = 5
BUTTON_PADX: Final[int] = 5
BUTTON_PADY: Final[int] = 10

TITLE_BLUE: Final[str] = "#4B9AFF"
LIGHT_GRAY: Final[str] = "#CCCCCC"

DICE_SIDES: Final = {
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
    
    #Creation of all the frames
    frameHeader = tk.Frame(master=window, relief=tk.RAISED, width=100, height=75, bg=TITLE_BLUE)
    frameHeader.grid(row=0, column=0, sticky="ew", columnspan=3, padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    frameButtons = tk.Frame(master=window, bg=LIGHT_GRAY)
    frameButtons.grid(row=1, column=0, sticky="nsw", pady=EXTERNAL_FRAME_PADDING)

    frameRollResult = tk.Frame(master=window, bg=LIGHT_GRAY)
    frameRollResult.grid(row=1, column=2, sticky="nesw", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    frameRollDice = tk.Frame(master=window, bg=LIGHT_GRAY)
    frameRollDice.grid(row=1, column=1, sticky="nsw", pady=EXTERNAL_FRAME_PADDING)

    #Creation of each label
    labelHeader = tk.Label(master=frameHeader, text="Dice Roller App", bg=TITLE_BLUE, font=("Roboto", 18, "bold"))
    labelHeader.pack(pady=10)

    labelDiceToRoll = tk.Label(master=frameRollDice, text="Dice to roll: 0", bg=LIGHT_GRAY, font=("Roboto", 12))
    labelDiceToRoll.grid(row=1, column=0, padx=10, pady=10)

    labelDisplayTotalRoll = tk.Label(master=frameRollResult, text="You rolled: ", bg=LIGHT_GRAY, font=("Roboto", 12))
    labelDisplayTotalRoll.pack(expand=True)

    labelDisplayAllGeneratedValues = tk.Label(master=frameRollResult, text="", bg=LIGHT_GRAY, font=("Roboto", 12))
    labelDisplayAllGeneratedValues.pack(expand=True)

    #Creates and binds each button to an event handler
    idx = 0
    for idx, (text, sides) in enumerate(DICE_SIDES.items(), start=1):
        button = tk.Button(master=frameButtons, text=f"Add {text}", bd=2, relief=tk.RAISED)
        button.grid(row=idx, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
        button.bind("<Button-1>", partial(handleAddDiceToRoll, sides=sides, labelToRoll=labelDiceToRoll, middleware=middlewareInstance))
    
    idx = idx + 1
    resetButton = tk.Button(master=frameButtons, text="Reset roll", bd=2, relief=tk.RAISED)
    resetButton.grid(row=idx, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
    resetButton.bind("<Button-1>", partial(handleClearDiceToRoll, labelToRoll=labelDiceToRoll, middleware=middlewareInstance))

    rollButton = tk.Button(master=frameRollDice, text="Roll dice", bd=2, relief=tk.RAISED)
    rollButton.grid(row=0, column=0,  sticky="ew", padx=5, pady=BUTTON_PADY)
    rollButton.bind("<Button-1>", partial(handleRollDice, 
                                labelTotalRolls=labelDisplayTotalRoll, labelAllRolls=labelDisplayAllGeneratedValues, labelToRoll=labelDiceToRoll, middleware=middlewareInstance))

    #Runs the GUI event loop till the program stops
    window.mainloop()


#Handles the setup for the window and relates attributes
def createWindow():
    window = tk.Tk()

    window.title("Dice Roller")
    window.geometry("700x500")
    window.rowconfigure(0, weight=0) 
    window.rowconfigure(1, weight=1) 
    window.columnconfigure(0, weight=0)
    window.columnconfigure(1, weight=1) 
    window.columnconfigure(2, weight=2)     
    
    return window


#Below are all the button event handlers. They call on the middleware to handle updating the logic/values of the program and mainly handle updating labels
def handleAddDiceToRoll(event, sides, labelToRoll, middleware):
    middleware.totalDice = middleware.totalDice + 1
    middleware.diceToRoll[str(sides)] = middleware.diceToRoll[str(sides)] + 1
    labelToRoll["text"] = f"Dice to roll: {middleware.totalDice}"

def handleClearDiceToRoll(event, labelToRoll, middleware):
    middleware.clearDiceToRoll()
    labelToRoll["text"] = "Dice to roll: 0"

def handleRollDice(event, labelTotalRolls, labelAllRolls, labelToRoll, middleware):
    allDiceRolled = middleware.getRolledDiceValues()

    sum = middleware.getSummedValues(allDiceRolled)
    if sum == 0:
        labelTotalRolls["text"] = "You rolled nothing"
        labelAllRolls["text"] = ""
    else:
        strAllRolls = ""
        tempStr = ""
        
        for i, (text, _) in enumerate(DICE_SIDES.items(), start=0):
            if not allDiceRolled[i]:
                continue
            
            for j in range(len(allDiceRolled[i])):
                #This loop turns each sublist into its own string
                if j == 0:
                    tempStr = f"{allDiceRolled[i][j]}"
                else:
                    tempStr = f"{tempStr}, {allDiceRolled[i][j]}"

            #Concats all numbers from a dice to AllRolls to eventually print all the generated values from all the dice rolled to the frontend
            tempStr = f"{tempStr}\n"
            strAllRolls = f"{strAllRolls}{str(text)}: {tempStr}"
            tempStr = ""

        labelAllRolls["text"] = f"All dice rolled: \n{strAllRolls}"

    labelTotalRolls["text"] = f"You Rolled: {sum}"
    labelToRoll["text"] = "Dice to roll: 0"


if __name__ == "__main__":
    print("To run the GUI, run `python3 main.py`, or see the README.md for more info")

    