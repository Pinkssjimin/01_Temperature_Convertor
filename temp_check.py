def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))

            if response < low:
                print("Too Cold!")
            else:
                return response

        except ValueError:
            print("Please enter a number")

# main Routine
# run this code twice (for two valid responses in test plan)
low = -273
number = temp_check(low)
print("y0u chose {}".format(number))

number = temp_check(-459)
print("You chose {}".format(number))
