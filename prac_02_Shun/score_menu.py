"""
print menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        print invalid input error message
    print menu
    get choice
<do final thing, if needed>
"""
from score import determine_score
MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
"""
def get_valid_score():
    score = float(input("enter valid score:"))
    while score <0 or score >100:
        print("invalid")
        score = float(input("enter valid score:"))
    return score

def main():
    score = get_valid_score()
    print(MENU)
    choice = input("Enter choice:").upper()
    while choice != "Q":
        if choice =="G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score(score)
            print(f"score {score} is {result}")
        elif choice =="S":
            print("*" *int(score))
        else:
            print("invalid option")

        print(MENU)
        choice = input("Enter choice:").upper()
main()





