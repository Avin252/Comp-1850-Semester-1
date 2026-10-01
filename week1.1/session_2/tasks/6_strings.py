# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # prints out the original entered string
print(f"Modified String 1: {user_string.lower()}") # makes every letter lowercase
print(f"Modified String 2: {user_string.upper()}") # makes every letter uppercase
print(f"Modified String 3: {user_string.strip()}") # ?
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces any 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}") # capitalizes the first letter
print(f"Modified String 6: {user_string[::-1]}") # reverses the inputted string
print(f"Modified String 7: {user_string.title()}") # capitalizes the first letter of every word
print(f"Modified String 8: {len(user_string)}") # shows how many characters including spaces are in the string
print(f"Modified String 9: {user_string.find('a')}") # shows which position the letter 'a' is
print(f"Modified String 10: {user_string.count('a')}") # tells you how many letter 'a' there is in the string
print(f"Modified String 11: {user_string.startswith('Hello')}") # checks to see if the string starts with 'Hello'
print(f"Modified String 12: {user_string.endswith('!')}") # checks to see if the string ends with the '!'
print(f"Modified String 13: {user_string.isalnum()}") # checks if there are any numbers in the string
print(f"Modified String 14: {user_string.isalpha()}") 
print(f"Modified String 15: {user_string.isdigit()}") # checks if the string is just digits and no letters



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!