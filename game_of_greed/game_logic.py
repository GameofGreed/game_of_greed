from collections import Counter
import random

class GameLogic:
    pass



    # def calculate_score 





    @staticmethod
    def roll_dice(die_num = 6) -> tuple:
        roll_result = tuple(())

        for die in range(1, die_num + 1):
            roll_result += (random.randint(1, 6),)
        return roll_result


class Banker:
    
    def __init__(self, round_points= 0) -> int:
        self.round_points = round_points


    # def shelf





    def bank(self, shelf_to_bank: int) -> int:
        self.round_points += shelf_to_bank

        if self.round_points >= 10000:
            print(f'Winner {self.round_points}')
            self.round_points = 0
        








    # def clear_shelf


    