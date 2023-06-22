from decouple import config

initial_capital = config('MY_MONEY', default=1000, cast=int)

from game import play_game

if __name__ == "__main__":
    play_game()


