import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
coords = []
for i in input:
    tmp = [int(j) for j in i.replace(" -> ", ",").strip().split(",")]
    coords.append(((tmp[0], tmp[1]), (tmp[2], tmp[3])))
    
coords1 = [i for i in coords if i[0][0] == i[1][0]]
coords2 = [i for i in coords if i[0][1] == i[1][1]]
coords3 = [i for i in coords if i[0][1] != i[1][1] and i[0][0] != i[1][0]]


dct = {}
for i in coords1:
    min_y = min([i[0][1], i[1][1]])
    max_y = max([i[0][1], i[1][1]])
    for j in range(min_y, max_y+1):
        k = str(i[0][0]) + "_" + str(j)
        dct.setdefault(k, 0)
        dct[k] +=1

for i in coords2:
    min_x = min([i[0][0], i[1][0]])
    max_x = max([i[0][0], i[1][0]])
    for j in range(min_x, max_x+1):
        k = str(j) + "_" + str(i[0][1])
        dct.setdefault(k, 0)
        dct[k] +=1        

for i in coords3:
    x = i[0][0]
    end_x = i[1][0]
    step_x = 1 if end_x > x else -1
    y = i[0][1]
    end_y = i[1][1]
    step_y = 1 if end_y > y else -1

    for j in range(x, end_x+step_x, step_x):
        k = str(j) + "_" + str(y)
        dct.setdefault(k, 0)
        dct[k] +=1
        y +=step_y        

    if y-step_y != end_y:
        print(str(i) + " " + str(y) + "_" + str(step_y) + "_" + str(end_y))

print(len([i for i in dct.values() if i>1]))        