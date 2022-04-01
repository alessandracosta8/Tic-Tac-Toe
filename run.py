class TicTacToe:
    """
    Class for the main game of Tic Tac Toe
    """
    def __init__(self):
        # single list that represents a 3x3 board, each number = cell
        self.board = [' ' for _ in range(9)]
        # keeps track of the winner if there is one
        self.current_winner = None
    
    def print_board(self):
        # which group of three spaces are we choosing row1 = 0,1,2 \ row2 = 3,4,5 \ row3 = 6,7,8 
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            # print a vertical line as a separator
            print("| " + " | ".join(row) + " |")

print(TicTacToe().print_board())