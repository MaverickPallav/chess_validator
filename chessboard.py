from pieces import Pawn, Rook, Knight, Bishop, Queen, King, Dragon, Phoenix, SquareKnight

class Chessboard:
    def __init__(self, board_size=8, starting_positions=None):
        self.board_size = board_size
        self.board = self.initialize_board(starting_positions)
        self.turn = 'White'  # White starts the game

    def initialize_board(self, starting_positions):
        # Initialize board with pieces in the correct positions
        board = [['' for _ in range(self.board_size)] for _ in range(self.board_size)]

        # Use custom starting positions if provided, else use default 8x8 setup
        if starting_positions:
            for position, pieces in starting_positions.items():
                for piece in pieces:
                    row, col = self.convert_position(position)
                    board[row][col] = piece
        else:
            # Default 8x8 initial configuration
            # White pieces
            board[0][0] = Rook('White')
            board[0][1] = Knight('White')
            board[0][2] = Bishop('White')
            board[0][3] = Queen('White')
            board[0][4] = King('White')
            board[0][5] = Bishop('White')
            board[0][6] = SquareKnight('White')
            board[0][7] = Rook('White')
            for i in range(self.board_size):
                board[1][i] = Pawn('White')

            # Black pieces
            board[7][0] = Rook('Black')
            board[7][1] = Knight('Black')
            board[7][2] = Bishop('Black')
            board[7][3] = Queen('Black')
            board[7][4] = King('Black')
            board[7][5] = Bishop('Black')
            board[7][6] = SquareKnight('Black')
            board[7][7] = Rook('Black')
            for i in range(self.board_size):
                board[6][i] = Pawn('Black')

        return board

    def print_board(self):
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))

    def move_piece(self, start, end):
        # Convert the start and end positions to row and column indices
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        # Get the piece at the start position
        piece = self.board[start_row][start_col]

        # Check if there's no piece at the start position
        if not piece:
            print('Invalid Move: No piece at start position')
            return False

        # Check if it's the correct player's turn
        if piece.color != self.turn:
            print('Invalid Move: Not your turn')
            return False
        
        # Print the move attempt for debugging
        print(f"{self.turn} player is moving {piece.__class__.__name__}({piece.color}) from {start} to {end}")

        # Validate the piece's move
        if not piece.is_valid_move(self.board, start, end):
            print('Invalid Move: Piece cannot move that way')
            return False

        # Make the move: place the piece on the destination and clear the start position
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = None

        # Switch the turn to the other player
        self.turn = 'Black' if self.turn == 'White' else 'White'
        return True

    def convert_position(self, position):
        column = position[0]
        row = position[1]
        row = int(row) - 1  # Convert to zero-indexed row
        col = ord(column.lower()) - ord('a')  # Convert column letter to index
        return row, col
