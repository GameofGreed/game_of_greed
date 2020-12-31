from game_of_greed.game_logic import GameLogic, Banker
roll_dice = GameLogic.roll_dice
from game_of_greed import __version__

import pytest


# passes
def test_version():
    assert __version__ == '0.1.0'


### Testing - Roll Dice
# When rolling 1 to 6 dice ensure…

# 1) A sequence of correct length is returned

# passes: generates correct length
def test_roll_dice_length():
    actual = len(roll_dice(4))
    expected = 4
    assert actual == expected

    
# 2) Each item in sequence is an integer with value between 1 and 6
# passes: broken into separate verifications
def test_roll_dice_int():
    our_tuple = roll_dice(4)
    result = 'types'
    for item in range (0,4):
        result = f'{result} : {type(our_tuple[item])}'
    actual = result
    expected = "types : <class 'int'> : <class 'int'> : <class 'int'> : <class 'int'>" 
    assert actual == expected
    
def test_roll_dice_range():
    our_second_tuple = roll_dice(4)
    result = 'result:'
    for item in range (0,4):
        if 1 <= our_second_tuple[item] <= 6:
            result = f'{result} Ok'
            
    actual = result
    expected = "result: Ok Ok Ok Ok" 
    assert actual == expected

def test_bank_instance():
    round_bank = Banker()
    assert round_bank.balance == 0


# @pytest.mark.skip('pending code')
def test_bank_instance_add_from_shelf():
    round_bank = Banker(0)
    round_bank.shelf(300)
    round_bank.shelf(750)
    round_bank.bank()
    assert round_bank.balance == 1050

# @pytest.mark.skip('pending code')
def test_bank_over_ten_thousand():
    round_bank = Banker (9000)
    round_bank.shelf(2000)
    round_bank.bank()
    assert round_bank.balance == 0
    
def test_new_banker():
    banker = Banker()
    assert banker.balance == 0
    assert banker.shelved == 0

def test_shelf():
    banker = Banker()
    banker.shelf(100)
    assert banker.shelved == 100
    assert banker.balance == 0

def test_single_five():
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected

def test_two_fives():
    actual = GameLogic.calculate_score((5, 5))
    expected = 100
    assert actual == expected


def test_two_ones():
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected

def test_one_and_five():
    actual = GameLogic.calculate_score((1, 5))
    expected = 150
    assert actual == expected


def test_zilch():
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected


def test_three_fives():
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected

def test_three_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five():
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


def test_straight():
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    expected = 1500
    assert actual == expected

def test_three_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected


def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected

def test_five_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    expected = 600
    assert actual == expected


def test_six_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    expected = 800
    assert actual == expected


def test_six_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    expected = 4000
    assert actual == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 3000),
        ((1, 1, 1, 1, 1, 1), 4000),
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 600),
        ((2, 2, 2, 2, 2, 2), 800),
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 900),
        ((3, 3, 3, 3, 3, 3), 1200),
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1200),
        ((4, 4, 4, 4, 4, 4), 1600),
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 1500),
        ((5, 5, 5, 5, 5, 5), 2000),
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 1800),
        ((6, 6, 6, 6, 6, 6), 2400),
        ((1, 2, 3, 4, 5, 6), 1500),
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 1200),
    ],
)
def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected

def test_deposit():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    assert banker.shelved == 0
    assert banker.balance == 100


def test_clear_shelf():
    banker = Banker()
    banker.shelf(100)
    banker.bank()
    banker.shelf(50)
    banker.clear_shelf()
    assert banker.balance == 100
    assert banker.shelved == 0


