from game_of_greed.game_logic import GameLogic, Banker, Player # this will eventually be the correct path when flo.py is working

# from game_logic import GameLogic, Banker, Player   # for use with manual testing running the script. 

class Game:
    """Class for game of Greed Application
    """

    def __init__(self,num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds
        
    
    def play(self, roller=None):
        """This will start or decline game

        Args:
            roller (function, optional): 
            Allows a custom dice roller function 
            Defaults to None.
        """
        self.roller = roller 

        self.round_num = 0

        # self.roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == 'y' or response == 'yes':
            self.start_game()
        else:
            self.decline_game()


    def decline_game(self):
        print('OK. Maybe another time')

    
    def start_game(self):
        player = Player()
        player.start_round()

        #if calc_score is = 0  and  shelved is a truthy value
            #self.clear_shelf()

if __name__ == "__main__":
    game = Game()
    game.play()
    

    

        