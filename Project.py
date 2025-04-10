class Game():
    def __init__(self):
        choice = ()

    def rock(self):
        for rock in Game:
            if input == 'Spock':
                return 'Rock has been vaporized. You lose.'
            elif input == 'Paper':
                return 'Rock has been covered. You lose.'
            elif input == 'Lizard' or 'Scissors':
                return 'Rock has crushed {choice}. You win.'
            else:
                return 'Draw'
            
    def paper(self):
        for paper in Game:
            if input == 'Scissors':
                return 'Paper has been cut. You lose.'
            elif input == 'Lizard':
                return 'Paper has been eaten. You lose.'
            elif input == 'Spock':
                return 'Paper has disproved Spock. You win.'
            elif input == 'Rock':
                return 'Paper has covered Rock. You win.'
            else:
                return 'Draw'
            
    def scissors(self):
        for scissors in Game:
            if input == 'Rock':
                return 'Scissors have been crushed. You lose.'
            elif input == 'Spock':
                return 'Scissors have been smashed. You lose.'
            elif input == 'Paper':
                return 'Scissors have cut Paper. You win.'
            elif input == 'Lizard':
                return 'Scissors have decapitated Lizard. You win.'
            else:
                return 'Draw'
            
    def spock(self):
        for spock in Game:
            if input == 'Paper':
                return 'Spock has been disproven. You lose.'
            elif input == 'Lizard':
                return 'Spock has been poisoned. You lose.'
            elif input == 'Rock':
                return 'Spock has vaporized Rock. You win.'
            elif input == 'Scissors':
                return 'Spock has smashed Scissors. You win.'
            else:
                return 'Draw'
            
    def lizard(self):
        for lizard in Game:
            if input == 'Rock':
                return 'Lizard has been crushed. You lose.'
            elif input == 'Scissors':
                return 'Lizard has been decapitated. You lose.'
            elif input == 'Paper':
                return 'Lizard has eaten paper. You win.'
            elif input == 'Spock':
                return 'Lizard has poisoned Spock. You win.'
            else:
                return 'Draw'
            
            
    def play_game(self):
        game = []
        choice = input()
        for moves in game:
            if choice == Rock:
                pass 


    def play_round(self):
        pass   



class Player():
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def get_choice(self):
        choice = input('Pick One: Rock, Paper, Scissors, Lizard, Spock')



class Computer():
    def __init__(self, choice):
        self.choice = choice

    def random_choice(self):
        pass


        

