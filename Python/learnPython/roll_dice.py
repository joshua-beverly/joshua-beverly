import random;

roll = random.randint(1,6) ## will return a random number between 1 and 6

#print("The computer rolled a " + str(roll))  ## remember to convert the int to str 

guess = int(input("Guess the dice roll:\n")) ## convert the input to an int so we can 
                                             ## compare guess to roll

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else:
    print("Wrong! They rolled a " + str(roll))

        