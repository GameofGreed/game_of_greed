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

        print(f'{roll_result}')
        return roll_result   


class Banker:
    
    def __init__(self, balance= 0, shelved= 0) -> int:
        self.balance = balance
        self.shelved = shelved

    # shelved = 0
    # balance = 0
    
    def shelf(self,calc_score) -> int:
        self.shelved += calc_score
        


    def bank(self) -> int:
        self.balance += self.shelved
        self.clear_shelf()

        if self.balance >= 10000:
            print(f'Winner {self.balance}')
            self.balance = 0 #maybe redundant
        

    def clear_shelf(self):
        self.shelved = 0 


class Player(Banker):

    def __init__(self, round = 0, scored_dice = tuple()):
        self.round = round
        self.scored_dice = scored_dice
        self.wallet = Banker()

    def start_round(self):
        print(f'Starting round {self.round}')
        user_choice = input('press (r) to roll dice or (q) to quit')
        
        if user_choice == 'r':
            admit = GameLogic.roll_dice()
            
            if GameLogic.calculate_score(admit):
                dice_shelf = input('enter dice to score')
                self.scored_dice = str_tuple_int(dice_shelf)
                self.wallet.shelf(GameLogic.calculate_score(self.scored_dice))
                self.bank_or_roll()

            else:
                print("Sorry you Farkled on your first roll!")
                self.start_round += 1
                self.start_round()   

        elif user_choice == 'q':
            print(f'Thanks for playing. You earned {self.wallet.balance} points.')

    def bank_or_roll(self):
            user_choice = input('press (r) to roll again or (b) to bank points or (q) to quit.')
        
            if user_choice == 'r':
                sec_roll = GameLogic.roll_dice(6-len(self.scored_dice))

                if GameLogic.calculate_score(sec_roll):
                    dice_shelf = input('enter dice to score')
                    self.scored_dice = str_tuple_int(dice_shelf)
                    self.wallet.shelf(GameLogic.calculate_score(self.scored_dice))
                    self.bank_or_roll()

                else:
                    print("Sorry you Farkled out!")
                    self.round += 1
                    self.start_round()

            elif user_choice == 'b':
                self.wallet.bank()
                self.round += 1 
                self.start_round()

            elif user_choice == 'q':
                print(f'Thanks for playing. You earned {self.wallet.balance} points.')

def str_tuple_int(input_str):
    input_str = list(input_str)

    for item in range(len(input_str)):
        input_str[item] = int(input_str[item])
        
    return tuple(input_str)


if __name__ == "__main__":
    # dice = GameLogic.roll_dice()
    # print(GameLogic.calculate_score((1,1,2,2,3,3)))

    GameLogic.start_round()
