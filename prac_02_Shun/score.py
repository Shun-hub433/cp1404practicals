"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def determine_score(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result
def main():
    score=random.randint(1,101)
    #score = float(input("Enter score: "))
    result = determine_score(score)
    #print(f"User score {score} is {result}")
    print(f"Random:{score} = {result}")

main()

