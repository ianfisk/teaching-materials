import random

def guessing_game():
    randNumber = random.randint(0,10) #This is how you can get random numbers, pretty easy!

    # Original way of writing the nested logic:
    userInput = int(input("Guess of a number between 0 and 10, you have 2 guesses: "))
    if userInput == randNumber:
        print("You guessed it:",randNumber)
    else:
        if userInput > randNumber:
            print("My number is less than:", userInput)
            userInput = int(input("Guess of a number between 0 and " + str(userInput - 1) + ": "))
            if userInput == randNumber:
                print("You guessed it:",randNumber)
            else:
                print("WRONG, the number is:", randNumber)
        else:
            print("My number is more than:", userInput)
            userInput = int(input("Guess of a number between " + str(userInput + 1) + " and 10: "))
            if userInput == randNumber:
                print("You guessed it:",randNumber)
            else:
                print("WRONG, the number is:", randNumber)

