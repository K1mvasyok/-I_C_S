from lab3.reversi import ReversiGame
from lab3.miniMaxBot import MiniMaxBot

def play_game_with_bots():
    game = ReversiGame()
    bot1 = MiniMaxBot('X', depth=3)
    bot2 = MiniMaxBot('O', depth=3)

    current_player = 'X'

    while True:
        print(f"\nCurrent player: {current_player}")
        game.print_board()
        print("Number of X pieces:", game.count_pieces('X'))
        print("Number of O pieces:", game.count_pieces('O'))

        if current_player == 'X':
            move = bot1.get_move(game)
        else:
            move = bot2.get_move(game)

        if move:
            row, col = move
            game.make_move(row, col, current_player)
            print(f"{current_player} makes move: {move}")
        else:
            print(f"{current_player} has no valid moves and skips.")
        
        current_player = 'X' if current_player == 'O' else 'O'

        if not any(game.is_valid_move(row, col, 'X') for row in range(8) for col in range(8)) and \
           not any(game.is_valid_move(row, col, 'O') for row in range(8) for col in range(8)):
            break

    x_pieces = game.count_pieces('X')
    o_pieces = game.count_pieces('O')

    if x_pieces > o_pieces:
        winner = 'X'
    elif x_pieces < o_pieces:
        winner = 'O'
    else:
        winner = 'Draw'

    print("\nFinal board:")
    game.print_board()
    print(f"Game Over! Winner: {winner}")
    print(f"Final Scores - X: {x_pieces}, O: {o_pieces}")

if __name__ == "__main__":
    play_game_with_bots()
