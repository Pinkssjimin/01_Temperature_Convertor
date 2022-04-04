# data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# get filename, cant be blanked / invalid
# assume valid data for now
filename = input("enter a filename (leave off the extension): ")

# add .txt suffix!
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for i in data:
    f.write(i + "\n")

# close file
f.close()
