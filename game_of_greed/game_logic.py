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
    shelved = 0
    balance = 0
    
    def shelf(self,calc_score):
        self.shelved += calc_score
        







    # def bank





    # def clear_shelf


    