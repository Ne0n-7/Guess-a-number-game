import random  # random library

random_number = random.randint(1, 20)  # generating a random number between 1 and 20, for easy level

guess = int(input("Can you guess a number between 1 and 20? "))  # asking the input from the user

tries = 5  # number of tries in the level

#  logic
#  checking random number and tries left.
while guess != random_number and tries > 0:

    #  giving clue to the user the guessed number is too high
    if guess > random_number:
        print("Too high")
    #  else printing out it was too low.
    else:
        print("Too low")

    #  indicating the number of tries left
    print("You have " + str(tries) + " tries left")
    # again getting input from the user for the loop to break
    guess = int(input("Guess again: "))
    #  decrementing the tries' counter for the while loop to end when they out of try.
    tries -= 1

    #  condition to show the final result, if the guessed dumber is still out of tries.
    if guess != random_number and tries == 0:
        print("You lost")
    #  printing out the final result.
    elif guess == random_number:
        print("Congratulations!")

#  the final message and program stops.
print("Have a nice day, Bye")
