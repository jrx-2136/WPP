import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]
    
    def get_computer_choice(self):
        return random.choice(self.choices)
    
    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_wins += 1
            return "You win!"
        else:
            self.computer_wins += 1
            return "Computer wins!"
    
    def check_winner(self):
        if self.user_wins > self.computer_wins:
            return "You won the game!"
        elif self.computer_wins > self.user_wins:
            return "Computer won the game!"
        else:
            return "The game is a tie!"
    
    def play(self):
        while self.current_round < self.rounds:
            self.current_round += 1
            print(f"Round {self.current_round}")
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in self.choices:
                print("Invalid choice, try again!")
                continue
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            print(self.find_winner(user_choice, computer_choice))
            print()
        
        print(self.check_winner())

# Example game
rounds = int(input("Enter number of rounds: "))
game = RockPaperScissors(rounds)
game.play()