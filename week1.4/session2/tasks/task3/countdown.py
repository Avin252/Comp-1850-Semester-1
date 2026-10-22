# Week 4, Session 2: 

# Given incomplete recursive function countdown with a docstring.
# Your task is to complete the function based on the details in the docstring.

def countdown(n):
    """
    This recursive function prints numbers from n down to 0.

    Args:
        n : int, positive integer representing the starting number.

    Returns:
        None, prints the countdown sequence from n to 0.
    """

    # Complete your code here
    # base case
    if n == 0:
        print(n)
    # recursive case
    else:
        print(n)
        countdown(n - 1)

# check if correct output is produced
countdown(30)    # 30 ... 0 (Note: each number is printed in a separate line)
countdown(5)     # 5 ... 0  (Note: each number in printed in a separate line)
countdown(0)

# Once you have completed, your next task is to write an equivalent function that
# uses a loop.
def countdown_loop(n):
    while n > 0:
        print(n)
        n = n -1
    else:
        print(n)


countdown_loop(30)   
countdown_loop(5)
countdown_loop(0)