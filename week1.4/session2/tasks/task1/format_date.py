# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator):
    # complete your code here
    formatted_date = day + separator + month + separator + year
    return formatted_date


# Write code to test the function with separators such as "/", ":", "."
day = input("Enter day number: ")
month = input("Enter month number: ")
year = input("Enter year number: ")
print(format_data(day, month, year, "|"))