from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import re

class Convertor:
    def __init__(self):

        # Formatting variables...
        background_colour = "light blue"

        # in actual program this is black and is populated with user calculations
        self.all_calc_list = ['1 degrees F is -17.2 degrees C',
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
                                     padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)

# class needs to be capitalised
class History:
    def __init__(self, partner, calc_history):

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
        # generate string from list of calculations...
        history_string = ""
        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history) - item - 1] + "\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) - calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                         "history. You can use the export "
                                         "button to save this data to a "
                                         "text file if desired.")


        # label to display calculation history to user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        # export / dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
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

    def export(self, calc_history):
        # print("You asked for export")
        Export(self, calc_history)
        # get_export.export_text.configure(text="export text goes here")


class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        background = "orange"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Set up child window (ie: export box)
        self.export_box = Toplevel()

        # if users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        #set uo GUI Frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        #Set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        #export text (label, row 1)
        self.export_text = Label(self.export_frame,
                                 text="Enter a filename in the "
                                      "box below an press the "
                                      "Save button to save your "
                                      "calculation history to "
                                      "text file.",
                                 justify=LEFT, width=40, bg=background, wrap=250)
        self.export_text.grid(row=1)

        # warning text (label, row 3)
        self.export_text = Label(self.export_frame, text="If the filename you "
                                                         "enter below already "
                                                         "exists, its contents "
                                                         "will be replaced with "
                                                         "your calculation history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="aral 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # error message labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        # save / cancel frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # save and cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):

        # Regular expression to check filename is valid
        has_error = "no"
        valid_char = "[A-Za-z0-9_]"

        filename = self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            # when space is entered its an error
            elif letter == " ":
                problem = "(no spaces allowed)"
            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
        # when nothing is entered it's a error
        if filename == "":
            problem = "can't be blank"
            has_error = "yes"
        # print the problem message when there's an error
        if has_error == "yes":
            print("Invalid filename - {}".format(problem))
        else:
            print("you entered a valid filename")



        #Dismiss button (row 2)
        self.dismiss_btn = Button(self.export_frame, text="Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_export, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_export(self, partner):
        #Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()
