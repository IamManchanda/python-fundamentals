from random import randint

rand_num = randint(0, 2)
if rand_num == 0:
    computer = 'rock'
elif rand_num == 1:
    computer = 'paper'
else:
    computer = 'scissors'

print("The available options are")
print("...rock...")
print("...paper...")
print("...scissors...")

player = input("Hey Player, make your choice: ").lower()
print(f"You played {player}")
print(f"Computer plays {computer}")

def gameResult(winner):
    if winner == 'player': print('Congratulations Player, you won this time')
    elif winner == 'computer': print('Sorry, Computer got it right this time')
    elif winner == 'tie': print("It's a tie")
    else: print('Something went wrong')

if player == computer: gameResult('tie')
elif player == 'rock':
    if computer == 'scissors': gameResult('player')
    elif computer == 'paper': gameResult('computer')
elif player == 'paper':
    if computer == 'rock': gameResult('player')
    elif computer == 'scissors': gameResult('computer')
elif player == 'scissors':
    if computer == 'rock': gameResult('computer')
    elif computer == 'paper': gameResult('player')
else: print('Something went wrong')
