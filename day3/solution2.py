import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 2
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = list(map(lambda x: list(x),my_input.readlines(file_input)))
pr(i_s, input)

c_input = input[:]        
for i in range(len(c_input[0])):
    digit_freq = [0,0]
    for j in range(len(c_input)):
        digit_freq[int(c_input[j][i])] +=1
    freq = "1" if digit_freq[0] <= digit_freq[1] else "0"
    pr(i_s, freq)
    c_input = list(filter(lambda x: x[i] == freq, c_input))
    pr(i_s, c_input)
    if len(c_input) == 1:
        break
o2 = int("".join(c_input[0]),2)

c_input = input[:]
for i in range(len(c_input[0])):
    digit_freq = [0,0]
    for j in range(len(c_input)):
        digit_freq[int(c_input[j][i])] +=1
    freq = "0" if digit_freq[0] <= digit_freq[1] else "1"
    pr(i_s, freq)
    c_input = list(filter(lambda x: x[i] == freq, c_input))
    pr(i_s, c_input)
    if len(c_input) == 1:
        break
co2 = int("".join(c_input[0]),2)

print(o2 * co2)