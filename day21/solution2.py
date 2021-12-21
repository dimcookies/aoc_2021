import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False 
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)
                
pos = [int(input[0][-1]), int(input[1][-1])]
scores = [0,0]
dice = 1

turn = 0
while max(scores) < 1000:

    t_pos = pos[turn%2]
    t_score = scores[turn%2]

    n_pos = ((t_pos + sum(range(dice, dice+3))) % 10) 
    if n_pos == 0:
        n_pos = 10
    pos[turn%2] = n_pos
    scores[turn%2] +=n_pos
    print(turn+1, pos[turn%2], scores[turn%2])

    dice +=3
    turn +=1

print(turn*3 * min(scores))    