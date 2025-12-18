import random
import os
import sys


SIZE = 9

if len(sys.argv) > 1:
    SIZE = sys.argv[1]


def printMultiplicationColumn(pickedNumber):
    for i in range(1, SIZE + 1):
        print(f"{pickedNumber} x {i} = {pickedNumber*i}")

def giveMultiplicationQuizes(pickedNumber):
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0

    numberList = list()
    for i in range(1,SIZE + 1):
        numberList.append(i)

    random.shuffle(numberList)
    mistakes = list()

    for i in numberList:
        while(True):
           
            try:
                answer = int(input(f"{pickedNumber} X {i} = "))
                if answer == pickedNumber * i:
                    score += 1
                    print("Correct!")
                else:
                    print("Wrong answer. Sorry.")
                    print(f"{pickedNumber} X {i} = {pickedNumber*i}")
                    print("Try to memorise it, and you will be tested later again.")
                    mistakes.append(i)
                break

            except ValueError:
                # Handle non-integer input
                print("Invalid input! Try entre a number.")
                continue
    
    if len(mistakes) > 0:
        print("You got these questions wrong, please review the answers.")
        for j in mistakes:
            print(f"{pickedNumber} X {j} = {pickedNumber*j}")
    return score
    


childName = input("Hi there, I am Times Bot. What's your name? ")
print(f"Hello {childName}, let's learn multiplication table.")
while(True):
    pickedNumber = -1
    while pickedNumber not in range(1, 13):
        try:
            pickedNumber = int(input(f"Pick a number between 1 and {SIZE} to learn: "))
        except:
            print("That's not a number.")
            continue

    print(f"Ok, let us learn the multipication of {pickedNumber}.")
    printMultiplicationColumn(pickedNumber)

    userInput = input("Press Enter when you are ready for the quizes, type [back] to choose another number, or type [exit] to quit. ")
    if "exit" in userInput.lower():
        sys.exit()
    if "back" in userInput.lower():
        continue

    score = 0
    while(score != SIZE):
        score = giveMultiplicationQuizes(pickedNumber)
        if score == SIZE:
            print(f"Great job, you got all the questions correct for multiplication of {pickedNumber}. Show it to your grownups.")
           
        else:
            print(f"You got {score} questions right. Let us try again.")
        userInput = input("Press Enter to continue, [back] to pick another number, or type [exit] to quit. ")
        if "back" in userInput:
            break
        if "exit" in userInput.lower():
            sys.exit()
        

    

        



