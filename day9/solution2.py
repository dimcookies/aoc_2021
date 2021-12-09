import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import math
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)

pr(i_s, input)

def get_coords(x,y):
    return [i for i in [(x, y-1), (x,y+1), (x-1,y), (x+1,y)] if i[0] < len(input) and i[1] < len(input[0]) and i[0]>=0 and i[1]>=0 and int(input[i[0]][i[1]]) < 9]


def get_h(x,y):
    if x < len(input) and y < len(input[0]) and x>=0 and y>=0:
        return int(input[x][y])
    return 99

res = []
for row in range(len(input)):
    for col in range(len(input[0])):
        v = int(input[row][col])
        if v < get_h(row, col-1) and v < get_h(row, col+1) and v < get_h(row-1, col) and v < get_h(row+1, col):
            res.append((row,col))

sizes = []
for point in res:
        ar = []
        p = {point}
        while len(p):
            
            coords = p.pop()
            if coords not in ar:
                ar.append(coords)
                for i in get_coords(*coords):
                    p.add(i)
        sizes.append(len(ar))
print(sizes)
print(math.prod(sorted(sizes, reverse=True)[:3]))

