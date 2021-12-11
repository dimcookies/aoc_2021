import sys
from typing import DefaultDict
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)
        
d = {'}':'{', ')' : '(', '>':'<' , ']' : '['}
errors = ""  
for line in input:
    #print("checking",line)
    st = []
    res = ""
    for char in line:
        if char in d.keys():
            try:
                p = st.pop()
                if p != d[char]:
                    errors +=char
                    break
                res += char
            except:
                errors +=char
                #print(line)
                break
        else:
            st.append(char)
print(errors)
points =  {'}':1197, ')' : 3, '>':25137 , ']' : 57}

print(sum([points[i] for i in errors]))