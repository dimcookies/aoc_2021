import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
import math
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines_str_array(file_input)
pr(i_s, input)
        

bin_input = "".join([bin(int(i, 16))[2:].zfill(4) for i in input[0]])
print(bin_input)

version_sum =0

def compute_vl(type, vls):
    if type == 0:
        return sum(vls)
    elif type == 1:
        return math.prod(vls)
    elif type == 2:
        return min(vls)
    elif type == 3:
        return max(vls)
    elif type == 5:
        return 1 if vls[0] > vls[1] else 0
    elif type == 6:
        return 1 if vls[0] < vls[1] else 0
    elif type == 7:
        return 1 if vls[0] == vls[1] else 0


def extract(bits, spaces):
    global version_sum
    (version, packet_type) = extract_version_type(bits)
    version_sum +=version
    print(spaces, "version:",version,"type:",packet_type)
    if packet_type == 4:
        (res, offset) = extract_type_4(bits[6:], spaces)
        print(spaces,res)
        return (offset+6,res)
    else:
        (offset, vls) = extract_other(bits[6:], spaces)
        res = compute_vl(packet_type, vls)
        return (offset+6,res)

def extract_version_type(bits):
    return (int(bits[:3],2), int(bits[3:6],2))

def extract_type_4(bits, spaces):    
    res = ""
    i = 0
    while True:
        sub = bits[i:i+5]
        res = res + bits[i+1:i+5]
        i +=5
        if sub[0] == '0':
            break        
    #i +=i%4    
    return (int(res,2), i)

def extract_other(bits, spaces):
    spaces = spaces + "\t"
    length_type = int(bits[0])
    if length_type == 1:
        packest_num = int(bits[1:12],2)
        print(spaces, "Subpackets of count", packest_num)
        offset = 0
        vls = []
        for i in range(packest_num):
            (t_offset, t_vl) =extract(bits[12+offset:], spaces)
            offset +=t_offset
            vls.append(t_vl)
        return (12+offset,vls)
    else:
        length = int(bits[1:16],2)
        print(spaces, "Subpackets of length", length)
        offset = 0
        vls = []
        while offset < length:
            #print(spaces, "offset", 16+offset, length)
            (t_offset,t_vl) =extract(bits[16+offset:], spaces)        
            offset += t_offset
            vls.append(t_vl)    
        return (16+offset,vls)



print(extract(bin_input,""))
print(version_sum)