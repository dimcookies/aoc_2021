import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = list(map(lambda x: list(x),my_input.readlines(file_input)))
pr(i_s, input)
        
gamma=""        
epsilon = ""
for i in range(len(input[0])):
    digit_freq = [0,0]
    for j in range(len(input)):
        digit_freq[int(input[j][i])] +=1
    gamma = gamma + ("1" if digit_freq[1] > digit_freq[0] else "0")
    epsilon = epsilon + ("1" if digit_freq[1] < digit_freq[0] else "0")
print(int(gamma, 2) * int(epsilon, 2)) 
