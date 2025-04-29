import random

print("--------Choose one of the five options: Rock, Paper, Scissors, Lizard, or Spock.--------\nThe winner is determined by the following rules: \nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors\nIf both players choose the same option, it’s a tie")

class Game():
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def rock(self, opponent_choice):
            if opponent_choice == 'Spock':
                return 'Rock has been vaporized. You lose.'
            elif opponent_choice == 'Paper':
                return 'Rock has been covered. You lose.'
            elif opponent_choice in ['Lizard', 'Scissors']: 
                return f'Rock has crushed {opponent_choice}. You win.'
            else:
                return 'Draw'
            
    def paper(self, opponent_choice):
            if opponent_choice == 'Scissors':
                return 'Paper has been cut. You lose.'
            elif opponent_choice == 'Lizard':
                return 'Paper has been eaten. You lose.'
            elif opponent_choice == 'Spock':
                return 'Paper has disproved Spock. You win.'
            elif opponent_choice == 'Rock':
                return 'Paper has covered Rock. You win.'
            else:
                return 'Draw'
            
    def scissors(self, opponent_choice):
            if opponent_choice == 'Rock':
                return 'Scissors have been crushed. You lose.'
            elif opponent_choice == 'Spock':
                return 'Scissors have been smashed. You lose.'
            elif opponent_choice == 'Paper':
                return 'Scissors have cut Paper. You win.'
            elif opponent_choice == 'Lizard':
                return 'Scissors have decapitated Lizard. You win.'
            else:
                return 'Draw'
            
    def spock(self, opponent_choice):
            if opponent_choice == 'Paper':
                return 'Spock has been disproven. You lose.'
            elif opponent_choice == 'Lizard':
                return 'Spock has been poisoned. You lose.'
            elif opponent_choice == 'Rock':
                return 'Spock has vaporized Rock. You win.'
            elif opponent_choice == 'Scissors':
                return 'Spock has smashed Scissors. You win.'
            else:
                return 'Draw'
            
    def lizard(self, opponent_choice):
            if opponent_choice == 'Rock':
                return 'Lizard has been crushed. You lose.'
            elif opponent_choice == 'Scissors':
                return 'Lizard has been decapitated. You lose.'
            elif opponent_choice == 'Paper':
                return 'Lizard has eaten Paper. You win.'
            elif opponent_choice == 'Spock':
                return 'Lizard has poisoned Spock. You win.'
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