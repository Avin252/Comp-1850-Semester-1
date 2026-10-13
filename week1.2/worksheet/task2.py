# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

numbers_list = read_numbers()
if len(numbers_list) == 0:
    sys.exit("Error: no numbers provided")
else:
    print(f"Minimum: {min(numbers_list)}")
    print(f"Maximum: {max(numbers_list)}")
    print(f"Mean: {sum(numbers_list) / len(numbers_list)}")
    numbers_list = sorted(numbers_list)
    length = len(numbers_list)
    if length % 2 == 0:
        pos1 = numbers_list[int((length / 2))]
        pos2 = numbers_list[int((length / 2) - 1)]
        median = (pos1 + pos2) / 2
    else:
        mid = int((length / 2) + 0.5) - 1
        print(mid)
        median = numbers_list[mid]
    print(f"Median: {median}")