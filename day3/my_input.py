import sys
import os

is_sample = True
file_input = "sample1" if is_sample else "input1"

def readlines(file_input):
    with open(os.path.join(sys.path[0], file_input), "r") as f:
        return list(map(lambda x: x.strip(),f.readlines()))                


def readlines_int(file_input):
    with open(os.path.join(sys.path[0], file_input), "r") as f:
        return list(map(lambda x: int(x.strip()),f.readlines()))                


def readlines_int_array(file_input):
    with open(os.path.join(sys.path[0], file_input), "r") as f:
        return list(map(lambda x: list(map(lambda y: int(y.strip()), x.strip().split())),f.readlines()))                
