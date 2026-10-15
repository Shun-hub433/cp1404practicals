"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"

#celsius = float(input("Celsius: "))
def c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

#fahrenheit = float(input("Fahrenheit : "))
def f_to_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = c_to_f(celsius)
            print(result)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            result = f_to_c(fahrenheit)
            print(result)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")
main()
"""
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit : "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
"""