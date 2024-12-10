import numpy as np

class ReversiGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'X'

    def initialize_board(self):
        board = np.full((8, 8), '.')
        board[3][3], board[4][4] = 'X', 'X'
        board[3][4], board[4][3] = 'O', 'O'
        return board

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def count_pieces(self, player):
        return np.count_nonzero(self.board == player)

    def is_valid_move(self, row, col, player):
        if self.board[row][col] != '.':
            return False
        opponent = 'O' if player == 'X' else 'X'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                found_opponent = True
                r += dr
                c += dc
            if found_opponent and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                return True
        return False

    def make_move(self, row, col, player):
        if not self.is_valid_move(row, col, player):
            return False
        self.board[row][col] = player
        opponent = 'O' if player == 'X' else 'X'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                to_flip.append((r, c))
                r += dr
                c += dc
            if to_flip and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                for flip_r, flip_c in to_flip:
                    self.board[flip_r][flip_c] = player
        return True

    def has_valid_moves(self, player):
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col, player):
                    return True
        return False

    def print_board(self):
        for row in self.board:
            print(" ".join(row))