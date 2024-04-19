import tkinter as tk
import tkinter.ttk as ttk
from typing import Final
from functools import partial
import RNG

EXTERNAL_FRAME_PADDING: Final[int] = 5
def test():
    window = tk.Tk()

    #Leave padding as is for now, and once funcitonality is fully implemented (or mostly) then make the app look nice
    window.rowconfigure([0,1], weight=1, minsize= 75)
    window.columnconfigure(0, weight=1, minsize= 2)

    headingFrame = tk.Frame(master=window, relief=tk.RAISED, width=100, height=75, bg="red")
    headingFrame.grid(row=0,column=0, padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)

    leftSideFrame = tk.Frame(master=window, width=100, height=50, bg="lime")
    leftSideFrame.grid(row=1,column=0, padx=EXTERNAL_FRAME_PADDING, pady=EXTERNAL_FRAME_PADDING)




    greeting = tk.Label(master=headingFrame, text="Hellow owrld")
    greeting.grid(padx=50, pady=10, sticky='n')

    extraLabel = tk.Label(master=leftSideFrame, text="I'm in Frame B")
    extraLabel.grid(row=0, column=0, padx=10, pady=3) #internal padding, consider using grid instead of pack

    displayLabel = tk.Label(master=window, text="-1")
    displayLabel.grid(padx=10, pady=3)

    button = tk.Button(master=leftSideFrame, text="click me!")
    button.grid(row=1, column=0, pady=20)
    button.bind("<Button-1>", partial(temp_handler, label=displayLabel)) #Button 1 = left click, 2 = middle mouse and 3 = right click
    
    # headingFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # leftSideFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    # masterFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


    window.mainloop()


def temp_handler(event, label):
    print("hello mario")
    newRoll = RNG.generateNumbers(20,1)
    label["text"] = str(newRoll[0])
    
if __name__ == "__main__":
    test()
    