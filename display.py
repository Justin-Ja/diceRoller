import tkinter as tk
import tkinter.ttk as ttk
from typing import Final
from functools import partial
import RNG

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
    window = tk.Tk()

    #Leave padding as is for now, and once funcitonality is fully implemented (or mostly) then make the app look nice
    #TODO: Move items around to a new function (such as init for the GUI) or file to clean up code

    window.geometry("700x475")
    window.rowconfigure(0, weight=0) 
    window.rowconfigure(1, weight=1) 
    window.columnconfigure(0, weight=0)
    window.columnconfigure(1, weight=1) 
    window.columnconfigure(2, weight=2) 

    frameHeader = tk.Frame(master=window, relief=tk.RAISED, width=100, height=75, bg="red")
    frameHeader.grid(row=0, column=0, sticky="ew", columnspan=3, padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    frameButtons = tk.Frame(master=window, bg="lime")
    frameButtons.grid(row=1, column=0, sticky="nsw", pady=EXTERNAL_FRAME_PADDING, padx=EXTERNAL_FRAME_PADDING)

    frameRollResult = tk.Frame(master=window, bg="blue")
    frameRollResult.grid(row=1, column=2, sticky="nesw", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    #temp frame
    frameRollDice = tk.Frame(master=window, bg="orange")
    frameRollDice.grid(row=1, column=1, sticky="nsw", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    labelHeader = tk.Label(master=frameHeader, text="Dice Roller App")
    labelHeader.pack(pady=10)

    displayLabel = tk.Label(master=frameRollResult, text="-1")
    displayLabel.pack(expand=True)

    #Creates and binds each button to roll TODO: Can we move this out to its own thing?
    idx = 0
    for idx, (text, sides) in enumerate(DICE_SIDES.items(), start=1):
        button = tk.Button(master=frameButtons, text=f"Add {text}")
        button.grid(row=idx, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)
        button.bind("<Button-1>", partial(getRollValue, label=displayLabel, sides=sides, rolls=1))
   
    idx = idx + 1
    resetButton = tk.Button(master=frameButtons, text=f"Reset roll")
    resetButton.grid(row=idx, column=0, padx=BUTTON_PADX, pady=BUTTON_PADY)

    rollButton = tk.Button(master=frameRollDice, text=f"Roll dice")
    rollButton.grid(row=0, column=0, pady=BUTTON_PADY)

    window.mainloop()


#TODO: When adding in update to allow mulitple roles, we'll need to overhaul this.
#Consider a middle man between display and RNG to maintain number of dice needing to be rolled

def getRollValue(event, label, sides, rolls):
    newRoll = RNG.generateNumbers(sides, rolls)
    #add a label at top of blue frame and say "Rolled x dy di(c)e"
    label["text"] = str(newRoll[0])
    
if __name__ == "__main__":
    launchGUI()
    