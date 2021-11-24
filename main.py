import math
import random

def play():
    user = input("What's your choice ? 'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        # return "You and the computer have both chosen {}. It's a tie.".format(computer)
        return (0, user, computer)

    if is_win(user, computer):
        # return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)
        return (1, user, computer)

    # return "You have chosen {} and the computer has chosen {}. You lost :(".format(user, computer)
    return (-1, user, computer)

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    #bermain sampai menang
    player_wins = 0
    compter_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and compter_wins < wins_necessary:
        result, user, computer = play()

        if result == 0:
            print('Its a tie. You and the computer have both chosen {}. \n'.format(user))
        elif result == 1:
            player_wins += 1
            print('You chosen {} and the computer chose {}. You won! \n'.format(user, computer))
        else:
            compter_wins += 1
            print('You chose {} and the computer chose {}. You Lost :( \n'.format(user, computer))
        print('\n')
    
    if player_wins > compter_wins:
        print('You have won the best of {} games! what a champ :D'.format(n))
    else:
        print('unfortunately, the computer has won the best of {} games. Better Try again'. format(n))




if __name__ == '__main__':
    # print(play())
    play_best_of(3) #2
    # play_best_of(9) #5