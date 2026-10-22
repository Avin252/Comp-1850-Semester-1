"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Avin Poudyal
"""

states_og = {"red": 4, "red_amber": 3, "green": 5, "amber": 3}

systime = 0
maxtime = int(input())

state_colours = ["red", "red_amber", "green", "amber"]
state_index = 0
state = state_colours[state_index]
time_in_state = 0

print(f"Time {systime:03} State {state}")
# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime < maxtime:

    if time_in_state >= states_og[state]:
        state_index = (state_index + 1) % len(state_colours)
        state = state_colours[state_index]
        time_in_state = 1
    else:
        time_in_state += 1

    print(f"Time {systime:03} State {state}")
    systime += 1

# At the end of each step you should output the time and state using the statement on line 14