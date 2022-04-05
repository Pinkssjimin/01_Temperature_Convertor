from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Convertor:
    def __init__(self):

        # Formatting variables...
        background_colour = "light blue"

        # in actual program this is black and is populated with user calculations
        self.all_calc_list = ['1 degrees F is -17.2 degrees C',
                              '1 degrees C is 33.8 degrees F',
                              '0 degrees F is -17.8 degrees C',
                              '100 degrees F is 37.8 degrees C',
                              '200 degrees F is 93.3 degrees C',
                              '35 degrees F is 1.7 degrees C',
                              '2 degrees F is -16.7 degrees C',
                              '234 degrees F is 112.2 degrees C',
                              '10 degrees F is -12.2 degrees C']

        # converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_colour,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_colour,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_history = history(self)
        get_history.history_text.configure(text="History text goes here")


class history:
    def __init__(self, partner):

        background = "green"

        #disable history button
        partner.history_button.config(state=DISABLED)

        #Set up child window (ie: history box)
        self.history_box = Toplevel()

        #set uo GUI Frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        #Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        #history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                       "calculations. please use the export "
                                       "button to create a text file of all "
                                       "your calculations for this session",
                                  font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background, wrap=250,
                                  padx=10, pady=10, fg="maroon")
        self.history_text.grid(row=1)

        # history output goes here (row 2)

        # export / dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.export_dismiss_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
