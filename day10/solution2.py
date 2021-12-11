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
d_inv = {v: k for k, v in d.items()}
points =  {'}':3, ')' : 1, '>':4 , ']' : 2}

pts = []
for line in input:
    #print("checking",line)
    errors = ""
    st = []
    for char in line:
        if char in d.keys():
            try:
                p = st.pop()
                if p != d[char]:
                    errors +=char
                    break
            except:
                errors +=char
                break
        else:
            st.append(char)
    if len(errors) == 0:
        print(line)
        st.reverse()
        res = 0
        for i in st:
            res = res * 5 + points[d_inv[i]]
        pts.append(res)
pts = sorted(pts)
print(pts[int(len(pts)/2)])