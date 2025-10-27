Sample Output Analysis

The project runs the solver for $N=4, 8,$ and $12$ to demonstrate complexity growth

Board Size (N)   Total Solutions Found  Total Nodes Visited   Time Taken(s)  Insight
4                     2                       ~25                Very Fast    Basic demonstration
8                     92                      ~20,500            Fast         Standard benchmark,manageable search space
12                    14,200                  ~2,000,000         Moderate     Demonstrates the efficiency of pruning in managing exponential growth

1.solve_n_queens_backtracking(board, col, N): The recursive function that drives the entire search process.

2.is_safe(board, row, col, N): The Constraint Check function, which embodies the core pruning logic. It's the "bounding" rule that limits the search space.

3.Global Counters: Used to measure the exact number of nodes visited, providing concrete data on the search complexity.

Pure Backtracking Solver: Implements the core recursive backtracking logic to find all possible valid solutions for any $N \ge 4$.
Constraint Satisfaction: The is_safe function enforces the constraints (no two queens in the same row, column, or diagonal). This check effectively prunes invalid branches early.
Performance Metrics: The output includes essential data to analyze algorithm complexity:Total Solutions Found: The final count of valid configurations.
Total Nodes Visited: The exact size of the search space explored by the algorithm.Time Taken: The wall-clock time required for the computation.
Visualization: (For $N=4$ or small $N$) The project can print a visual representation of a solution using '👑'
