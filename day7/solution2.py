import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int_array(file_input, sep=",")[0]
pr(i_s, input)

dct = {}

def dst(a,b):    
    n = abs(a-b)
    return int((1 + n)*(n/2))

res = []        
for i in range(min(input), max(input)+1):
    res.append(sum([dst(i,j) for j in input]))
print(min(res))    