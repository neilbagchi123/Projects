"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    
    # X goes first, so if there are equal numbers of X and O, it's X's turn
    # Otherwise, it's O's turn
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    # Check each cell on the board
    for i in range(3):
        for j in range(3):
            # If the cell is empty, it's a valid move
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
                
    return possible_actions


def result(board, action):
    """
    Returns the board that would result from action being played on board.
    """
    # Validate the action
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Create a deep copy of the board to avoid modifying the original
    new_board = copy.deepcopy(board)
    
    # Determine whose turn it is
    current_player = player(board)
    
    # Make the move
    i, j = action
    new_board[i][j] = current_player
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == X:
            return X
        if board[0][j] == board[1][j] == board[2][j] == O:
            return O
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if there's a winner
    if winner(board) is not None:
        return True
    
    # Game is over if there are no empty spaces left
    for row in board:
        if EMPTY in row:
            return False
    
    # If we get here, all spaces are filled but there's no winner (tie)
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If the board is terminal, no move is possible
    if terminal(board):
        return None
    
    current_player = player(board)
    
    # Initialize best_move and best_value
    best_move = None
    
    if current_player == X:
        # X wants to maximize the utility
        best_value = float('-inf')
        
        # Try all possible actions and choose the one with the highest value
        for action in actions(board):
            # Calculate the min value for this action
            value = min_value(result(board, action))
            
            # Update best_value and best_move if a better move is found
            if value > best_value:
                best_value = value
                best_move = action
    else:
        # O wants to minimize the utility
        best_value = float('inf')
        
        # Try all possible actions and choose the one with the lowest value
        for action in actions(board):
            # Calculate the max value for this action
            value = max_value(result(board, action))
            
            # Update best_value and best_move if a better move is found
            if value < best_value:
                best_value = value
                best_move = action
                
    return best_move


def max_value(board):
    """
    Helper function for minimax to find the maximum utility value.
    """
    if terminal(board):
        return utility(board)
    
    value = float('-inf')
    
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    
    return value


def min_value(board):
    """
    Helper function for minimax to find the minimum utility value.
    """
    if terminal(board):
        return utility(board)
    
    value = float('inf')
    
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    
    return value