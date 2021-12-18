import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
from collections import Counter
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)
        
template = input[0]
print(template)
rules = {i.split()[0]:i.split()[-1] for i in input[2:]}

for turn in range(40):
    tmp = ""
    for i in range(len(template)-1):    
        tmp +=template[i] + rules["".join(template[i:i+2])]
    tmp +=template[-1]

    print(len(tmp))
    template = tmp
vls = Counter(list(template)).values()
print("diff", max(vls) - min(vls))


