import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)
pr(i_s, input)
        
        
rules = input[0]

data = input[2:]

print(data)

def inc_data(data1, inf_state):
    nl = [inf_state] * len(data1)
    for t in range(2):
        data1.insert(0, nl[:])
        data1.append(nl[:])
    for i  in data1:
        for t in range(2):
            i.insert(0, inf_state)
            i.append(inf_state)

def get_coords(x,y, data1, inf_state):
    return [data1[i[0]][i[1]] if i[0] < len(data1) and i[1] < len(data1[0]) and i[0]>=0 and i[1]>=0 else inf_state  for i in [(x-1, y-1), (x-1, y), (x-1, y+1), (x,y-1), (x,y), (x,y+1), (x+1, y-1), (x+1, y) , (x+1, y+1)]  ]

def print_array(data1):
    for i in data1:    
        print("".join(i))
    print()
print_array(data)

inf_state = "."
for i in range(2):        
    inc_data(data, inf_state)
    #print_array(data)    
    res = []
    for i in range(len(data)):
        tmp = []
        for j in range(len(data[0])):
            coords = "".join(get_coords(i,j, data, inf_state))
            num = int(coords.replace(".","0").replace("#","1"), 2)      
            # if num == 0:
            #     print(i,j)  
            tmp.append(rules[num])
        res.append(tmp)
    data = res
    inf_state = rules[-1] if inf_state =="#"  else rules[0]
    
    #print_array(data)    
    

print(sum([sum([ 1 for j in i if j == '#']) for i in data]))