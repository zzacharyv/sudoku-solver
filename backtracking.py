import constraintSatisfactionProblem as csp
import display
import time

def is_legal(board, row, col, num):
    if num in csp.get_constraints(board,row,col):
        return False
    return True

def solve(board, row, col):
        if csp.find_empty_cell(board) == None:
                return True
        if col == 9:
                row += 1
                col = 0
        if board[row][col] != 0:
                return solve(board, row, col + 1)
        for num in range(1, 10):
                if is_legal(board, row, col, num):
                        board[row][col] = num

                        if solve(board, row, col + 1):
                                return True
                board[row][col] = 0
        return False

def solve_and_display(board, screen, row, col):
        if csp.find_empty_cell(board) == None:
                return True
        if col == 9:
                row += 1
                col = 0
        if board[row][col] != 0:
                return solve_and_display(board, screen, row, col + 1)
        for num in range(1, 10):
                if is_legal(board, row, col, num):
                        board[row][col] = num
                        display.draw_board(screen, board, 504, 504)
                        time.sleep(0.3)
                        if solve_and_display(board, screen, row, col + 1):
                                return True
                board[row][col] = 0
        return False