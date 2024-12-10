import numpy as np
from lab3.reversi import ReversiGame

class MiniMaxBot:
    def __init__(self, player, depth=3):
        self.player = player
        self.opponent = 'X' if player == 'O' else 'O'
        self.depth = depth

    def evaluate_board(self, game):
        """
        Оценочная функция для доски.
        Возвращает разницу в количестве фишек между игроком и его оппонентом.
        """
        return game.count_pieces(self.player) - game.count_pieces(self.opponent)

    def minimax(self, game, depth, maximizing_player):
        """
        Алгоритм Minimax.
        :param game: Объект игры.
        :param depth: Текущая глубина поиска.
        :param maximizing_player: True, если бот максимизирует свои результаты, иначе False.
        :return: Оценка доски и лучший ход.
        """
        if depth == 0 or not any(game.is_valid_move(row, col, self.player) for row in range(8) for col in range(8)):
            return self.evaluate_board(game), None

        best_move = None
        if maximizing_player:
            max_eval = float('-inf')
            for row in range(8):
                for col in range(8):
                    if game.is_valid_move(row, col, self.player):
                        # Копируем игру для симуляции
                        simulated_game = self.simulate_move(game, row, col, self.player)
                        eval, _ = self.minimax(simulated_game, depth - 1, False)
                        if eval > max_eval:
                            max_eval = eval
                            best_move = (row, col)
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for row in range(8):
                for col in range(8):
                    if game.is_valid_move(row, col, self.opponent):
                        # Копируем игру для симуляции
                        simulated_game = self.simulate_move(game, row, col, self.opponent)
                        eval, _ = self.minimax(simulated_game, depth - 1, True)
                        if eval < min_eval:
                            min_eval = eval
                            best_move = (row, col)
            return min_eval, best_move

    def simulate_move(self, game, row, col, player):
        """
        Создаёт копию игры и выполняет ход.
        :param game: Объект игры.
        :param row: Строка хода.
        :param col: Колонка хода.
        :param player: Игрок, совершающий ход.
        :return: Новый объект игры с выполненным ходом.
        """
        new_game = ReversiGame()
        new_game.board = np.copy(game.board)
        new_game.make_move(row, col, player)
        return new_game

    def get_move(self, game):
        """
        Возвращает лучший ход, используя алгоритм Minimax.
        :param game: Объект игры.
        :return: Кортеж (row, col) — координаты хода.
        """
        _, best_move = self.minimax(game, self.depth, True)
        return best_move