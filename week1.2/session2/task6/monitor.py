# Week 1.2, Session 2: Task 6
celsius = int(input("Please enter the temperature in Celsius: "))
pressure = int(input("Please enter the pressure in PSI: "))
status = int(input("Please enter the status (1 for active, 0 for inactive): "))

def pressure_check(pressure, status):
    if pressure > 100 and status == 1:
        print("Warning: High pressure detected")
        print("Run some maintenance")
        quit()
    elif 70 < pressure <= 100 and status == 1:
        print("Pressure is at normal range.")
    elif pressure <= 70 and status == 1:
        print("Pressure is low, everythings normal")

if celsius > 80 and status == 1:
    pressure_check(pressure, status)
    print("Warning: High temperature detected!")
    print("Please turn off the machine or die")
    quit()
elif 50 < celsius <=80 and status == 1:
    pressure_check(pressure, status)
    print("Warning: Temperature is at normal range.")
elif celsius <= 50 and status == 1:
    pressure_check(pressure, status)
    print("Temperature is low, youre fine")
else:
    print("Machine is off, no warnings.")