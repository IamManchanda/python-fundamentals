print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("Player 1, make your choice: ")
print('*** No Cheating Please! ***\n\n' * 20)
player2 = input("Player 2, make your choice: ")

if player1 == player2: print("It's a tie")
elif player1 == 'rock':
    if player2 == 'scissors': print('Player 1, you won')
    elif player2 == 'paper': print('Player 2, you won')
elif player1 == 'paper':
    if player2 == 'rock': print('Player 1, you won')
    elif player2 == 'scissors': print('Player 2, you won')
elif player1 == 'scissors':
    if player2 == 'rock': print('Player 2, you won')
    elif player2 == 'paper': print('Player 1, you won')
else: print('Something went wrong')
