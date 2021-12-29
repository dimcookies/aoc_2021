import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_array(file_input)
pr(i_s, input)
        

def get_op(op, reg):
    try:
        return int(op)
    except:
        return reg[op]

for i in range(99999999999999,11111111111111,-1):
        print("try", i)
        alu_input = str(i)

        reg = {'w':0, 'x':0, 'y':0, 'z':0}

        for i in input:
            if i[0] == 'inp':
                reg[i[1]] = int(alu_input[0])
                alu_input = alu_input[1:]
            elif i[0] == 'add':    
                reg[i[1]] += get_op(i[2], reg)
            elif i[0] == 'mul':
                reg[i[1]] *= get_op(i[2], reg)
            elif i[0] == 'div':
                reg[i[1]] = int(reg[i[1]]/get_op(i[2], reg))
            elif i[0] == 'mod':
                reg[i[1]] = reg[i[1]] % get_op(i[2], reg)
            else:
                reg[i[1]] = 1 if reg[i[1]] == get_op(i[2], reg) else 0

        if reg['z'] == 0:
           print(i)
           break
