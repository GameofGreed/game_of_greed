from game_of_greed.game_logic import GameLogic, Banker
roll_dice = GameLogic.roll_dice
from game_of_greed import __version__


def test_version():
    assert __version__ == '0.1.0'



# sequence of correct length is returned
def test_roll_dice_length():
    actual = len(roll_dice(4))
    expected = 4
    assert actual == expected
