from getpass import getpass

class Game:
    guessedWord = []
    
    def __init__(self, name='Player', chances=7):
        self.name =  name
        self.chances = chances

    def __getWord(self):
        return getpass(prompt="Enter Word: ").lower()

    def __getCharacter(self):
        ch = input("Guess The Character of Word (Space Included): ").lower()
        return ch if len(ch) == 1 else None

    def __print_stick(self):
        for i in range(0, self.chances):
            print("|")

    def __printHangMan(self):
        print("|------")
        if (self.chances == 6):
            self.__print_stick()
            return
        print("|     |")
        if (self.chances == 5):
            self.__print_stick()
            return
        print("|   (* *)")
        if (self.chances == 4):
            self.__print_stick()
            return
        print("|     |  ")
        if (self.chances == 3):
            self.__print_stick()
            return
        print("|   --|--")
        if (self.chances == 2):
            self.__print_stick()
            return
        print("|     |")
        if (self.chances == 1):
            self.__print_stick()
            return
        print("|    / \\")
        print("|")

    def __insertTempWord(self, tempWord, word):
        for i in range(0, len(word)):
            if tempWord == word[i]:
                self.guessedWord[i] = word[i]

    def __insertLineInGuessedWord(self, wordLenght):
        for i in range(0, wordLenght):
            self.guessedWord.append('_')

    def play(self):
        word = self.__getWord()
        self.__insertLineInGuessedWord(len(word))
        while (self.chances and (''.join(self.guessedWord) != word)):
            print(''.join(self.guessedWord)+"\n")
            tempWord = self.__getCharacter()
            if tempWord and (tempWord not in word):
                self.chances -= 1
                print("Wrong Guess!!")
                self.__printHangMan()
            elif tempWord:
                if tempWord in self.guessedWord:
                    print("Already Inserted!!")
                else:
                    self.__insertTempWord(tempWord, word)
                    print("Correct Guess!!")
            else:
                print("Enter Single Character!!")
        if not self.chances:
            print(f"{self.name} Lost!!\nWord: {word}")
        else:
            print(f"{word}\n\n{self.name} Won!!")

if __name__ == "__main__":
    game = Game()
    game.play()