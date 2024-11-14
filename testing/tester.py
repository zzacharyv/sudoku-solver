import sys
sys.path.insert(1,'/Users/zacha/OneDrive/Desktop/finished products/sudokuSolver-main/')
import constraintSatisfactionProblem as csp
import backtracking
import time
import ast
import validate
import random

def current_milli_time():
    return time.time() * 1000

def get_board(puzzle):
    b = [[7,5,9,4,6,2,8,1,3],
    [4,6,3,5,1,8,2,9,7],
    [1,2,8,9,7,3,6,4,5],
    [6,9,7,1,8,4,5,3,2],
    [5,8,4,2,3,6,9,7,1],
    [2,3,1,7,9,5,4,8,6],
    [3,4,5,8,2,1,7,6,9],
    [9,1,2,6,4,7,3,5,8],
    [8,7,6,3,5,9,1,2,4]]

    a = [[5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]]

    if puzzle == "a":
        return a
    return b 

def del_vals(board,percentage_out):
    for i in range(9):
        for j in range(9):
            if random.randint(0,100) < percentage_out:
                board[i][j] = 0
    return board

def generate_puzzles(filename,difficulty):
    original_stdout = sys.stdout
    with open(filename, 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        for i in range(1000):
            print(del_vals(get_board("a"),difficulty))
        sys.stdout = original_stdout # Reset the stan

def test_file(filename,algorithm):
    total_time = 0
    count_valid = 0
    count = 0

    f = open(filename, "r")

    for line in f.readlines():
        board = ast.literal_eval(line)
        start = current_milli_time()
        if algorithm == "backtracking":
            backtracking.solve(board,0,0)
        else:
            csp.solve(board)
        stop = current_milli_time()
        total_time += stop-start
        if validate.validate_sudoku(board):
            count_valid += 1
    f.close()
    return(total_time,count_valid)

def main():
    list = []
    # generate_puzzles("/Users/zacharyvannett/Desktop/AI/Sudoku/final/testing/boards/wicked_a.txt",70)
    print(test_file('/Users/zacha/OneDrive/Desktop/finished products/sudokuSolver-main/testing/boards/hard_a.txt',"csp"))
    print(test_file('/Users/zacha/OneDrive/Desktop/finished products/sudokuSolver-main/testing/boards/hard_b.txt',"csp"))




if __name__ == "__main__":
    main()



