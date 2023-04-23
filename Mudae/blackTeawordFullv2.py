import random

filename = "fulldictionary.txt"
input_string = input("Enter a string to search for: ")

matching_lines = []
with open(filename, "r") as f:
    for line in f:
        if input_string in line:
            matching_lines.append(line.strip())

if matching_lines:
    for i in range(0, 5):
        random_line = random.choice(matching_lines)
        print(random_line)
    
else:
    print("No matching strings found.") 