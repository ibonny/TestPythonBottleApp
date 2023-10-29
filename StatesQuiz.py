import os
import random

stateList = []
capitalList = []

try:
    stateFile = open("states.txt", "r")
except:
    print("Cannot open states file.")

    exit(1)
else:
    for items in stateFile:
        stateList.append(items.strip())

    stateFile.close()

try:
    capitalFile = open("capitals.txt", "r")
except:
    print("Cannot open capitals file.")

    exit(1)
else:
    for items in capitalFile:
        capitalList.append(items.strip())

    capitalFile.close()

ans = 0

while ans != 6:
    statepick = random.randint(0, 49)
    choicelist = []
    # Set the correct answer.
    choicelist.append(statepick)
    choicecount = 0
    while choicecount < 4:
        x = random.randint(0, 49)
        if x != statepick and x not in choicelist:
            choicelist.append(x)
            choicecount = choicecount+1

    random.shuffle(choicelist)
    correct = choicelist.index(statepick)+1
    print("What is the capital of %s?" % stateList[statepick])
    print("1)", capitalList[choicelist[0]])
    print("2)", capitalList[choicelist[1]])
    print("3)", capitalList[choicelist[2]])
    print("4)", capitalList[choicelist[3]])
    print("5)", capitalList[choicelist[4]])
    print("6) Quit")

    ans = int(input("Enter your response: "))
    if ans == correct:
        print("Correct")
    elif ans in range(1, 5):
        print("Incorrect")
    elif ans == 6:
        print("Goodbye")
    else:
        print("Incorrect response.")
