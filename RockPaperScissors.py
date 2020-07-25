# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: SubjectCharlie
"""
#THIS IS A ROCK PAPER SCISSORS GAME

import random

print("It's time for a game of Rock, Paper, Scissors! Best 2 out of 3 wins, go!")
playerScore = 0
opponentScore = 0

while playerScore < 2 and opponentScore < 2:
    print('Enter R, P, or S.')
    playerChoice = input()
    choices = ['R', 'P', 'S']
    Opponent = choices[random.randint(0,2)]
    if playerChoice == 'R' or playerChoice == 'r':
        if Opponent == 'R':
            print('ROCK TIES WITH ROCK!')
        elif Opponent == 'P':
            print('ROCK LOSES TO PAPER!')
            opponentScore = opponentScore + 1
        elif Opponent == 'S':
            print('ROCK WINS AGAINST SCISSORS!')
            playerScore = playerScore + 1       
    elif playerChoice == 'P' or playerChoice == 'p':
        if Opponent == 'R':
            print('PAPER WINS AGAINST ROCK!')
            playerScore = playerScore + 1
        elif Opponent == 'P':
            print('PAPER TIES WITH PAPER!')
        elif Opponent == 'S':
            print('PAPER LOSES TO SCISSORS!')
            opponentScore = opponentScore + 1
    elif  playerChoice == 'S' or playerChoice == 's':
        if Opponent == 'R':
            print('SCISSORS LOSE TO ROCK!')
            opponentScore = opponentScore + 1
        elif Opponent == 'P':
            print('SCISSORS WIN AGAINST PAPER!')
            playerScore = playerScore + 1
        elif Opponent == 'S':
            print('SCISSORS TIE WITH SCISSORS!')
    else:
        print('Try entering that again.')


if playerScore == 2:
    print('Wow, you beat me!')
else:
    print('I won! Better luck next time.')
            
            
        
    
