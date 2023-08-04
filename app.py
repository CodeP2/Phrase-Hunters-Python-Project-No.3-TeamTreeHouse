from game import Game


if __name__ == "__main__":
    game = Game()
    #game.start()
    while True:
        question = input("Would you like to play again?(Y/N)\n>  ")
        if question.lower() == "y":
            game.start()
        elif question.lower() == "n":
            print("Goodbye!")
            break
        else:
            print("Incorrect choice! try again!\n")
