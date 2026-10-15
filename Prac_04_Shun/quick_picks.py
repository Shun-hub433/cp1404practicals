import random
MAX_LINE = 45
MIN_LINE = 1
NUMBER_PER_PICK = 6

get_user_input = int(input("How many quick picks?:"))

for i in range(get_user_input):
    quick_pick = []
    while len(quick_pick) < NUMBER_PER_PICK:
        number = random.randint(MIN_LINE,MAX_LINE)

        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))
