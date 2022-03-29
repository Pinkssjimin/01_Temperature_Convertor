def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Entera number: "))

            if response < low:
                print("Too Cold!")
            else:
                return response

        except ValueError:
            print("Please enter a number")

# main rountine
