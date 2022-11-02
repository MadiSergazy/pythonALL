from settings import Settings
from checkerboard import Checkerboard
from collections import namedtuple
import game_functions as gf

def printed_board(checkerboard):
    """Print Checkerboard (black font with black background)"""
    # Set the font and background color format: \033[display mode; foreground color; background color m; and \033[0m behind is used to close the attribute, without adding will affect the back
    print('\033[1;41m--------------Simple Backgammon Game (Console Version)---------------\033[0m ')


print('\033[1;30;43m-------------------------------------------------------')
print('     1    2    3    4    5    6    7    8    9    10   ')
for i in range(len(checkerboard)):
    # ord returns the ASCII value of the character, and chr then returns the character; end=''sets no line break
    print(chr(ord('A') + i) + '    ', end='')
    for j in range(len(checkerboard[i])):
        print(checkerboard[i][j] + '    ', end='')
    print()
print('-------------------------------------------------------\033[0m')


def update_board(ck_settings, checkerboard, position):
    """Update Checkerboard Information"""


if ck_settings.chess_player == 1:
    print('Please chess player*Enter the chess piece coordinates (for example, A1, enter exit to exit the program):',
          end='')
check_input(ck_settings, checkerboard, '*', position)
else:
print('Please ask the player o to enter the chess piece coordinates (for example, C1, enter exit to exit the program):',
      end='')
check_input(ck_settings, checkerboard, 'o', position)


def check_input(ck_settings, checkerboard, char, position):
    """Check the input data, if correct, print the coordinates to the chessboard"""
    inputStr = input()  # Get input data


if len(inputStr) == 0:
    # Judging the empty situation
    print('\033[1;31m***Please enter coordinates (eg A1)!***\033[0m')
elif inputStr == 'exit':
    # exit the program
    exit()
elif not inputStr[1].isdigit():
    # The second digit is not a number
    print('\033[1;31m***The coordinates you entered are incorrect, please re-enter (eg A1)!***\033[0m')
else:
    # Get the board index
    ch = inputStr[0].upper()  # Get the first character and convert to uppercase
    i = ord(ch) - 65  # A's ASCII is 65
    j = int(inputStr[1:3]) - 1  # The maximum allowed is 10, so two bits must be obtained
    # Determine whether input overflow
if (i < 0 or i > 9 or j < 0 or j > 9):
    print('\033[1;31m***The coordinates you entered are incorrect, please re-enter (eg A1)!***\033[0m')
    # Determine whether the input has a chess piece
else:
    if checkerboard[i][j] == '-':
        # Cumulative steps (total of both sides)
        ck_settings.win_number += 1
        # If there is no child, the player symbol is replaced, and the player is converted
        checkerboard[i][j] = char
        ck_settings.chess_player *= -1
        # A total of 9 steps to start verifying wins and losses
        if ck_settings.win_number >= 9:
            check_stats(ck_settings, checkerboard, (i, j), char, position)
    else:
        print(
            '\033[1;31m*** There are already other pieces in the coordinates you entered, please re-enter (eg A1)!***\033[0m')


def check_stats(ck_settings, checkerboard, pos, char, position):
    """Check the four directions, whether there is a win or lose"""


pos_i, pos_j = pos
directs = [(1, 0), (0, 1), (1, 1),
           (1, -1)]  # Horizontal, vertical, oblique, and reverse oblique inspection in four directions
for direct in directs:
    line_checkerboard = []
    d_i, d_j = direct
    # Horizontal
    if d_j == 0:
        # Horizontally arranged into an array
        for j in range(ck_settings.number):
            # Only judge if it is "*" or "o"
            if checkerboard[pos_i][j] == char:
                line_checkerboard.append(position(pos_i, j))
        # print('Horizontal', line_checkerboard)
        win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)
    elif d_i == 0:
        # Vertically arranged into an array
        for i in range(ck_settings.number):
            # Only judge if it is "*" or "o"
            if checkerboard[i][pos_j] == char:
                line_checkerboard.append(position(i, pos_j))
        # print('Vertical', line_checkerboard)
        win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)
    elif d_i == 1 and d_j == 1:
        # Slash into an array
        # Left part
        minValue = min(pos_i, pos_j)  # Get smaller value
    for i in range(minValue):
        # Only judge if it is "*" or "o"
        if checkerboard[pos_i - minValue + i][pos_j - minValue + i] == char:
            line_checkerboard.append(position(pos_i - minValue + i, pos_j - minValue + i))

        # Right part
    maxValue = max(pos_i, pos_j)
    maxValue = ck_settings.number - maxValue  # Get the maximum value that can be superimposed
for i in range(maxValue):
    # Only judge if it is "*" or "o"
    if checkerboard[pos_i + i][pos_j + i] == char:
        line_checkerboard.append(position(pos_i + i, pos_j + i))
    # print('slash', line_checkerboard)
win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)
else:
# Backslash into an array
# Left part
minValue = min(ck_settings.number - pos_i, pos_j)  # Get smaller value
for i in range(minValue):
    # Only judge if it is "*" or "o"
    if checkerboard[pos_i + minValue - 1 - i][pos_j - minValue + i] == char:
        line_checkerboard.append(position(pos_i + minValue - 1 - i, pos_j - minValue + i))

    # Right part
maxValue = min(pos_i, ck_settings.number - pos_j)  # Get the maximum value that can be superimposed
for i in range(maxValue):
    # Only judge if it is "*" or "o"
    if checkerboard[pos_i - i][pos_j + i] == char:
        line_checkerboard.append(position(pos_i - i, pos_j + i))
# print('backslash', line_checkerboard)
win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char)


def win_condition(ck_settings, checkerboard, line_checkerboard, d_j, char):
    """ judge whether five consecutive """


if len(line_checkerboard) >= 5:
    for i, item in enumerate(line_checkerboard):
        index = i + 4
        if index < len(line_checkerboard):
            # Horizontal situation
            if d_j == 0:
                j1 = item.y
                j2 = line_checkerboard[index].y
                if (j2 - j1) == 4:
                    printed_board(checkerboard)
                    print('\033[1;32m' + char + 'The player wins!\033[0m')
                ck_settings.game_active = False
                break
        # Vertical, oblique, and reverse
        else:
            i1 = item.x
            i2 = line_checkerboard[index].x
            # Take the absolute value because the backslash is negative
            if abs(i2 - i1) == 4:
                printed_board(checkerboard)
                print('\033[1;32m' + char + 'The player wins!\033[0m')
            ck_settings.game_active = False
            break