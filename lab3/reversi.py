class ReversiGame:
    def __init__(self):
        # Инициализация доски
        self.board = [['.'] * 8 for _ in range(8)]
        self.board[3][3], self.board[4][4] = 'X', 'X'
        self.board[3][4], self.board[4][3] = 'O', 'O'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_valid_move(self, row, col, player):
        # Проверка, можно ли сделать ход
        if self.board[row][col] != '.':
            return False
        opponent = 'X' if player == 'O' else 'O'
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            has_opponent = False
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                has_opponent = True
                r, c = r + dr, c + dc
            if has_opponent and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                return True
        return False

    def make_move(self, row, col, player):
        # Выполнение хода
        if not self.is_valid_move(row, col, player):
            return False
        self.board[row][col] = player
        opponent = 'X' if player == 'O' else 'O'
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                pieces_to_flip.append((r, c))
                r, c = r + dr, c + dc
            if pieces_to_flip and 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player:
                for flip_r, flip_c in pieces_to_flip:
                    self.board[flip_r][flip_c] = player
        return True

    def count_pieces(self, player):
        return sum(row.count(player) for row in self.board)
