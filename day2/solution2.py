import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_array(file_input)
pr(i_s, input)
state = [0,0,0]
for i in input:
    pr(i_s, state)
    if i[0] == 'down':
        state[2]+=int(i[1])
    elif i[0] == 'up':
        state[2]-=int(i[1])
    else:
        state[0] = state[0]+ int(i[1])
        state[1] = state[1]+ int(i[1]) * state[2]

print(state, state[0] * state[1])        
        
