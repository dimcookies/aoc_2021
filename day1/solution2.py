import my_input
from utils import pr
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int(file_input)
pr(i_s, input)
l = len(input)
input=input + input[:3]
print(len(list(filter(lambda x: sum(input[x:x+3]) < sum(input[x+1:x+4]) ,range(l)))))
        
