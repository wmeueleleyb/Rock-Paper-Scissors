import random, os, time

P_hand = {'rock':"---'   ____)     |       (_____)   |       (_____)   |       (____)    | ---.__(___)      ",
         'paper':"---'   ____)     |      _________) |       _________)|       ________) |---.__________)   ",
      'scissors':"---'   ____)     |      _________) |       _________)|      (____)     |---.__(___)       "}
CPU_hand = {'rock':"  (____   '---   |(_____)          |(_____)          | (____)          |  (___)__.---    ",
           'paper':"     (____   '---| (_________      |(_________       | (________       |  (__________.--- ",
        'scissors':"    (____   '--- | (_________      |(_________       |     (____)      |      (___)__.--- "}

move, c_move = 'rock', 'rock'
p_score, c_score = 0,0
GameOver = False
line = ''

os.system('color c')
print('Rock, Paper, Scissors')
print("___________\nInstructions: Let's play a game of rock, paper, scissors.\nif you're not familiar, the rules are simple.")
print('ROCK beats SCISSORS | SCISSORS beats PAPER | PAPER beats ROCK.\nFirst one to reach a score of 3 wins.')
print('\nTo begin type your name')
print('>',end = '')
name = input()

def show_hands():
    global name, p_score, c_score
    os.system('cls')
    print('\n')
    print('               '+name+': '+str(p_score)+'                               cpu: '+str(c_score)+'\n\n')
    print(line,end = '')
    print('               '+P_hand[move][0:17]+'                 '+CPU_hand[c_move][0:17])   
    print('               '+P_hand[move][18:35]+'                 '+CPU_hand[c_move][18:35])
    print('               '+P_hand[move][36:53]+'                 '+CPU_hand[c_move][36:53])
    print('               '+P_hand[move][54:71]+'                 '+CPU_hand[c_move][54:71])
    print('               '+P_hand[move][72:-1]+'                 '+CPU_hand[c_move][72:-1]+'\n')

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
        move, c_move = 'rock','rock'
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

    if c_move == 'rock' and move == 'scissors': c_score += 1
    elif c_move == 'rock' and move == 'paper': p_score += 1
    elif c_move == 'paper' and move == 'rock': c_score += 1
    elif c_move == 'paper' and move == 'scissors': p_score += 1
    elif c_move == 'scissors' and move == 'rock': p_score += 1
    elif c_move == 'scissors' and move == 'paper': c_score += 1

    show_hands()
    
    if p_score == 3:
        print(name+' wins')
        print('\nwould you like to play again? (y/n)')
        print('>',end = '')
        Continue = input().lower()
        if Continue == 'y':
            move, c_move = 'rock','rock'
            p_score, c_score = 0,0
            GameOver = False
        else: GameOver = True
    elif c_score == 3:
        print('PC wins')
        print('\nwould you like to play again? (y/n)')
        print('>',end = '')
        Continue = input().lower()
        if Continue == 'y':
            move, c_move = 'rock','rock'
            p_score, c_score = 0,0
            GameOver = False
        else: GameOver = True
