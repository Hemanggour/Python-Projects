class Quiz():
    numOfQue = 0
    ques = []
    ans = []

    def __init__(self):
        self.__getAns()
        self.__getQue()

    def __getAns(self):
        try:
            with open("answers.txt", 'r', encoding='utf-8') as file:
                self.ans = [line.strip() for line in file.readlines()]
        except Exception as e:
            print(f"Error: {e}")

    def __getQue(self):
        try:
            with open("questions.txt", 'r', encoding='utf-8') as file:
                self.ques = [line.strip() for line in file.readlines()]
                self.numOfQue = len(self.ques)
        except Exception as e:
            print(f"Error: {e}")

    def play(self):
        correct, wrong = 0, 0
        count = 0
        ansInd = 0
        name = input("Enter Your Name: ")
        self.__getQue()
        self.__getAns()
        while count < self.numOfQue:
            for num in range(count, min(count+5, self.numOfQue)):
                print(f"{self.ques[num]}")
                count += 1
            answer = input("Select Option (a/b/c/d): ").lower().strip()
            if ansInd < len(self.ans):
                if answer == self.ans[ansInd][0]:
                    print("Correct Answer!!\n")
                    correct += 1
                    ansInd += 1
                elif (answer == 'a') or (answer == 'b') or (answer == 'c') or (answer == 'd'):
                    print("Wrong Answer!!")
                    wrong += 1
                    print(f"Answer: {self.ans[ansInd]}")
                    ansInd += 1
                else:
                    print("Invalid Option!!\n")
                    count -= 5
        print(f"{name} Your Result:\nCorrect: {correct}\nWrong: {wrong}\nAccuracy: {(((correct)/(wrong + correct)) * 100)}%")

if __name__ == '__main__':
    game = Quiz()
    game.play()