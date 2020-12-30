from game_of_greed.game_logic import GameLogic, Banker
roll_dice = GameLogic.roll_dice
from game_of_greed import __version__


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

