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
    return [i for i in [(x, y-1), (x,y+1), (x-1,y), (x+1,y), (x-1, y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1)] if i[0] < len(input) and i[1] < len(input[0]) and i[0]>=0 and i[1]>=0 and input[i[0]][i[1]] <= 9]

def find_flashing():
    return [(row,col) for row in range(len(input)) for col in range(len(input[0])) if input[row][col] > 9]

flashes = 0
turn =0
while True:
    for row in range(len(input)):
        for col in range(len(input[0])):            
                input[row][col] +=1
    flashing = find_flashing()
    flashed = []
    while True:
        tmp = [i for i in flashing if i not in flashed] 
        if not tmp:
            break
        for f in tmp:
            for k in get_coords(*f):
                input[k[0]][k[1]] +=1
            flashed.append(f)
        flashing = find_flashing()
    for i in flashed:
        input[i[0]][i[1]] = 0
    # print(turn)        
    # for i in input:
    #     print("".join([str(j) for j in i]))
    # print()
    turn +=1
    if len(flashed) == 100:
        print(turn)
        break
