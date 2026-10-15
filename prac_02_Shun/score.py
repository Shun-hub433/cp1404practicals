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

def det_prize(result):
    if result =="Excellent":
        return "You get a prize!"

def main():
    score=random.randint(1,101)
    #score = float(input("Enter score: "))
    result = determine_score(score)
    rr = det_prize(result)
    #print(f"User score {score} is {result}")
    print(f"Random:{score} = {result}")
    print(rr)


main()

