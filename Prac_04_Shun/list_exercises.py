numbers = []
for i in range(5):
    number = int(input("Number:"))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")

average = sum(numbers)/len(numbers)
print(f"The average number is {average}")



usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
get_username = input("User name:")

if get_username in usernames:
    print("Access granted")
else:
    print("Access denied")