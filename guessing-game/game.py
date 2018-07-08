from random import randint

random_number = randint(0, 9)
guess = None

while guess != random_number:
    guess = int(input('Pick a number from 0 to 9: '))
    if guess < random_number:
        print('=> Too low')
    elif guess > random_number:
        print('=> Too High!')
else:
    print(f"You Won!\nThe Random number is {random_number}")
