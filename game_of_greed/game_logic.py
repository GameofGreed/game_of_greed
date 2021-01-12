import collections
import random

class GameLogic:

    @staticmethod
    def calculate_score(rolled_tuple) -> int:
        roll = collections.Counter(rolled_tuple)
        score = 0

        if len(roll.items()) == 6:
            score += 1500
        else:
            for die, count in roll.items():
                if die == 1:
                    if count > 2:
                        score += (die * 1000) * ( count - 2)
                    else:
                        score += die * 100 * count
                elif die == 5 and count < 3:
                    score += die * 10 * count
                elif(count > 2):
                    score += (die * 100) * (count -2 )
            

        return score
    


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
    
    def __init__(self, round_points= 0) -> int:
        self.round_points = round_points



    def bank(self, shelf_to_bank: int) -> int:
        self.round_points += shelf_to_bank

        if self.round_points >= 10000:
            print(f'Winner {self.round_points}')
            self.round_points = 0
        
    shelved = 0
    balance = 0
    
    def shelf(self,calc_score) -> int:
        self.shelved += calc_score
        



    #def clear_shelf


if __name__ == "__main__":
    dice = GameLogic.roll_dice()
