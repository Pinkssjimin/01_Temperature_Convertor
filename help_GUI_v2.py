from tkinter import *
from functools import partial #To prevent unwanted windows

import random


class Convertor:
    def __init__(self):

        #Formatting variables...
        background_colour = "light blue"

        #converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_colour)
        self.converter_frame.grid()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
