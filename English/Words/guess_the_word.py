import codecs
import io
import locale
import random
import sys
import time

class WordsFile:
    def __init__ (self, filename):
        self.filename = filename

    def readWords(self):
            f = codecs.open(self.filename, encoding ='utf-8', mode = 'r')
            listWords = []
            for line in f.readlines ():
                englishBulgarianWords = line.split (' - ')
                if (len(englishBulgarianWords) < 2):
                        continue
                bulgarianWords = englishBulgarianWords[1].split (', ')
                englishBulgarianWords[0] = u''.join(englishBulgarianWords[0]).encode('utf-8').strip()
                listBulgarianWords = []
                for i in range (len(bulgarianWords)):
                    bulgarianWords[i] = bulgarianWords[i].replace('\n','')
                    bulgarianWords[i] = bulgarianWords[i].replace('\r','')
                listWords.append([[englishBulgarianWords[0]], bulgarianWords])
            f.close()
            return listWords

class LearnEnglishWords:
    def __init__ (self, filename, listWords):
        self.correctAnswers = 0
        self.listWords = listWords
        self.total = len (self.listWords)
        self.allQuestions = self.total * 2
        self.listRandomIndexes = random.sample(xrange(self.total), self.total)
        self.indexEnglishWords = 0
        self.indexBulgarianWords = 1
        self.currentWord = 0

    def __ask(self, words):
        for i in range (len(words)):
                word = u''.join(words[i]).encode('utf-8').strip()
                print (word)
        print ("Your answer: ")
        userAnswer = raw_input()
        return userAnswer

    def __calculatePercentage (self, total):
            return ((self.correctAnswers/((total)*1.0)) *100)

    def __checkAnswer (self, answer, words):
        word = ""
        for i in range (len(words)):
                word = u''.join(words[i]).encode('utf-8').strip()
                if (answer == word):
                            print ("=====That's right!")
                            self.correctAnswers+=1
                            return
        print ("=====Wrong answer! The correct one is: " + word)

    def guessWords (self, indexAsk, indexAnswer):
        for i in range (len(self.listRandomIndexes)):
            userAnswer = self.__ask(self.listWords[self.listRandomIndexes[i]][indexAsk])
            self.__checkAnswer(userAnswer, self.listWords[self.listRandomIndexes[i]][indexAnswer])
            self.currentWord+=1
            print ("Question " + str (self.currentWord) + "/" + str(self.allQuestions) +
                ", current score: " + str(round(self.__calculatePercentage(self.currentWord),2)) + "%")

    def finalResult (self):
        percentage = self.__calculatePercentage(self.allQuestions)
        print ("====The test has finsihsed. Result:")
        print (str(percentage) + '%')
        if(percentage < 95 ):
            print ("The test hasn't been passed")
        else:
            print ("Congratulations!")

if __name__ == "__main__":
    filename = 'words'
    file = WordsFile (filename)
    listWords = file.readWords ()
    learnEnglishWords = LearnEnglishWords (filename, listWords)
    learnEnglishWords.guessWords(learnEnglishWords.indexEnglishWords, learnEnglishWords.indexBulgarianWords)
    learnEnglishWords.guessWords(learnEnglishWords.indexBulgarianWords, learnEnglishWords.indexEnglishWords)
    learnEnglishWords.finalResult ()
