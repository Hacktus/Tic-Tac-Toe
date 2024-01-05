def is_winner(board, player):
    """
    Check if the specified player has won the game.
    
    Args:
    board: 2D list representing the game board.
    player: Character representing the current player ('X' or 'O').

    Returns:
    Boolean indicating whether the player has won.
    """
    # Check rows and columns for win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[row][i] == player for row in range(3)):
            return True

    # Check diagonals for win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """
    Check if the board is full (no empty spaces).

    Args:
    board: 2D list representing the game board.

    Returns:
    Boolean indicating whether the board is full.
    """
    return all(all(cell is not None for cell in row) for row in board)

def minimax(board, depth, is_maximizing, alpha, beta, player):
    """
    Minimax algorithm with Alpha-Beta pruning for optimizing moves.

    Args:
    board: 2D list representing the game board.
    depth: Integer representing the depth of recursion.
    is_maximizing: Boolean indicating if the current move is maximizing or minimizing.
    alpha: Alpha value for Alpha-Beta pruning.
    beta: Beta value for Alpha-Beta pruning.
    player: Character representing the current player ('X' or 'O').

    Returns:
    Integer representing the score of the board state.
    """
    if is_winner(board, 'X'):
        return 10 - depth
    if is_winner(board, 'O'):
        return -10 + depth
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'  # Try a move
                    score = minimax(board, depth + 1, False, alpha, beta, player)
                    board[i][j] = None  # Undo the move
                    best_score = max(best_score, score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'  # Try a move
                    score = minimax(board, depth + 1, True, alpha, beta, player)
                    board[i][j] = None  # Undo the move
                    best_score = min(best_score, score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board, player):
    """
    Find the best move for the current player.

    Args:
    board: 2D list representing the game board.
    player: Character representing the current player ('X' or 'O').

    Returns:
    Tuple representing the row and column of the best move.
    """
    best_score = float('-inf' if player == 'X' else 'inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = player
                score = minimax(board, 0, player == 'O', float('-inf'), float('inf'), player)
                board[i][j] = None
                if (player == 'X' and score > best_score) or (player == 'O' and score < best_score):
                    best_score = score
                    best_move = (i, j)

    return best_move

def print_board(board):
    """
    Print the current state of the board.

    Args:
    board: 2D list representing the game board.
    """
    for row in board:
        print(' '.join(['_' if cell is None else cell for cell in row]))

# Example Game Loop
board = [[None] * 3 for _ in range(3)]
current_player = 'X'
while not is_winner(board, 'X') and not is_winner(board, 'O') and not is_board_full(board):
    print_board(board)
    if current_player == 'X':  # AI player
        move = find_best_move(board, current_player)
        board[move[0]][move[1]] = current_player
    else:
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] is None:
                    board[row][col] = current_player
                    valid_move = True
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter numbers only.")
    current_player = 'O' if current_player == 'X' else 'X'

print_board(board)
if is_winner(board, 'X'):
    print("X wins!")
elif is_winner(board, 'O'):
    print("O wins!")
else:
    print("It's a draw!")
