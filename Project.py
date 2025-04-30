import random

print("--------Choose one of the five options: Rock, Paper, Scissors, Lizard, or Spock.--------\nThe winner is determined by the following rules: \nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors\nIf both players choose the same option, it’s a tie")

lose = 'You lose'
win = 'You win'
class Game():
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    def rock(self, opponent_choice):
            if opponent_choice == 'Spock':
                return f'Rock has been vaporized. {lose}.'
            elif opponent_choice == 'Paper':
                return f'Rock has been covered. {lose}.'
            elif opponent_choice in ['Lizard', 'Scissors']: 
                return f'Rock has crushed {opponent_choice}. {win}.'
            else:
                return 'Draw'
            
    def paper(self, opponent_choice):
            if opponent_choice == 'Scissors':
                return f'Paper has been cut. {lose}.'
            elif opponent_choice == 'Lizard':
                return f'Paper has been eaten. {lose}.'
            elif opponent_choice == 'Spock':
                return f'Paper has disproved Spock. {win}.'
            elif opponent_choice == 'Rock':
                return f'Paper has covered Rock. {win}.'
            else:
                return 'Draw'
            
    def scissors(self, opponent_choice):
            if opponent_choice == 'Rock':
                return f'Scissors have been crushed. {lose}.'
            elif opponent_choice == 'Spock':
                return f'Scissors have been smashed. {lose}.'
            elif opponent_choice == 'Paper':
                return f'Scissors have cut Paper. {win}.'
            elif opponent_choice == 'Lizard':
                return f'Scissors have decapitated Lizard. {win}.'
            else:
                return 'Draw'
            
    def spock(self, opponent_choice):
            if opponent_choice == 'Paper':
                return f'Spock has been disproven. {lose}.'
            elif opponent_choice == 'Lizard':
                return f'Spock has been poisoned. {lose}.'
            elif opponent_choice == 'Rock':
                return f'Spock has vaporized Rock. {win}.'
            elif opponent_choice == 'Scissors':
                return f'Spock has smashed Scissors. {win}.'
            else:
                return 'Draw'
            
    def lizard(self, opponent_choice):
            if opponent_choice == 'Rock':
                return f'Lizard has been crushed. {lose}.'
            elif opponent_choice == 'Scissors':
                return f'Lizard has been decapitated. {lose}.'
            elif opponent_choice == 'Paper':
                return f'Lizard has eaten Paper. {win}.'
            elif opponent_choice == 'Spock':
                return f'Lizard has poisoned Spock. {win}.'
            else:
                return 'Draw'
            
            
    def play_game(self):
        player = Player()
        computer = Computer()

        player_choice = player.get_choice()

        while player_choice not in self.choices:
            print("Invalid choice. Please try again.")
            player_choice = player.get_choice()

        
        computer_choice = computer.random_choice()

        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)

        if player_choice == 'Rock':
             result = self.rock(computer_choice)
        elif player_choice == 'Paper':
             result = self.paper(computer_choice)
        elif player_choice == 'Scissors':
             result = self.scissors(computer_choice)
        elif player_choice == 'Lizard':
             result = self.lizard(computer_choice)
        elif player_choice == 'Spock':
             result = self.spock(computer_choice)
        else:
            result = "Invalid choice."
        
        print(result)

    def play_round(self):
        self.play_game()

class Player():
    def __init__(self, name="You", choice=""):
        self.name = name
        self.choice = choice

    def get_choice(self):
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        choice = input('Pick One: Rock, Paper, Scissors, Lizard, Spock: ')
        choice = choice.capitalize()

        self.choice = choice
        return choice


class Computer():
    def __init__(self, choice=""):
        self.choice = choice

    def random_choice(self):
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.choice = random.choice(choices)
        return self.choice
    
if __name__ == "__main__":
    game = Game()
    game.play_round()