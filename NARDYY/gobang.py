from settings import Settings
from checkerboard import Checkerboard
from collections import namedtuple
import game_functions as gf


def run_game():
    """run game"""
    # Configure instantiation
    ck_settings = Settings()
    # Instantiate the chessboard and call the drawing method
    ck = Checkerboard(ck_settings)
    checkerboard = ck.draw()
    # namedtupleCreate a data type similar to tuples, in addition to being accessible by index, iterating, and accessing data by attribute name
    position = namedtuple('Position', ['x', 'y'])

    while ck_settings.game_active:
        # Print board
        gf.printed_board(checkerboard)
        # Update board
        gf.update_board(ck_settings, checkerboard, position)


run_game()