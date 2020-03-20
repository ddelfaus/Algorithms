#!/usr/bin/python
# Write a function rock_paper_scissors to generate all of the possible plays that can be made in a game
#  of "Rock Paper Scissors", given some input n, which represents the number of plays per round.
# find repeated steps for recursion
# find base case
# (rock_paper_scissors(1), [['rock'], ['paper'], ['scissors']])
# (rock_paper_scissors(2), [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']])
# for n list out each of the choices
import sys


def rock_paper_scissors(n):
    plays = []

    # recursive part
    # for n in range(n,0,-1):
    #   plays.append('rock')
    #   plays.append('paper')
    #   plays.append('scissors')

    def recursive_rps(n,choice = []):
        
        # base case
        if n == 0:
            plays.append(choice)
        else:
            recursive_rps(n-1, choice + ['rock'])
          
            recursive_rps(n-1, choice + ['paper'])
            recursive_rps(n-1, choice + ['scissors'])

    recursive_rps(n)

    return plays


print(rock_paper_scissors(2))
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
