import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names

num_names = int(input("How many names would you like to choose? "))

# from the list, avoiding any duplicate choices

chosen_names = random.sample(names, num_names)
# chooses a random sample of names from the list without replacement, ensuring no duplicates.
# Display the chosen names, one per line
for name in chosen_names:
    print(name)
