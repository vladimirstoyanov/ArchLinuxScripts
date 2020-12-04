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
    def __init__ (self, filename):
        self.correctAnswers = 0
        file = WordsFile (filename)
        self.listWords = file.readWords()
        self.total = len (self.listWords)
        self.allQuestions = self.total * 2
        self.listRandomIndexes = random.sample(xrange(self.total), self.total)
        self.indexEnglishWords = 0
        self.indexBulgarianWords = 1
        self.currentWord = 0
        self.guessWords(self.indexEnglishWords, self.indexBulgarianWords)
        self.guessWords(self.indexBulgarianWords, self.indexEnglishWords)
        self.finalResult ()

    def finalResult (self):
        percentage = self.calculatePercentage(self.allQuestions)
        print ("====The test has finsihsed. Result:")
        print (str(percentage) + '%')
        if(percentage < 95 ):
            print ("The test hasn't been passed")
        else:
            print ("Congratulations!")

    def calculatePercentage (self, total):
            return ((self.correctAnswers/((total)*1.0)) *100)

    def ask(self, words):
        for i in range (len(words)):
                word = u''.join(words[i]).encode('utf-8').strip()
                print (word)
        print ("Your answer: ")
        userAnswer = raw_input()
        return userAnswer

    def isMatch (self, answer, words):
        word = ""
        for i in range (len(words)):
                word = u''.join(words[i]).encode('utf-8').strip()
                if (answer == word):
                            print ("=====That's right!")
                            self.correctAnswers+=1
        print ("=====Wrong answer! The correct one is: " + word)

    def guessWords (self, indexAsk, indexAnswer):
        for i in range (len(self.listRandomIndexes)):
            userAnswer = self.ask(self.listWords[self.listRandomIndexes[i]][indexAsk])
            self.isMatch(userAnswer, self.listWords[self.listRandomIndexes[i]][indexAnswer])
            self.currentWord+=1
            print ("Question " + str (self.currentWord) + "/" + str(self.allQuestions) +
                ", current score: " + str(round(self.calculatePercentage(self.currentWord),2)) + "%")

learnEnglishWords = LearnEnglishWords ('words')
