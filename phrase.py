class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.have_guessed = False

    def display(self, guesses):
        self.output_phrase = ""
        self.check_letter(guesses)
        self.check_complete(self.output_phrase)
        print(self.output_phrase)

    def check_letter(self, guesses):
        for letter in self.phrase:
            if " " in letter:
                self.output_phrase += " "
            elif letter in guesses:
                self.output_phrase += letter
            else:
                self.output_phrase += "_"

    def check_complete(self, output):
        if output == self.phrase:
            self.have_guessed = True
