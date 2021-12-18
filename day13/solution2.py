import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
        
coords = [[int(j) for j in i.split(",")] for i in input if i and i[0].isdigit()]
instructions = [i for i in input if i and i.startswith('fold')]

def print_a(ar):
    print()
    print()
    print()
    print("\n".join(["".join(['#' if j else '.' for j in i]) for i in ar]))
    print(sum([len([j for j in i if j]) for i in ar]))


def init_array(coords):
    mx = max([i[0] for i in coords])
    my = max([i[1] for i in coords])
    ar = [[False]*(mx+1) for i in range(my+1)] 
    for i in coords:        
        ar[i[1]][i[0]] = True
    return ar        

def merge_lines(ar1, ar2):
    for i in range(len(ar1)):
        ar2[i] = ar1[i] or ar2[i]

def fold_y(v, ar):
    for i in range(v+1, len(ar)):
        merge_lines(ar[i], ar[v-(i-v)])
    return ar[:v]
    
def fold_x(v, ar):
    res = []
    for line in ar:
        for i in range(v+1, len(ar[0])):
            line[v-(i-v)] = line[v-(i-v)] or line[i]
        line = line[:v]
        res.append(line)
    return res

input_ar = init_array(coords)
print_a(input_ar)
for i in instructions:
    ar = i.split()[-1].split('=')
    v = int(ar[1])
    if ar[0] == 'x':
        input_ar = fold_x(v, input_ar)
    else:
        input_ar = fold_y(v, input_ar)
print_a(input_ar)
    