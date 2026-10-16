"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
 "when inputs are not valid number such as letter...etc"
2. When will a ZeroDivisionError occur?
 "denominator is 0"
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
