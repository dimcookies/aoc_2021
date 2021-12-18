import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
from collections import Counter, defaultdict
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)
        
template = input[0]
print(template)
rules = {i.split()[0]:i.split()[-1] for i in input[2:]}

dct = defaultdict(int)
for i in range(len(template)-1):
    dct[template[i:i+2]] +=1
#print(dct)


for turn in range(40):
    nd = {}
    for i in dct:        
        n = rules[i]
        for j in (i[0]+ n, n+i[1]):
            nd[j] = nd.get(j,0) + dct[i]
    dct = nd
    #print(dct)         

res = {}
for i in dct:    
    for j in i:
        res[j] = res.get(j,0) + dct[i]
res[template[0]] +=1        
res[template[-1]] +=1

vls = res.values()
print("diff", int((max(vls) - min(vls))/2))


