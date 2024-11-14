def is_row_valid(row_num,sudoku):
    return len(set(sudoku[row_num])) == 9

def is_col_valid(col_num,sudoku):
    col = [item[col_num] for item in sudoku]
    return len(set(col)) == 9

def is_cell_valid(cel_row, cel_col,sudoku):
    vals = sudoku[cel_row][cel_col: cel_col+3]
    vals.extend(sudoku[cel_row+1] [cel_col: cel_col+3])
    vals.extend(sudoku[cel_row+2] [cel_col: cel_col+3])
    return len(set(vals)) == 9

def validate_sudoku(sudoku):
    for i in range(0,9):
        if not is_row_valid(i,sudoku):
            return False
        if not is_col_valid(i,sudoku):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not is_cell_valid(i, j,sudoku):
                return False
    return True
