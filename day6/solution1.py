import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int_array(file_input,sep=",")[0]

for day in range(80):
    for i in range(len(input)):
        input[i] -=1
        if input[i] == -1:
            input.append(8)
            input[i] = 6
    print(len(input))            
        
        
        
