filename = "dictionary7.txt"
input_string = input("Enter a string to search for: ")

with open(filename, "r") as f:
    for line in f:
        if input_string in line:
            print(line.strip())