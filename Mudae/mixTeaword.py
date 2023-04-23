import random

filename = "fulldictionary.txt"
input_string = input("Enter a string to search for: ")

matching_lines = []
with open(filename, "r") as f:
    for line in f:
        if input_string in line:
            matching_lines.append(line.strip())

if matching_lines:
    # Sort matching_lines in descending order based on string length
    sorted_lines = sorted(matching_lines, key=len, reverse=True)
    
    #redtea
    longest_line = sorted_lines[0]
    print(f"Longest matching string: {longest_line}")
    #yellowtea
    for i in range(0, 4):
        random_line = random.choice(matching_lines)
        print(random_line)
    #greentea
    sorted_lines = sorted(matching_lines, key=len)
    shortest_line = sorted_lines[0]
    print(f"Shortest matching string: {shortest_line}")
    
else:
    print("No matching strings found.")