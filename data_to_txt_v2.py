import re

data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

has_error = "yes"
while has_error == "yes":
    print()
    filename = input("Enter a filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
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

# add .txt suffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for i in data:
    f.write(i + "\n")

# close file
f.close()
