import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)
pr(i_s, input)


def print_input(input):
    for i in input:
        print("".join(i))
    print()        

print_input(input)

turn = 0
while True:
    turn +=1
    cnt = 0
    tmp = [row[:] for row in input]       
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '>':
                new_pos = 0 if j+1 >= len(input[i]) else j+1
                if input[i][new_pos] == '.':
                    tmp[i][new_pos] = '>'
                    tmp[i][j] = '.'
                    cnt +=1
    input = [row[:] for row in tmp]              

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'v':
                new_pos = 0 if i+1 >= len(input) else i+1
                if input[new_pos][j] == '.':
                    tmp[new_pos][j] = 'v'
                    tmp[i][j] = '.'
                    cnt +=1                 
    input = [row[:] for row in tmp]    

    #print_input(input)
    if cnt == 0:
        break

print(turn)