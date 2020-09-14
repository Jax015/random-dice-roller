from random import randint

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    round = 1

    while round != 11:
        print ("Round " + str(round))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll: " + str(player1))
        print("Player 2 Roll: " + str(player2))

        if player1 == player2:
            print("Draw!\n")
        elif player1 > player2:
            print("PLayer 1 Wins!\n")
        else:
            print("Player 2 Wins!\n")

        round = round + 1



    if player1wins == player2wins:
        print("Draw!")
    elif player1wins > player2wins:
        print("Player 1 Wins! Rounds Won: " + str(player1wins))
    else:
        print("Player 2 Wins! Rounds Won: " + str(player2wins))

def dice_roll():
    diceRoll = randint(1,6)
    return diceRoll

main()
input()
