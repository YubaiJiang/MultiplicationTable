import random
import os



def printMultiplicationColumn(pickedNumber):
    for i in range(1, 13):
        print(f"{pickedNumber} x {i} = {pickedNumber*i}")

def giveMultiplicationQuizes(pickedNumber):
    os.system('cls' if os.name == 'nt' else 'clear')
    score = 0

    numberList = list()
    for i in range(1,13):
        numberList.append(i)

    random.shuffle(numberList)

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
                break

            except ValueError:
                # Handle non-integer input
                print("Invalid input! Try entre a number.")
                continue
    return score
    


childName = input("Hi there, I am Times Bot. What's your name? ")
print(f"Hello {childName}, let's learn multiplication table.")
while(True):
    pickedNumber = -1
    while pickedNumber not in range(1, 13):
        pickedNumber = int(input("Pick a number between 1 and 12 to learn: "))

    print(f"Ok, let us learn the multipication of {pickedNumber}.")
    printMultiplicationColumn(pickedNumber)

    input("Press Enter when you are ready for the quizes.")
    

    score = 0
    while(score != 12):
        score = giveMultiplicationQuizes(pickedNumber)
        if score == 12:
            print(f"Great, you got all the questions correct for multiplication of {pickedNumber}. Show it to your grownups.")
        else:
            print(f"You got {score} questions right. Let us try again.")

    

        



