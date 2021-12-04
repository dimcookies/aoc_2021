import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int(file_input)
pr(i_s, input)
print(len(list(filter(lambda x: input[x] < input[x+1] ,range(len(input) - 1)))))
        
        
