import time

# --- Global Counters for Analysis ---
TOTAL_NODES_VISITED = 0
TOTAL_SOLUTIONS = 0

# ====================================================
# 1. Backtracking Algorithm (N-Queens Solver)
# ====================================================

def is_safe(board, row, col, N):
    """
    Checks if placing a queen at board[row][col] is safe.
    Only checks left (row), upper-left diagonal, and lower-left diagonal, 
    as we place queens column by column from left to right.
    """
    
    # Check this row on the left side
    for c in range(col):
        if board[row][c] == 1:
            return False
    
    # Check upper-left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
        
    # Check lower-left diagonal
    r, c = row, col
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
        
    return True

def solve_n_queens_backtracking(board, col, N):
    """
    Main recursive function implementing Backtracking.
    Finds all possible solutions.
    """
    global TOTAL_NODES_VISITED, TOTAL_SOLUTIONS
    TOTAL_NODES_VISITED += 1

    # Base Case: All queens are placed (Solution found)
    if col >= N:
        TOTAL_SOLUTIONS += 1
        # Optionally, print the board here if only a few solutions are expected
        # print_board(board, N)
        return 

    # Recursive Step: Try placing a queen in every row of the current column
    for row in range(N):
        # 1. Constraint Check (Pruning/Bounding)
        if is_safe(board, row, col, N):
            
            # 2. Place Queen (Select/Branch)
            board[row][col] = 1
            
            # 3. Recurse to the next column
            solve_n_queens_backtracking(board, col + 1, N)
            
            # 4. Backtrack (Unselect/Unwind)
            board[row][col] = 0


# ====================================================
# 2. Helper and Execution Functions
# ====================================================

def print_board(board, N):
    """Prints a single solution visually."""
    print("-" * (N * 2 + 1))
    for i in range(N):
        row_str = "|" + "|".join(" 👑" if board[i][j] == 1 else " -" for j in range(N)) + " |"
        print(row_str)
    print("-" * (N * 2 + 1))


def run_n_queens(N):
    """Sets up and runs the solver for a given N."""
    global TOTAL_NODES_VISITED, TOTAL_SOLUTIONS
    
    # Reset globals for the run
    TOTAL_NODES_VISITED = 0
    TOTAL_SOLUTIONS = 0
    
    # Initialize an N x N empty board (0s)
    board = [[0] * N for _ in range(N)]
    
    print(f"\n--- Solving N-Queens for N = {N} ---")
    
    start_time = time.time()
    
    # Start the backtracking search from the first column (col=0)
    solve_n_queens_backtracking(board, 0, N)
    
    end_time = time.time()
    
    # --- Analysis ---
    print(f"\n✅ Solution Complete (N={N})")
    print(f"Total Solutions Found: {TOTAL_SOLUTIONS}")
    print(f"Total Nodes Visited (Search Space Size): {TOTAL_NODES_VISITED}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")
    print("-" * 30)

# ====================================================
# 3. Execution and Engineering Analysis
# ====================================================

# Run for small N to see a quick result
run_n_queens(4)

# Run for a larger N to demonstrate search time and complexity
run_n_queens(8)

# Run for a challenging N to demonstrate the pruning's impact on time
run_n_queens(12)

# Note: The 'is_safe' check acts as the 'bounding' function in Branch and Bound, 
# pruning entire sub-trees (branches) of invalid moves early.
