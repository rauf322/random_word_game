from random_word import Wordnik


class MakeWord():
    def __init__(self):
        self.word = Wordnik().get_random_word()


    # def __str__(self):
    #     return f"Random word is: {self.word=}"

class Guess(MakeWord):
    def __init__(self):
        super().__init__()
        self.guess = ["_"] * len(self.word)
        self.stash = ""


    
class TriesToFind(Guess):
    def __init__(self):
        super().__init__()
        self.count = len(self.word)*2

    def __str__(self):
        return f"Welcome to the Fun moment of our game!\nYou suppose to guess the word which contains of {len(self.word)} letter, each letter that u was using before will be contains in stash"

    def time_to_guess(self):
        tries = 0
        while tries < self.count:
            letter = self.check_letter()
            tries += 1
            self.stash += letter
            indices = [i for i, letters in enumerate(self.word) if letters == letter]
            for i in indices: 
                self.guess[i] = letter
            print(self.guess)
            if "_" not in self.guess:
                return "You won!"
        return f"You've lost! The word was {self.word=}"

    def check_letter(self):
        print(f"By now the stash holds this letters {self.stash}")
        letter = input(f"Provide the letter of word:")
        while len(letter) != 1:
            letter = input("Provide the letter of word which contains one letter: ")
        if letter in self.stash:
            print("Are u pity you was using this letter before be careful!")
        self.count -= 1
        print(f"By now you have that many tries got left {self.count}")
        return letter
            
        

        


    

a = TriesToFind()
print(a)
print(a.time_to_guess())