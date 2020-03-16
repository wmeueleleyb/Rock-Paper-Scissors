import random
import os

Moves = ['Rock','Paper','Scissors']
P_Moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
GameEnd = False

while GameEnd == False:
    
    os.system("cls")
    print("You are playing against the computer")
    print("Make your move")
    print("-------------------------------------")
    print("[A] Rock \n"
          "[B] Paper \n"
          "[C] Scissors")
    
    print("Your Move: ", end = '')
    move = str(input()).upper()
    comp_move = random.choice(Moves)

    print('------------------------------------------------')
    print('Player: ' + P_Moves[move] + '\nPC: ' + comp_move)
    print('------------------------------------------------')

    if comp_move == 'Rock' and move == 'C': print('PC wins')
    elif comp_move == 'Rock' and move == 'B': print('Player wins')
    elif comp_move == 'Paper' and move == 'A': print('PC wins')
    elif comp_move == 'Paper' and move == 'C': print('Player wins')
    elif comp_move == 'Scissors' and move == 'A': print('Player wins')
    elif comp_move == 'Scissors' and move == 'B': print('PC wins')
    else: print('It\'s a draw')
    
    print("Would you like to play again? (y/n): ",end = '')
    Continue = str(input())
    if Continue == "y": GameEnd = False
    else: GameEnd = True

