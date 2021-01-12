import pytest
from tests.user_acc_test.flo import diff
from game_of_greed.game import Game

pytestmark = [pytest.mark.version_2, pytest.mark.version_3]

def test_quitter():
    game = Game()
    errors = diff(game.play, path="tests/user_acc_test/sim_txt_files/quitter.sim.txt")
    assert not errors, errors[0]


def test_one_and_done():
    game = Game()
    errors = diff(game.play, path="tests/user_acc_test/sim_txt_files/one_and_done.sim.txt")
    assert not errors, errors[0]


# def test_single_bank():
#     game = Game()
#     errors = diff(game.play, path="tests/user_acc_test/bank_one_roll_then_quit.sim.txt")
#     assert not errors, errors[0]


# def test_bank_first_for_two_rounds():
#     game = Game()
#     errors = diff(game.play, path="tests/user_acc_test/bank_first_for_two_rounds.sim.txt")
#     assert not errors, errors[0]