import random

# Get user to input how many random numbers they want
input_num = int(input("How many random numbers would you like to generate? "))
# Generate this many random numbers
random_numbers = [random.randint(1, 100) for _ in range(input_num)]
# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for num in random_numbers:
        outfile.write(f"{num}\n")
