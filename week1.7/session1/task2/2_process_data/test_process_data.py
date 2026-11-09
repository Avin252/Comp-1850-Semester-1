# Week 1.7, Session 1: Task 2 - unit test for process_data() 

# Write test functions for the values you have chosen in the equivalence classes
# for testing the functions

# Hint: you should test for empty list, list with a single value, list with multiple values
# and for positive and negative integers


from process_data import process_data


def test_empty_list():
    if not process_data([]) == []:
        raise AssertionError("Expected an empty list for input of an empty list")
    # complete the implementation for
    # testing an empty list
    
    
def test_one_int_list():
    if not process_data([5]) == [5]:
        raise AssertionError("Expected the same list for input of a single integer")
    # complete the implementation for 
    # testing a list with a single integer


def test_multiple_int_list():
    if not process_data([1, 2, 3]) == [1, 2, 3]:
        raise AssertionError("Expected the same list for input of multiple integers")
    # complete the implementation for
    # testing a list with multiple integers

    
    
