import tkinter as tk
import tkinter.ttk as ttk
from typing import Final
from functools import partial
import RNG

EXTERNAL_FRAME_PADDING: Final[int] = 5

def launchGUI():
    window = tk.Tk()

    #Leave padding as is for now, and once funcitonality is fully implemented (or mostly) then make the app look nice
    #TODO: Move items around to a new function (such as init for the GUI) or file to clean up code

    window.geometry("600x400")
    window.rowconfigure(0, weight=0) 
    window.rowconfigure(1, weight=1) 
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3) 

    # Header frame
    frameHeader = tk.Frame(master=window, relief=tk.RAISED, width=100, height=75, bg="red")
    frameHeader.grid(row=0, column=0, sticky="ew", columnspan=2, padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    # Button frames
    frameButtons = tk.Frame(master=window, bg="lime")
    frameButtons.grid(row=1, column=0, sticky="nsw", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    # Third frame for the rest of the space
    frameRollResult = tk.Frame(master=window, bg="blue")
    frameRollResult.grid(row=1, column=1, sticky="nsew", padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)


    labelHeader = tk.Label(master=frameHeader, text="Dice Roller App")
    labelHeader.pack(pady=10)

    extraLabel = tk.Label(master=frameButtons, text="I'm in Frame B")
    extraLabel.grid(row=0, column=0, padx=10, pady=3)

    displayLabel = tk.Label(master=frameRollResult, text="-1")
    displayLabel.pack(expand=True)

    button = tk.Button(master=frameButtons, text="click me!")
    button.grid(row=1, column=0, pady=20)
    button.bind("<Button-1>", partial(temp_handler, label=displayLabel)) #Button 1 = left click, 2 = middle mouse and 3 = right click

    window.mainloop()


def temp_handler(event, label):
    newRoll = RNG.generateNumbers(20,1)
    label["text"] = str(newRoll[0])
    
if __name__ == "__main__":
    launchGUI()
    