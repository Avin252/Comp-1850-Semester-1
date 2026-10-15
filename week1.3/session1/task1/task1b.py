# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# a list is a LIFO structure, so popping gets the last item in the list and goes backwards
# What features of Python does it rely on?