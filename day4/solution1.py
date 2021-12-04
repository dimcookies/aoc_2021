import sys
sys.path.insert(0, "..")
import my_input
from utils import pr
i_s = False
i_puzzle = 1
file_input = "sample" + str(i_puzzle) if i_s else "input" + str(i_puzzle) 

input = my_input.readlines(file_input)

nums = [int(x) for x in input[0].strip().split(",")]
pr(i_s, nums)

line_num = 1

boards = []

while line_num < len(input):
    
    boards.append([[int(x) for x in i.strip().split()] for i in input[line_num+1:line_num+6]])
    line_num +=6

print(boards)

def sum_board(board):
    return sum([sum([x for x in i if x != -1]) for i in board])

def board_won(board):
    if -5 in [sum(i) for i in board]:
        return True
    for i in range(5):
        if sum([board[j][i] for j in range(5)]) == -5:
            return True
    return False

for num in nums:
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[i][j] == num:
                    board[i][j] = -1
        if board_won(board):
            sb = sum_board(board)
            print(sb, sb*num)
            quit()

