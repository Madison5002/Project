import random

instructions = r'''
────────────────────────────────────────────────────────────
HOW TO PLAY:

You will choose from the following five options:
🪨  Rock
📄  Paper
✂️  Scissors
🦎  Lizard
🖖  Spock

The rules are:
- Scissors ✂️ cuts Paper 📄
- Paper 📄 covers Rock 🪨
- Rock 🪨 crushes Lizard 🦎
- Lizard 🦎 poisons Spock 🖖
- Spock 🖖 smashes Scissors ✂️
- Scissors ✂️ decapitates Lizard 🦎
- Lizard 🦎 eats Paper 📄
- Paper 📄 disproves Spock 🖖
- Spock 🖖 vaporizes Rock 🪨
- Rock 🪨 crushes Scissors ✂️

First to win 2 out of 3 rounds is the champion! 🏆
────────────────────────────────────────────────────────────
'''

rock_ascii = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_ascii = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors_ascii = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lizard_ascii = '''
⠀⠀⣀⣀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣞⠁⠨⠭⠱⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠫⡒⠀⠀⡄⣽⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣄⣠⢿⣿⢱⡿⠋⣷⣦⣜⠱⡀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⡯⣄⡁⠈⠁⢸⣟⣁⢈⣷⣜⣷⣋⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠃⢈⡿⠦⣄⣀⡇⢀⡉⠋⠀⠙⢧⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣤⢄⣸⢸⠀⠀⠀⠈⡇⢨⠷⠤⠤⠥⠸⣁⡀⠹⢩⠒⠒⢲⢄⠀⠀
⠀⣺⡿⠧⠤⠊⣀⣶⣶⣶⡁⣸⠀⠀⠀⠀⠀⠀⠀⠉⠁⠒⠠⢄⡐⠓⡄
⠀⠁⠀⠀⠀⠈⢡⡴⠛⡽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡞⢻
⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⣀⠀⠀⢀⡠⠃⡽
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠪⠭⠤⠐⠊⠁
'''

