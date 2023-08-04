import random

import string

from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            "Hello World",
            "Velvet dreams",
            "Starlit night",
            "Pages of history",
            "Untold secrets"
            ]
        self.active_phrase = None
        self.guesses = []
        self.lives = None

    def welcome(self):
        print("Welcome to the Phrase Hunting Game!")
    
    def set_difficulty(self):
        difficulty = "\nchoose a difficulty:\n1)Easy\n2)Medium\n3)Hard\n"
        choice = "\nWhat difficulty would you like?(choices: 1, 2 or 3)\n>  "
        option = input(f"{difficulty}{choice}")
        while True:
            if option == "1":
                self.lives = 15
                break
            elif option == "2":
                self.lives = 10
                break
            elif option == "3":
                self.lives = 5
                break
            else:
                option = input(f"Incorrect Choice! Try again!\n{difficulty}{choice}")

    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        self.active_phrase = random_phrase.lower()

    def get_guess(self):
        guess_letter = input("\nWhat is your guess?\n>  ")
        try:
            if any(char in string.punctuation for char in guess_letter)\
                or len(guess_letter) > 1:
                raise ValueError("Error")
            elif guess_letter.isdigit():
                raise TypeError("Error")
            else:
                self.guesses.append(guess_letter.lower())
                self.check_if_missed(guess_letter)
        except ValueError:
            print(f"\nIncorrect input\nDetails: {guess_letter}")
        except TypeError:
            print(f"\nnumbers are not letters!\nDetails: {guess_letter}")
    
    def check_if_missed(self, guess):
        if guess not in self.active_phrase:
            self.missed += 1
        else:
            pass

    def game_over(self, obj, life):
        if obj.have_guessed:
            print("Congratulations you have Won!\nThank you for playing!")
            return True
        elif life == 0:
            print("You have lost!\nThank you for playing!")
            return True
        else:
            return False
        
    def reset_game(self):
        self.lives = None
        self.guesses = []
        self.get_random_phrase()
        self.missed = 0

    def start(self):
        self.welcome()
        self.set_difficulty()
        print(self.lives)
        self.get_random_phrase()
        phrase_obj = Phrase(self.active_phrase)
        while True:
            life_remaining = self.lives-self.missed
            phrase_obj.display(self.guesses)
            print(f"You have {life_remaining} out of {self.lives} lives")
            if self.game_over(phrase_obj, life_remaining):
                break
            self.get_guess()
        self.reset_game()
