import sys
sys.path.insert(0, "..")
import my_input
from utils import pr

i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_int_array_single(file_input)
pr(i_s, input)
        
        
def get_coords(x,y):
    return [i for i in [(x,y+1), (x+1,y), (x,y-1), (x-1,y)] if i[0] < (len(input)*5) and i[1] < (len(input[0])*5) and i[0]>=0 and i[1]>=0]

#costs = {(i,j):sys.maxsize for i in range(len(input)) for j in range(len(input))}

costs = {}

seen = {(0,0)}
unvisited = set()
costs[(0,0)] = 0
for i in get_coords(0,0):
            costs[i] = input[i[0]][i[1]]
            unvisited.add(i)

#print(costs)

sq_size = len(input)
def get_input(x,y):
    x_original = x % sq_size
    y_original = y % sq_size 
    x_repeat = int(x/sq_size)
    y_repeat = int(y/sq_size)

    res = (input[x_original][y_original] + x_repeat + y_repeat) % 9

    return res if res != 0 else 9

while len(unvisited):    
    current = sorted(unvisited, key=lambda x: costs.get(x,sys.maxsize))[0]
    seen.add(current)
    unvisited.remove(current)
    for i in get_coords(*current):
        #print(j,i)
        if i not in seen:
            unvisited.add(i)
        n = costs[current] + get_input(*i)
        if n<costs.get(i,sys.maxsize):
            costs[i] = n
#print(costs)
print(costs[((len(input)*5)-1,(len(input[0])*5)-1)])