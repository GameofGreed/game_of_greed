import collections
import random

class GameLogic:

    @staticmethod
    def calculate_score(rolled_tuple) -> int:
        roll = collections.Counter(rolled_tuple)
        score = 0

        if len(roll.items()) == 3:
            pairs = 0
            for item in roll.items():
                if item[1] == 2:
                    pairs += 1
            if pairs == 3:
                score += 1500 
                return score       

        if len(roll.items()) == 6:
            score += 1500

        else:
            for die, count in roll.items():
                print('die', die) 
                print('count', count) 
                if die == 1:
                    if count > 2:
                        score += (die * 1000) * ( count - 2)
                    else:
                        score += die * 100 * count
                elif die == 5 and count < 3:
                    score += die * 10 * count
                elif(count > 2):
                    score += (die * 100) * (count -2 )
            

        # print(roll.items())
        print('score', score)
        return score 
    


    @staticmethod
    def roll_dice(die_num = 6) -> tuple:
        roll_result = tuple(())

        for die in range(1,die_num+1):
            roll_result = roll_result + (random.randint(1,6),)

        print(f'{roll_result}')
        return roll_result   

    @staticmethod
    def start_round():
        user_choice = input('press (r) to roll dice or (q) to quit')
        
        if user_choice == 'r':
            GameLogic.roll_dice()
            
            dice_shelf = input('enter dice to score')
            
            dice_shelf = list(dice_shelf)

            for item in range(len(dice_shelf)):
                dice_shelf[item] = int(dice_shelf[item])
                
            dice_shelf = tuple(dice_shelf)

            print('gamelogic score @fn: start_round', GameLogic.calculate_score(dice_shelf))

            user_choice = input('press (r) to roll again or (b) to bank points')
        
            if user_choice == 'r':
                GameLogic.roll_dice(6-len(dice_shelf))
                
                

        



class Banker:
    
    def __init__(self, balance= 0, shelved= 0) -> int:
        self.balance = balance
        self.shelved = shelved

    def shelf(self,calc_score) -> int:
        self.shelved += calc_score
        


    def bank(self) -> int:
        self.balance += self.shelved
        self.clear_shelf()

        if self.balance >= 10000:
            print(f'Winner {self.balance}')
            self.balance = 0
        

    def clear_shelf(self):
        self.shelved = 0 


if __name__ == "__main__":

    dice = GameLogic.roll_dice()

    # dice = GameLogic.roll_dice()
    # print(GameLogic.calculate_score((1,1,2,2,3,3)))

    GameLogic.start_round()
