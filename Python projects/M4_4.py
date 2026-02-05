import random
number = random.randint(1, 10)
print ("I'm thinking of a number from 1 to 10")
while True:
    guess = int(input(" What is your guess: "))
    if guess > number:
        print ("Too high!")
    elif guess < number:
        print ("Too low!")
    else:
        print ("Correct!")
        break