# Sudoku_Solver
# AI-Based Sudoku Solver

## Overview of the Project

This project is a console-based Sudoku Solver developed using Python. It uses a constraint satisfaction approach to solve Sudoku puzzles efficiently. The system takes user input for a Sudoku grid and validates the input before solving it.

The solver ensures that all Sudoku rules are followed and then generates a valid completed Sudoku grid.


## Features

1. User Input: Allows users to enter Sudoku row by row.
2. Input Validation: Checks for invalid values and duplicate entries.
3. Error Handling: Detects incorrect inputs and prevents invalid puzzles.
4. AI Solver: Uses constraint satisfaction to solve the puzzle.
5. Clean Output: Displays both input and solved Sudoku clearly.


## Technologies Used / Tools

1. Language: Python 3  
2. Interface: Command Line Interface (CLI)  
3. Library: python-constraint  


## Steps to Install & Run the Project

1. Prerequisite: Make sure Python is installed on your system.
2. Install required library:
   pip install python-constraint
3. Download or clone the project.
4. Navigate to the project folder:
   cd Program
5. Run the program:
   python program.py


## Instructions for Testing

1. Run the program.
2. Enter Sudoku values row by row.
3. Use 0 for empty cells.
4. Ensure no duplicate values in a row.
5. After entering all rows, the program will:
   - Validate the input
   - Solve the Sudoku
   - Display the result
  
  
## Screenshots

1) Input start:
   
   <img width="1164" height="106" alt="image" src="https://github.com/user-attachments/assets/69df20c5-6667-4750-af06-2d380e23ea07" />

2) Invalid row:
   
   <img width="352" height="79" alt="image" src="https://github.com/user-attachments/assets/de23822d-4293-47b0-a109-0c324e66bf68" />

3) Current sudoku:
   
   <img width="229" height="280" alt="image" src="https://github.com/user-attachments/assets/3e1a1a37-cdeb-43b3-92e4-2a8e7e912ad9" />

4) Final output:
   
   <img width="219" height="307" alt="image" src="https://github.com/user-attachments/assets/6e100bbc-5ca0-46a4-a6fa-6b3ea2f13a18" />

5) Solved sudoku:
    
   <img width="211" height="294" alt="image" src="https://github.com/user-attachments/assets/f1bb3bcc-c4f0-431a-92eb-d33489b48636" />
