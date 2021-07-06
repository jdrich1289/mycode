# STEP    DIRECTIONS
# 1.     Create a directory called tempconvert and a Python program called temperature.py
# 2.     Create two variables:  fahrenheit and celsius
# 3.     Assign a starting value to fahrenheit (some number that makes sense)
# 4.      Use the formula to convert fahrenheit to celsius and assign the value to the variable celsius
# 5.      Print the results to the console (screen).  
# 6.     Run the program and let me know if you ran into issues.   
# Use the following formula
#     celsius = (fahrenheit -32) * 5/9
from welcome import welcome

def to_fahrenheit(celsius):
    fahrenheit = float(celsius * 1.8 + 32)
    return fahrenheit


def to_celsius(fahrenheit):
    celsius = float((fahrenheit -32) * 5/9)
    return celsius


def main():
    keep = 1
    while keep != 0:
        selection = input("1) for Fahrenheit to Celsius conversion \n2) for Celsius to Fahrenheit conversion \nq) to exit program\nEnter your selection (1/2/q): ")
        print()
        if selection.lower() == 'q':
            print("Exitting the program. Thank you!")
            break
        elif selection == '1':
            temper = float(input("Enter the temperature you want to convert: "))
            cel = to_celsius(temper)
            print(round(cel, 2), "degrees fahrenheit.")
            print()
            keep = 1
        elif selection == '2':
            temper = float(input("Enter the temperature you want to convert: "))
            fah = to_fahrenheit(temper)
            print(round(fah, 2), "degrees celsius.")
            print()
            keep = 1
        else:
            print("------Enter the correct selection (1/2/q)------")
            keep = 1
         

welcome()
main()
