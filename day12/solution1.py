import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_array(file_input, '-')
pr(i_s, input)
        
cnt = 0        
def find_path(visited):
    global cnt
    current = visited[-1]
    available = [i[1] for i in input if i[0] == current] + [i[0] for i in input if i[1] == current]
#    print(visited, current, available)
    if current == 'end':
        cnt +=1
        #print(visited)
        return
    if len(available) == 0:
        return
    for i in [k for k in available if k.isupper() or (k not in visited)]:
            visited_c = visited[:] 
            visited_c.append(i)
            find_path(visited_c)            

visited = ['start']
find_path(visited)
print(cnt)