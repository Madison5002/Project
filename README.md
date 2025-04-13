# Project


conda create --name project_lab python=3.13.1
conda activate project_lab


#Cecily Davis + Madison Parker - Rock Paper Scissors Lizard Spock - Project Milestone 3

To build the Rock, Paper, Scissors, Lizard, Spock game, we need to consider a series of steps. 

The game begins with initialization, where the rules are set (Establish classes). 
The user is prompted for entering a decision, whereas one at random is built by the computer (Take input). 
Then, the game logic processes both the choices and compares them by a set of predetermined rules in order to decide the winner.(For loop or if-then) 
The rules consider the ten potential collisions, such as "Rock crushes Scissors" and "Spock vaporizes Rock." (Return results)  
Having determined the winner, the game then moves to the user interface stage, where the options and the outcome are shown (Print results). 
Finally, a game loop is used where players are able to play several games, view how many they won/lost/tied, and decide when to quit the program. (While loop)

The game design is made up of three primary classes: Game, Player, and Computer. 
The Game class provides the hidden logic, for example, holding the rules within a dictionary, looping through all rounds with play_round(), getting the winner within determine_winner() by comparing selections, and presenting results with display_result(). 
The Player class interacts with the user through holding the player's name and selection by get_player() and validates with get_choice(). 
The Computer class produces the computer's selection using the generate_choice() method.

1.	Game (Main controller of the game)
Attributes:
rules: A dictionary that defines which choices defeat others.
Methods:
play_game(): Manages the game loop, allowing multiple rounds.
play_round(): Executes one round of the game.
determine_winner(player_choice, computer_choice): Compares the choices and returns the winner.
display_result(winner): Displays the outcome of the round.

2.	Player (Handles user input)
Attributes:
name: Stores the player’s name.
choice: Stores the player’s selected option.
Methods:
get_choice(): Asks the player to choose between Rock, Paper, Scissors, Lizard, or Spock and validates their input.

3.	Computer (Simulates an opponent)
Attributes:
choice: Stores the randomly chosen move.
Methods:
generate_choice(): Uses the random.choice() function to select a move.


