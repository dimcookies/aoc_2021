import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import re
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)
pr(i_s, input)

regex = r"(on|off) x=(\-?\d+)\.\.(\-?\d+),y=(\-?\d+)\.\.(\-?\d+),z=(\-?\d+)\.\.(\-?\d+)"        

on_cubes = set()

def within_limits(v):
    return -50 <= v <=50
 
for line in input:        
    matches = re.finditer(regex, line, re.MULTILINE)

    limits = []
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            limits.append(match.group(groupNum))
    print(limits)
    if not [i for i in limits[1:] if within_limits(int(i))]:
        continue
    for x in range(int(limits[1]), int(limits[2])+1):
        for y in range(int(limits[3]), int(limits[4])+1):
            for z in range(int(limits[5]), int(limits[6])+1):
                coords = (x,y,z)
                if limits[0] == 'on':
                    on_cubes.add(coords)
                elif coords in on_cubes:
                    on_cubes.remove(coords)
print(len(on_cubes))