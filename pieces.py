class Piece:
    def __init__(self, color):
        self.color = color

    def is_valid_move(self, board, start, end):
        """Should be implemented by subclasses to check if a move is valid."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}({self.color})"
    
    def convert_position(self, position):
        """Converts a chessboard position like 'a1' to row, col index."""
        column = position[0]
        row = position[1]
        row = 8 - int(row)  # Convert to zero-indexed row (8th row becomes 0)
        col = ord(column.lower()) - ord('a')  # Convert column letter to index (0 for 'a', 1 for 'b', etc.)
        return row, col

    def is_square_empty(self, board, row, col):
        """Helper method to check if a square is empty."""
        return board[row][col] is None or board[row][col].color != self.color

class Pawn(Piece):
    def is_valid_move(self, board, start, end):
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        # White pawn movement
        if self.color == 'White':
            # Single step forward (e.g., a2 to a3)
            if start_col == end_col and end_row == start_row - 1 and not board[end_row][end_col]:
                return True  # Move one square forward

            # First move, can move two squares forward (e.g., a2 to a4)
            if start_row == 6 and end_row == 4 and start_col == end_col and not board[end_row][end_col] and not board[start_row - 1][start_col]:
                return True  # Move two squares forward from the starting position

            # Capturing move (e.g., a2 to b3, where there's an opponent piece)
            if abs(start_col - end_col) == 1 and end_row == start_row - 1 and board[end_row][end_col]:
                return True  # Capture diagonally

        else:  # Black pawn movement
            # Single step forward (e.g., a7 to a6)
            if start_col == end_col and end_row == start_row + 1 and not board[end_row][end_col]:
                return True  # Move one square forward

            # First move, can move two squares forward (e.g., a7 to a5)
            if start_row == 1 and end_row == 3 and start_col == end_col and not board[end_row][end_col] and not board[start_row + 1][start_col]:
                return True  # Move two squares forward from the starting position

            # Capturing move (e.g., a7 to b6, where there's an opponent piece)
            if abs(start_col - end_col) == 1 and end_row == start_row + 1 and board[end_row][end_col]:
                return True  # Capture diagonally

        # If no valid move, return False
        return False



class Rook(Piece):
    def is_valid_move(self, board, start, end):
        """Checks if the Rook's move is valid."""
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        if start_row != end_row and start_col != end_col:
            return False  # Rook moves in straight lines only

        # Check if path is clear
        if start_row == end_row:  # Horizontal move
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if not self.is_square_empty(board, start_row, col):
                    return False
        elif start_col == end_col:  # Vertical move
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if not self.is_square_empty(board, row, start_col):
                    return False
        return True


class Knight(Piece):
    def is_valid_move(self, board, start, end):
        """Checks if the Knight's move is valid."""
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        if abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1:
            return True
        if abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2:
            return True
        return False


class Bishop(Piece):
    def is_valid_move(self, board, start, end):
        """Checks if the Bishop's move is valid."""
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        if abs(start_row - end_row) != abs(start_col - end_col):
            return False  # Bishop moves diagonally

        # Check if path is clear
        row_step = 1 if start_row < end_row else -1
        col_step = 1 if start_col < end_col else -1
        row, col = start_row + row_step, start_col + col_step
        while row != end_row and col != end_col:
            if not self.is_square_empty(board, row, col):
                return False
            row += row_step
            col += col_step
        return True


class Queen(Piece):
    def is_valid_move(self, board, start, end):
        """Checks if the Queen's move is valid."""
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        # Queen moves like both a rook and bishop
        if start_row == end_row or start_col == end_col:  # Rook-like move
            return Rook(self.color).is_valid_move(board, start, end)
        if abs(start_row - end_row) == abs(start_col - end_col):  # Bishop-like move
            return Bishop(self.color).is_valid_move(board, start, end)
        return False


class King(Piece):
    def is_valid_move(self, board, start, end):
        """Checks if the King's move is valid."""
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        if max(abs(start_row - end_row), abs(start_col - end_col)) == 1:
            return True
        return False

class SquareKnight(Piece):
    def is_valid_move(self, board, start, end):
        """Checks if the SquareKnight's move is valid."""
        start_row, start_col = self.convert_position(start)
        end_row, end_col = self.convert_position(end)

        # Check if move is exactly 2 squares in one direction and 2 squares in the other direction
        if (abs(start_row - end_row) == 2 and abs(start_col - end_col) == 2):
            return True
        return False
