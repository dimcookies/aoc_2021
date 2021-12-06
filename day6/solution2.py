import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int_array(file_input,sep=",")[0]


counts = dict()
for i in input:
  counts[i] = counts.get(i, 0) + 1

for i in range(9):
    counts.setdefault(i, 0)
print( [counts[k] for k in sorted(counts.keys())])   

for day in range(256):
    md = (day) % 9
    t = counts.get(md)        
    counts[md] = 0 
    counts[(day +9 )%9] += t
    counts[(day +7 )%9] += t
    
#    print( [counts[k] for k in sorted(counts.keys())], day, md)
           

print(sum(counts.values()))
       
        
        
        
