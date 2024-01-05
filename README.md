### Graph Representation
In this project, a tree diagram is used to represent the decision-making process in the Tic-Tac-Toe game. Each node in the tree corresponds to a specific state of the game board, and the edges represent the transition between these states based on player moves. The Minimax algorithm navigates through this tree to determine the best move at each step. The implementation of Alpha-Beta Pruning is highlighted in the tree to illustrate the reduction in the number of nodes evaluated, optimizing the decision-making process.

### Real-World Problem Definition
The project focuses on developing an AI for the game of Tic-Tac-Toe, serving as a microcosm for decision-making in constrained environments. The primary challenge addressed is creating an AI that can make optimal moves against a human opponent in this simplified model. The Tic-Tac-Toe scenario reflects broader applications in areas where efficient and strategic decision-making is essential, such as in automated planning, resource allocation, and other fields requiring complex decision-making under constraints.

### Project Overview
The project aims to create an intelligent Tic-Tac-Toe AI using the Minimax algorithm with Alpha-Beta Pruning. The key components include:
1. A 3x3 matrix representing the Tic-Tac-Toe board.
2. Functions to check win conditions and board status.
3. Implementation of the Minimax algorithm to evaluate moves.
4. Integration of Alpha-Beta Pruning to optimize the decision-making process.
5. A function to select the best move for the AI player.
6. A game loop to facilitate gameplay between the AI and a human player.

The objective is to demonstrate the application of these algorithms in a simple yet effective AI model, showcasing the principles of strategic decision-making and optimization in a controlled setting.

### Code Explanation
The Python code provided implements the Tic-Tac-Toe AI. Key functions include:
- `is_winner`: Checks if a player has won the game.
- `is_board_full`: Checks if the board is full.
- `minimax`: The core recursive function that simulates the game, alternating between players, and returning the best score from the current player's perspective.
- `find_best_move`: Uses the Minimax algorithm to find the best move for the AI.
- `print_board`: Displays the current state of the game board.

The Minimax function is enhanced with Alpha-Beta Pruning, which helps in skipping the evaluation of branches that don't promise a better outcome than already evaluated ones. This is evident in the conditional checks within the minimax function, where the loop breaks if `beta` is less than or equal to `alpha`. 

The example game loop demonstrates how these functions work together to enable gameplay, allowing interaction between the AI and a human player. This loop continues until a player wins or the board is full, ensuring that all possible game outcomes are accounted for.


<img width="779" alt="image" src="https://github.com/Hacktus/Tic-Tac-Toe/assets/126244304/0937af8e-0a8b-4ddf-82d6-408906470888">


<img width="205" alt="image" src="https://github.com/Hacktus/Tic-Tac-Toe/assets/126244304/a60dc202-83eb-40e3-ab28-733b87c129fb">

