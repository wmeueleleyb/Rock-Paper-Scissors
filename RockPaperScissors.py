import random, os, time

P_hand = {'rock':"---'   ____)     |       (_____)   |       (_____)   |       (____)    | ---.__(___)     |",
         'paper':"---'   ____)     |      _________) |       _________)|       ________) |---.__________)   ",
      'scissors':"---'   ____)     |      _________) |       _________)|      (____)     |---.__(___)       "}

CPU_hand = {'rock':"  (____   '---   |(_____)          |(_____)          | (____)          |  (___)__.---    ",
            'paper':"     (____   '---| (_________      |(_________       | (________       |  (__________.--- ",
         'scissors':"    (____   '--- | (_________      |(_________       |     (____)      |      (___)__.--- "}

move, c_move = 'rock', 'rock'
GameOver = False
line = ''

def show_hands():
    os.system('cls')
    print('==============================ROCK PAPER SCISSORS==============================')
    print('')
    print(line,end = '')
    print('               '+P_hand[move][0:17]+'                 '+CPU_hand[c_move][0:17])
    print('               '+P_hand[move][18:35]+'                 '+CPU_hand[c_move][18:35])
    print('               '+P_hand[move][36:53]+'                 '+CPU_hand[c_move][36:53])
    print('               '+P_hand[move][54:71]+'                 '+CPU_hand[c_move][54:71])
    print('               '+P_hand[move][72:-1]+'                 '+CPU_hand[c_move][72:-1])
    print('')

os.system('color c')
print('Rock, Paper, Scissors')
print("___________\nInstructions: Let's play a game of rock, paper, scissors.\nif you're not familiar, the rules are simple.")
print('ROCK beats SCISSORS | SCISSORS beats PAPER | PAPER beats ROCK.\n')
print('')
print('\nTo begin type START')
print('>',end = '')
name = input()

while GameOver == False:

    show_hands()
    
    print('Rock, Paper, or Scissors?')
    print('>',end = '')
    p_move = input().lower()
    if p_move != 'rock' and p_move != 'paper' and p_move != 'scissors':
        while p_move != 'rock' and p_move != 'paper' and p_move != 'scissors':
            print('That is not a move please try again')
            print('>',end = '')
            p_move = input().lower()

    for i in range(6):
        if i % 2 == 0:
            line = '\n'
            show_hands()
            time.sleep(0.2)
        else:
            line = ''
            show_hands()
            time.sleep(0.2)

    move = p_move
    c_move = random.choice(['rock','paper','scissors'])

    show_hands()

    if c_move == 'rock' and move == 'scissors': print('PC wins')
    elif c_move == 'rock' and move == 'paper': print('Player wins')
    elif c_move == 'paper' and move == 'rock': print('PC wins')
    elif c_move == 'paper' and move == 'scissors': print('Player wins')
    elif c_move == 'scissors' and move == 'rock': print('Player wins')
    elif c_move == 'scissors' and move == 'paper': print('PC wins')
    else: print('It\'s a draw')

    move, c_move = 'rock', 'rock'
    
    print('Would you like to play again? (y/n)')
    print('>',end = '')
    Continue = input().lower()
    if Continue == "y": GameOver = False
    else: GameOver = True
