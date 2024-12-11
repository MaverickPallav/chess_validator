import unittest
from pieces import Pawn, Rook, Knight, Queen, King, SquareKnight

class TestChessValidator(unittest.TestCase):

    def test_valid_pawn_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[6][0] = Pawn('White')  # Place a White pawn at a2 (row 6, col 0 in 0-indexed)
        
        # Test a valid move for a White Pawn (a2 to a3)
        result = chessboard[6][0].is_valid_move(chessboard, "a2", "a3")
        self.assertTrue(result)

    def test_invalid_pawn_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[6][0] = Pawn('White')  # Place a White pawn at a2 (row 6, col 0 in 0-indexed)
        
        # Test an invalid move for a White Pawn (a2 to a5, which is not allowed for a Pawn)
        result = chessboard[6][0].is_valid_move(chessboard, "a2", "a5")
        self.assertFalse(result)

    def test_valid_rook_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][0] = Rook('White')  # Place a White rook at a1
        
        # Test a valid move for a White Rook (a1 to a4)
        result = chessboard[0][0].is_valid_move(chessboard, "a1", "a4")
        self.assertTrue(result)

    def test_invalid_rook_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][0] = Rook('White')  # Place a White rook at a1
        
        # Test an invalid move for a White Rook (a1 to b2)
        result = chessboard[0][0].is_valid_move(chessboard, "a1", "b2")
        self.assertFalse(result)

    def test_valid_knight_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][0] = Knight('White')  # Place a White knight at a1
        
        # Test a valid move for a White Knight (a1 to b3)
        result = chessboard[0][0].is_valid_move(chessboard, "a1", "b3")
        self.assertTrue(result)

    def test_invalid_knight_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][0] = Knight('White')  # Place a White knight at a1
        
        # Test an invalid move for a White Knight (a1 to a3)
        result = chessboard[0][0].is_valid_move(chessboard, "a1", "a3")
        self.assertFalse(result)

    def test_valid_square_knight_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][0] = SquareKnight('White')  # Place a White SquareKnight at a1
        
        # Test a valid move for a White SquareKnight (a1 to c3)
        result = chessboard[0][0].is_valid_move(chessboard, "a1", "c3")
        self.assertTrue(result)

    def test_invalid_square_knight_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][0] = SquareKnight('White')  # Place a White SquareKnight at a1
        
        # Test an invalid move for a White SquareKnight (a1 to a3)
        result = chessboard[0][0].is_valid_move(chessboard, "a1", "a3")
        self.assertFalse(result)

    def test_valid_queen_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][3] = Queen('White')  # Place a White Queen at d1
        
        # Test a valid move for a White Queen (d1 to d5)
        result = chessboard[0][3].is_valid_move(chessboard, "d1", "d5")
        self.assertTrue(result)

    def test_invalid_queen_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[0][3] = Queen('White')  # Place a White Queen at d1
        
        # Test an invalid move for a White Queen (d1 to e3)
        result = chessboard[0][3].is_valid_move(chessboard, "d1", "e3")
        self.assertFalse(result)
    
    def test_king_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[4][4] = King('White')  # Place a White king at e5 (row 4, col 4 in 0-indexed)
        
        # Test a valid move for the White King (e5 to e6)
        result = chessboard[4][4].is_valid_move(chessboard, "e5", "e6")
        self.assertTrue(result)
    
    def test_invalid_king_move(self):
        chessboard = [[None] * 8 for _ in range(8)]  # Empty 8x8 chessboard
        chessboard[4][4] = King('White')  # Place a White king at e5 (row 4, col 4 in 0-indexed)

        # Test an invalid move for the White King (e5 to e7)
        result = chessboard[4][4].is_valid_move(chessboard, "e5", "e7")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
