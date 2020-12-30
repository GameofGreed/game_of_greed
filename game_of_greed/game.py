from game_logic import GameLogic, Banker


class Game:
    """Class for game of Greed Application
    """

    def __init__(self,num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds
    
    def play(self, roller=None):
        """This will start of decline game

        Args:
            roller (function, optional): 
            Allows a custom dice roller function 
            Defaults to None.
        """

        self.round_num = 0

        self._roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input(">")

        if response == 'y' or response == 'yes':
            self.start_game()
        else:
            self.decline_game()


    def decline_game(self):
        print('OK, why start me then?')

    
    def start_game(self):
        pass

    game = Game()
    game.play()
    