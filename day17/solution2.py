import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)[0]
pr(i_s, input)

import re

regex = r"target area: x=(\-?\d+)\.\.(\-?\d+), y=(\-?\d+)\.\.(\-?\d+)"

matches = re.finditer(regex, input, re.MULTILINE)

limits = []
for matchNum, match in enumerate(matches, start=1):    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1        
        limits.append(int(match.group(groupNum)))

print(limits)        


def simulate(vel):
    pos = [0,0]
    max_h = 0
    while pos[0] <= limits[1] and pos[1] > min(limits[2:]):
        pos[0] +=vel[0]
        pos[1] +=vel[1]

        vel[0] += -1 if vel[0] >0 else 0
        vel[1] -=1

        if pos[1] > max_h:
            max_h = pos[1]
        #print(pos, vel)
        if limits[0] <= pos[0] <= limits[1] and min(limits[2:]) <= pos[1] <= max(limits[2:]):
            return max_h
    return -1

max_heights =  []
for i in range(0,limits[1] + 10):
    for j in range(min(limits[2:]), 100):
        res = simulate([i,j]) 
        if res != -1:
            max_heights.append(res)

print(max(max_heights)) 
print(len(max_heights))           