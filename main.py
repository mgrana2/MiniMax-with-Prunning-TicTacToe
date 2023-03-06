from alphabeta import TicTacToe
from alphabeta import alpha_beta_value


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    # Implement me
    
    HUGE_NUMBER=1000000
    
    while not state.is_end_state():
        if state.is_max_node():
            # Player X's turn
            print("Player X's turn")
            children = state.generate_children()
            best_move = None
            best_value = -HUGE_NUMBER
            for child in children:
                child_value = alpha_beta_value(child)
                if child_value > best_value:
                    best_move = child
                    best_value = child_value
            state = best_move
        else:
            # Player O's turn
            print("Player O's turn")
            children = state.generate_children()
            best_move = None
            best_value = HUGE_NUMBER
            for child in children:
                child_value = alpha_beta_value(child)
                if child_value < best_value:
                    best_move = child
                    best_value = child_value
            state = best_move
        print(state)

    if state.won('x'):
        print('Player X wins!')
    elif state.won('o'):
        print('Player O wins!')
    else:
        print('Draw!')

def main():
    """
    You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    state = TicTacToe(empty_board, True)
    print(state)
    play(state)


if __name__ == '__main__':
    main()
