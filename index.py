import random

correctNumber = random.randint(0, 100)

# print(correctNumber)

attempts = 0

print("**************RULES**************\n1.First rule of the number game is Don't talk anyone about it.\n2.First rule of the number game is Don't talk anyone about it.\n3.Remember higher points means nothing.")

while True:
    userInput = int(input("Please enter a number: "))
    if userInput > correctNumber: 
        if userInput - correctNumber >= 50:
            print("Way too less.")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
        elif userInput - correctNumber >= 25:
            print("Decrease the number!")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
        elif userInput - correctNumber > 10:
            print("You're close but little bit less.")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
        elif userInput - correctNumber <= 10:
            print("You're too close decrease a little bit.")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
    elif userInput < correctNumber:
        if correctNumber - userInput >= 50:
            print("Way too more.")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
        elif correctNumber - userInput >= 25:
            print("Increase the number!")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
        elif correctNumber - userInput > 10:
            print("You're close but little bit more.")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
        elif correctNumber - userInput <= 10:
            print("You're too close increase a little bit.")
            attempts +=1
            print("Your current attempts: %s" % (attempts))
    elif userInput == userInput:
        print("Correct!")
        print("Your score is %s" % (attempts * 5))
        break

