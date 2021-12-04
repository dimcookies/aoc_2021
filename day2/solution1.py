import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_array(file_input)
pr(i_s, input)
#print(len(list(filter(lambda x: input[x] < input[x+1] ,range(len(input) - 1)))))

x = sum([int(x[1]) for x in input if x[0] == 'forward'])
y = sum([int(x[1]) if x[0] == 'down' else (-1 * int(x[1])) for x in input if x[0] != 'forward'])
print(x*y)

        
