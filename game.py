from chessboard import Chessboard
from pieces import Rook, Pawn, Phoenix

def play_game():
    # Custom starting positions for pieces (position -> piece)
    starting_positions = {
        'a1': [Rook('White')],  # White Rook at a1
        'h1': [Rook('White')],  # White Rook at h1
        'a2': [Pawn('White')],  # White Pawn at a2
        'b2': [Pawn('White')],  # White Pawn at b2
        'd4': [Phoenix('White')],  # Phoenix piece placed at d4 for White
    }

    chessboard = Chessboard(board_size=8, starting_positions=starting_positions)

    while True:
        # Print current board
        chessboard.print_board()

        # Input start and end positions for move
        start = input(f"{chessboard.turn} player's move (start position): ")
        end = input(f"{chessboard.turn} player's move (end position): ")

        # Try to move piece
        if not chessboard.move_piece(start, end):
            print("Invalid move! Try again.")
        else:
            chessboard.print_board()  # Print board after successful move

if __name__ == "__main__":
    play_game()
