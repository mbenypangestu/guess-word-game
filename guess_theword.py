import random as rand
import pandas as pd

class Data:
    def __init__(self, index, word):
        self._index = index
        self._word  = word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):
        self._word = word

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, index):
        self._index = index

class GameProperty:
    def __init__(self):
        self._score = 0
        self._current_word = None
        self._current_answer = None

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def current_word(self):
        return self._current_word

    @current_word.setter
    def current_word(self, current_word):
        self._current_word = current_word

    @property
    def current_answer(self):
        return self._current_answer

    @current_answer.setter
    def current_answer(self, current_answer):
        self._current_answer = current_answer

class GuessWord:
    def __init__(self):
        self._datas = []
        self._game_property = GameProperty()

    @property
    def datas(self):
        return self._datas

    @datas.setter
    def datas(self, datas):
        self._datas = datas

    def addData(self, data):
        self.datas.append(data)

    @property
    def game_property(self):
        return self._game_property

    @game_property.setter
    def game_property(self, game_property):
        self._game_property = game_property

    def start(self):
        print("================== Game Tebak Kata ==================\n")

        while(True):
            self.generateGuessWord()
            self.getAnswer()
            self.checkAnswer()
            self.getScore()

            coba = input("\nMau coba lagi (y/n) ? ")
            if coba != "y" and coba != "Y":
                self.getScore()
                break

        print("\n======================= Finish ======================")

    def generateGuessWord(self):
        data_length = len(self.datas)

        choosen_index   = rand.randrange(0, data_length - 1)
        choosen_word    = self.datas[choosen_index].word
        self.game_property.current_word = choosen_word

        shuffled_word   = list(choosen_word)
        rand.shuffle(shuffled_word)
        shuffled_word = ''.join(shuffled_word)

        print("Tebak kata berikut : ", shuffled_word)

    def getAnswer(self):
        answer = input("Jawab : ")
        self.game_property.current_answer = answer

    def isAnswerCorrect(self):
        if self.game_property.current_answer == self.game_property.current_word:
            return True
        else:
            return False

    def checkAnswer(self):
        if self.isAnswerCorrect() == True:
            self.game_property.score = self.game_property.score + 1
            print("ANDA BENAR !! Horrayyy")
        else:
            print("ANDA SALAH !! Silahkan coba lagi :(")
            print("Jawaban yang benar : ", self.game_property.current_word)

    def getScore(self):
        print("\nScore : ", self.game_property.score)


def main():
    file        = pd.read_csv("data.csv", sep=',')
    datafile    = pd.DataFrame(file)

    gw = GuessWord()

    for i in range(len(datafile)):
        data = Data(i, datafile["WORD"][i])
        gw.addData(data)

    gw.start()

if __name__ == '__main__':
    main()