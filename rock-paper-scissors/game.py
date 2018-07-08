from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

def gameResult(winner):
    if winner == 'player': print('Player, you won this time')
    elif winner == 'computer': print('Computer got it right this time')
    elif winner == 'tie': print("It's a tie")

while player_wins < winning_score and computer_wins < winning_score:
    print("The available options are")
    print("...rock...")
    print("...paper...")
    print("...scissors...\n")

    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'

    player = input("Hey Player, make your choice: ").lower()
    print(f"\nYou played {player}")
    print(f"Computer plays {computer}\n")

    if player == computer: gameResult('tie')
    elif player == 'rock':
        if computer == 'scissors': gameResult('player'); player_wins += 1
        elif computer == 'paper': gameResult('computer'); computer_wins += 1
    elif player == 'paper':
        if computer == 'rock': gameResult('player'); player_wins += 1
        elif computer == 'scissors': gameResult('computer'); computer_wins += 1
    elif player == 'scissors':
        if computer == 'rock': gameResult('computer'); computer_wins += 1
        elif computer == 'paper': gameResult('player'); player_wins += 1
    else: print('Something went wrong, Please play again.'); break
    
    print(f"\nPlayer Score: {player_wins}")
    print(f"Computer Score: {computer_wins}\n")
else:
    if player_wins > computer_wins: print('Congratulations Player, You won the Game!')
    elif player_wins < computer_wins: print('Sorry! You Lost.')    
