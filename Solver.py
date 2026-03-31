from constraint import Problem, AllDifferentConstraint
#print sudoku grid
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()
# solve sudoku using constraints
def solve_sudoku(puzzle):
    problem = Problem()
    cells = [(r, c) for r in range(9) for c in range(9)]
    for cell in cells:
        problem.addVariable(cell, range(1, 10))
    for r in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(r, c) for c in range(9)])
    for c in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(r, c) for r in range(9)])
    for br in range(3):
        for bc in range(3):
            box = [(r, c) for r in range(br*3, br*3+3)
                           for c in range(bc*3, bc*3+3)]
            problem.addConstraint(AllDifferentConstraint(), box)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                problem.addConstraint(
                    lambda var, val=puzzle[r][c]: var == val,
                    [(r, c)]
                )
    solution = problem.getSolution()
    if solution:
        return [[solution[(r, c)] for c in range(9)] for r in range(9)]
    return None
#check row validity
def check_row(row):
    nums = [x for x in row if x != 0]
    return len(nums) == len(set(nums))
#check full sudoku validity
def check_valid(puzzle):
    for row in puzzle:
        nums = [x for x in row if x != 0]
        if len(nums) != len(set(nums)):
            return False
    for col in range(9):
        nums = []
        for row in range(9):
            if puzzle[row][col] != 0:
                nums.append(puzzle[row][col])
        if len(nums) != len(set(nums)):
            return False
    return True
# take input from user 
def get_input():
    print("Enter Sudoku row by row (Use 0 for empty cells):")
    print("Please enter space between the numbers")
    puzzle = []
    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) != 9:
                print("Enter exactly 9 numbers")
                continue
            try:
                row = list(map(int, row))
            except:
                print("Enter only numbers")
                continue
            if any(num < 0 or num > 9 for num in row):
                print("Numbers must be between 0 and 9")
                continue
            #row validation
            if not check_row(row):
                print("\nInvalid row. Duplicate values found.\n")
                continue
            puzzle.append(row)
            print(f"\nRow {i+1} recorded: {row}")
            print("\nCurrent sudoku:")
            temp_board = puzzle + [[0]*9]*(8-i)
            print_board(temp_board)
            print()
            break
    return puzzle
# main program
puzzle = get_input()
print("\nFinal input sudoku:\n")
print_board(puzzle)
if not check_valid(puzzle):
    print("\nInvalid sudoku input.\n")
else:
    solution = solve_sudoku(puzzle)
    if solution:
        print("\nSolved sudoku:\n")
        print_board(solution)
    else:
        print("No solution found")