spock_ascii = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⢸⣿⣷⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠈⣿⣿⡆⠀⠀⠀⠀⣼⣿⣿⠀⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡀⢹⣿⣧⠀⠀⠀⣸⣿⣿⠃⣰⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠘⣿⣿⡄⠀⢀⣿⣿⡏⢠⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡀⢻⣿⣧⠀⣸⣿⡟⢀⣾⣿⡿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣇⣸⣿⣿⣶⣿⣿⠁⣼⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⢿⣿⣿⣷⣦⣀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀
'''

welcome_banner = r"""
__        __   _                            _         
\ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
  \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
                                                     
       ✨ ROCK • PAPER • SCISSORS • LIZARD • SPOCK ✨
"""


lose = 'You lose.'
win = 'You win.'

class Game():

    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def rock(self, player_choice, computer_choice):
            if computer_choice == 'Spock':
                self.computer.points += 1
                return f'Rock has been vaporized. You lose.'
            elif computer_choice == 'Paper':
                self.computer.points += 1
                return f'Rock has been covered. You lose.'
            elif computer_choice in ['Lizard', 'Scissors']: 
                self.player.points += 1
                return f'Rock has crushed {computer_choice}. You win.'
            else:
                return 'Draw'
            
    def paper(self, player_choice, computer_choice):
            if computer_choice == 'Scissors':
                self.computer.points += 1
                return f'Paper has been cut. You lose.'
            elif computer_choice == 'Lizard':
                self.computer.points += 1
                return f'Paper has been eaten. {lose}.'
            elif computer_choice == 'Spock':
                self.player.points += 1
                return f'Paper has disproved Spock. {win}.'
            elif computer_choice == 'Rock':
                self.player.points += 1
                return f'Paper has covered Rock. {win}.'
            else:
                return 'Draw'
            
    def scissors(self, player_choice, computer_choice):
            if computer_choice == 'Rock':
                self.computer.points += 1
                return f'Scissors have been crushed. {lose}.'
            elif computer_choice == 'Spock':
                self.computer.points += 1
                return f'Scissors have been smashed. {lose}.'
            elif computer_choice == 'Paper':
                self.player.points += 1
                return f'Scissors have cut Paper. {win}.'
            elif computer_choice == 'Lizard':
                self.player.points += 1
                return f'Scissors have decapitated Lizard. {win}.'
            else:
                return 'Draw'
            
    def spock(self, player_choice, computer_choice):
            if computer_choice == 'Paper':
                self.computer.points += 1
                return f'Spock has been disproven. {lose}.'
            elif computer_choice == 'Lizard':
                self.computer.points += 1
                return f'Spock has been poisoned. {lose}.'
            elif computer_choice == 'Rock':
                self.player.points += 1
                return f'Spock has vaporized Rock. {win}.'
            elif computer_choice == 'Scissors':
                self.player.points += 1
                return f'Spock has smashed Scissors. {win}.'
            else:
                return 'Draw'
            
    def lizard(self, player_choice, computer_choice):
            if computer_choice == 'Rock':
                self.computer.points += 1
                return f'Lizard has been crushed. {lose}.'
            elif computer_choice == 'Scissors':
                self.computer.points += 1
                return f'Lizard has been decapitated. {lose}.'
            elif computer_choice == 'Paper':
                self.player.points += 1
                return f'Lizard has eaten Paper. {win}.'
            elif computer_choice == 'Spock':
                self.player.points += 1
                return f'Lizard has poisoned Spock. {win}.'
            else:
                return 'Draw'
            
            
    def play_game(self):
        print(welcome_banner)
        print(instructions)
        self.player = Player()
        self.computer = Computer()

        while self.player.points < 2 and self.computer.points < 2:
            player_choice = self.player.get_choice()

            while player_choice not in self.choices:
                print("Invalid choice. Please try again.")
                player_choice = self.player.get_choice()
                
            computer_choice = self.computer.random_choice()

            ascii_art = {
                 'Rock': rock_ascii,
                 'Paper': paper_ascii,
                 'Scissors': scissors_ascii,
                 'Lizard': lizard_ascii,
                 'Spock': spock_ascii
                 }
            print("🧍 You chose:")
            print(ascii_art[player_choice])
            print("🤖 Computer chose:")
            print(ascii_art[computer_choice])

            if player_choice == 'Rock':
                result = self.rock(player_choice, computer_choice)
            elif player_choice == 'Paper':
                result = self.paper(player_choice, computer_choice)
            elif player_choice == 'Scissors':
                result = self.scissors(player_choice, computer_choice)
            elif player_choice == 'Lizard':
                result = self.lizard(player_choice, computer_choice)
            elif player_choice == 'Spock':
                result = self.spock(player_choice, computer_choice)
            else:
                result = "Invalid choice."
        
            print (f'{result} Computer: {self.computer.points} You: {self.player.points}')

        if self.player.points == 2:
            print("Congratulations! You won the best of 3 series.")
            print(r"""
  ___   _   __  __ ___    _____   _____ ___ 
 / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \
| (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
 \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\
""")
        else:
            print("Computer wins the best of 3 series. Better luck next time!")
            print(r"""
  ___   _   __  __ ___    _____   _____ ___ 
 / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \
| (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /
 \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\
""")
         

    def play_round(self):
        self.play_game()

class Player():
    def __init__(self, name="You", choice="", score=()):
        self.name = name
        self.choice = choice
        self.score = score
        self.points = 0

    def get_choice(self):
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        choice = input('Pick One: Rock, Paper, Scissors, Lizard, Spock: ')
        choice = choice.capitalize()

        self.choice = choice
        return choice


class Computer():
    def __init__(self, choice="", score=()):
        self.choice = choice
        self.score = score
        self.points = 0

    def random_choice(self):
        choices = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.choice = random.choice(choices)
        return self.choice
    
if __name__ == "__main__":
    game = Game()
    game.play_round()