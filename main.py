from lab3.reversi import ReversiGame
from lab3.miniMaxBot import MiniMaxBot

# def play_game_with_bots():
    # game = ReversiGame()
    # bot1 = MiniMaxBot('X', depth=3)
    # bot2 = MiniMaxBot('O', depth=3)

    # current_player = 'X'
    # passes = 0

    # while passes < 2:
    #     print(f"\nCurrent player: {current_player}")
    #     game.print_board()
    #     print("Number of X pieces:", game.count_pieces('X'))
    #     print("Number of O pieces:", game.count_pieces('O'))

    #     if current_player == 'X':
    #         move = bot1.get_move(game)
    #     else:
    #         move = bot2.get_move(game)

    #     if move:
    #         row, col = move
    #         game.make_move(row, col, current_player)
    #         print(f"{current_player} makes move: {move}")
    #         passes = 0
    #     else:
    #         print(f"{current_player} has no valid moves and skips.")
    #         passes += 1
        
    #     current_player = 'X' if current_player == 'O' else 'O'

    # x_pieces = game.count_pieces('X')
    # o_pieces = game.count_pieces('O')

    # if x_pieces > o_pieces:
    #     winner = 'X'
    # elif x_pieces < o_pieces:
    #     winner = 'O'
    # else:
    #     winner = 'Draw'

    # print("\nFinal board:")
    # game.print_board()
    # print(f"Game Over! Winner: {winner}")
    # print(f"Final Scores - X: {x_pieces}, O: {o_pieces}")

def play_game_with_bots():
    game = ReversiGame()
    bot1 = MiniMaxBot('X')
    bot2 = MiniMaxBot('O')

    while not game.is_game_over():
        game.display_board()
        if game.current_player == 'X':
            move = bot1.get_move(game)
        else:
            move = bot2.get_move(game)

        if move:
            game = game.simulate_move(move, game.current_player)
        else:
            print(f"No valid moves for {game.current_player}")

        game.current_player = 'O' if game.current_player == 'X' else 'X'

    print("Game Over!")
    game.display_board()

if __name__ == "__main__":
    play_game_with_bots()