import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

        
def get_mappings(s):
    #s ="acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
    ar = s.split()

    one = [i for i in ar if len(i) == 2][0]
    four = [i for i in ar if len(i) == 4][0]
    seven = [i for i in ar if len(i) == 3][0]
    eight = [i for i in ar if len(i) == 7][0]

    d1 = list(set(list(seven)) - set(list(one)))[0]
    d2_d4 = list(set(list(four)) - set(list(seven)))

    five_digit = [i for i in ar if len(i) == 5]
    six_digit = [i for i in ar if len(i) == 6]

    from collections import Counter
    cnt = Counter("".join(five_digit))

    d2_d5 = [i for i in cnt.keys() if cnt[i] == 1]

    d4 = (set(d2_d4) - set(d2_d5)).pop()
    d2 = (set(d2_d4) - set(d4)).pop()
    d5 = (set(d2_d5) - set(d2)).pop()

    d7 = ((set(list(eight)) - set(list(one))) - set([d1,d2,d4,d5])).pop()

    cnt2 = Counter("".join(six_digit))
    d3 = [i for i in cnt2.keys() if cnt2[i] == 2 and i != d4 and i != d5][0]
    d6 = (set(list(one)) - set(d3)).pop()
    two= [d1,d3,d4,d5,d7]
    three = [d1,d3,d4,d6,d7]
    five = [d1,d2,d4,d6,d7]
    six = [d1,d2,d4,d5,d6,d7]
    nine = [d1,d2,d3,d4,d6,d7]
    zero = [d1,d2,d3,d5,d6,d7]

    dct = {
    "".join(sorted(one)): '1',
    "".join(sorted(two)): '2',
    "".join(sorted(three)): '3',
    "".join(sorted(four)): '4',
    "".join(sorted(five)): '5',
    "".join(sorted(six)): '6',
    "".join(sorted(seven)): '7',
    "".join(sorted(eight)): '8',
    "".join(sorted(nine)): '9',
    "".join(sorted(zero)): '0'
    }
    return dct


input = my_input.readlines(file_input)

sum = 0
for line in input:
    ar = line.split("|")
    dct = get_mappings(ar[0].strip())
    sum +=int("".join([ dct["".join(sorted(i))] for i in ar[1].split()]))
print(sum)    