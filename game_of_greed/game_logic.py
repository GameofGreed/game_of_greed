import collections
import random

class GameLogic:


    @staticmethod
    def calculate_score(rolled_tuple) -> int:
        roll = collections.Counter(rolled_tuple)
        score = 0

        print(roll.items())

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
        
        print(roll_result)
        return roll_result   


    
    @staticmethod
    def start_round(round = 1,die_num = 6):
        print(f'''
        Current Score is {currentBank.balance} 
        Current Shelf is {currentBank.shelved}
        ... Round {round}''')
        user_choice = input('press (r) to roll dice or (q) to quit')
        
        if user_choice == 'r':
            GameLogic.roll_dice(die_num)
            
            dice_shelf = input('enter dice to score')
            
            dice_shelf = list(dice_shelf)
            self_list = dice_shelf # saving list

            if currentBank.stored:
                   for item in range(len(currentBank.stored)):
                       dice_shelf.append(currentBank.stored[item])
                    
            for item in range(len(dice_shelf)):
                dice_shelf[item] = int(dice_shelf[item])
            
            dice_shelf = tuple(dice_shelf)
            score = GameLogic.calculate_score(dice_shelf)
            currentBank.shelf(score,self_list )

            print(f'''
            current shelved points {currentBank.shelved}
            current shelved dice {currentBank.stored}''')

            if score:
                user_choice = input('press (r) to roll again or (b) to bank points')
            
           
                if user_choice == 'b':
                    currentBank.bank()
                    GameLogic.start_round(round + 1)
                elif user_choice == 'r':
                    GameLogic.start_round(1,6-len(dice_shelf))
            else:
                print('FARKLLLLLLEEEEEEE')
                GameLogic.start_round(round+1)
                currentBank.clear_shelf()
                currentBank.clear_stored()
        else:
            print('okay thanks i guess') 
                
    

class Banker:
    
    def __init__(self, balance= 0, shelved= 0,stored = []) -> int:
        self.balance = balance
        self.shelved = shelved
        self.stored = stored

    # shelved = 0
    # balance = 0
    
    def shelf(self,calc_score,die_list) -> int:
        self.shelved += calc_score
        for item in range(len(die_list)):
                self.stored.append(die_list[item])       


    def bank(self) -> int:
        self.balance += self.shelved
        self.clear_shelf()

        if self.balance >= 10000:
            print(f'Winner {self.balance}')
            self.balance = 0 #maybe redundant
        

    def clear_shelf(self):
        self.shelved = 0
    
    def clear_stored(self):
        self.stored = []




# should remove any unbanked points, resetting to zero.
# should not affect previously banked points


if __name__ == "__main__":
#     dice = GameLogic.roll_dice()
#     print(GameLogic.calculate_score((2,2,1,1,3,3)))

    currentBank = Banker()
    GameLogic.start_round()