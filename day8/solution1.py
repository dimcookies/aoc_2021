import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)

input = [i.split('|')[1].split() for i in input]
pr(i_s, input)

part1_valid = [2,3,4,7]

cnt = 0
for i in input:
    for j in i:
        if len(j) in part1_valid:
            cnt +=1
print(cnt)            

