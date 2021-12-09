import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)

pr(i_s, input)

def get_h(x,y):
    if x < 100 and y < 100 and x>=0 and y>=0:
        return int(input[x][y])
    return 99
res = []
for row in range(len(input)):
    #print(" ", row)
    for col in range(len(input[0])):
        #print("  ", col)
        v = int(input[row][col])
        if v < get_h(row, col-1) and v < get_h(row, col+1) and v < get_h(row-1, col) and v < get_h(row+1, col):
            #print(row,col)
            res.append(v+1)
print(res)                  

print(sum(res))

