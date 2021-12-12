import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = True
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_array(file_input, '-')
pr(i_s, input)
        
cnt = 0

from collections import Counter
def can_visit(k, visited):  
    if k =='start':
        return False     
    cnt = Counter([i for i in visited if i.islower()])
    #print(visited, cnt)
    return k not in visited or sum(set(cnt.values())) == 1

def is_available(fr, current, to):
    return current == fr and to != 'start'

def find_path(visited):
    global cnt
    current = visited[-1]
    available = [i[1] for i in input if is_available(i[0], current, i[1])] + [i[0] for i in input if is_available(i[1], current, i[0])]
    #print(visited, current, available)
    if current == 'end':
        cnt +=1
        #print(visited)
        return
    if len(available) == 0:
        return
    for i in [k for k in available if k.isupper() or (can_visit(k, visited))]:
            visited_c = visited[:] 
            visited_c.append(i)
            find_path(visited_c)            

visited = ['start']
find_path(visited)
print(cnt)