from game_of_greed.game_logic import GameLogic, Banker
roll_dice = GameLogic.roll_dice
from game_of_greed import __version__

import pytest


def test_version():
    assert __version__ == '0.1.0'



# sequence of correct length is returned
def test_roll_dice_length():
    actual = len(roll_dice(4))
    expected = 4
    assert actual == expected


def test_bank_instance():
    round_bank = Banker()
    assert round_bank.round_points == 0


# @pytest.mark.skip('pending code')
def test_bank_instance_add_from_shelf():
    round_bank = Banker(0)
    round_bank.bank(300)
    round_bank.bank(750)
    assert round_bank.round_points == 1050

# @pytest.mark.skip('pending code')
def test_bank_over_ten_thousand():
    round_bank = Banker (9000)
    round_bank.bank(2000)
    assert round_bank.round_points == 0
    