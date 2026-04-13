#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'winner' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING erica
#  2. STRING bob
#

def winner(erica, bob):
    # start scores as zero
    e_score = 0
    b_score = 0
    
    # find # of games played
    games_played = len(erica)

    # set scores as a dict, makes adding or changing scores dynamic
    game_score = {'E':1, 'M':3, 'H':5} 

    # single loop to calculate individual scores
    for i in range(games_played):
        e_score += game_score[erica[i]]
        b_score += game_score[bob[i]]

    # trigger to see who won
    if e_score > b_score:
        return 'Erica'
    elif b_score > e_score:
        return 'Bob'
    else:
        return 'Tie'


if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # erica = input()
    erica = 'EMHH'
    bob = 'MMMH'

    # bob = input()

    result = winner(erica, bob)

    print(result)

    # fptr.write(result + '\n')

    # fptr.close()