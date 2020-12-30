from collections import Counter
import random

class GameLogic:
    pass



    # def calculate_score 





    @staticmethod
    def roll_dice(die_num = 6) -> tuple:
        # create tuple with random int 1-6
        # The length of tuple must match the argument given 
        
        roll_result = tuple(())
        # loop through rolling single die for die_num number of times
        # add to tuple and return 
        for die in range(1,die_num+1):
            roll_result = roll_result + (random.randint(1,6),)
        return roll_result   


class Banker:
    pass


    # def shelf





    # def bank





    # def clear_shelf


    