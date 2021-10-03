"""
Format:
<item>
<question>a question</question>
<answer>the answer of the question</answer>
<option1> a possible answer </option1>
<option2> a possible answer </option2>
....
<optionN> a possible answer </optionN>
</item>
"""
import random
import re

class Item:
    def __init__ (self, question, answer, possibleAnswers):
        self.question = question
        self.answer = answer
        self.possibleAnswers = possibleAnswers


class Trivia:
    def __init__ (self):
        self.listItems = []
        self.correct_answers = 0
        self.readQuestions()
        self.current_question = 1
        self.total = len(self.listItems)

    def parseItem (self, item):
        question = re.search(r'<question>(.*?)<\/question>', item).group(1)
        answer = re.search(r'<answer>(.*?)<\/answer>', item).group(1)
        possibleAnswersCount = 1
        possibleAnswers = []
        while (True):
            try:
                possibleAnswer = re.search(r'<option' + str(possibleAnswersCount) + '>(.*?)<\/option' +str(possibleAnswersCount) + '>', item).group(1)
                possibleAnswersCount+=1
                possibleAnswers.append(possibleAnswer)
            except:
                break

        item = Item(question, answer, possibleAnswers)
        self.listItems.append(item)

    def readQuestions (self):
        f=open("trivia", 'r')
        item_tag = ""
        begin_item = False
        for line in f.readlines():
            if (line.find('</item>')!=-1):
                begin_item = False
                item_tag+=line
                self.parseItem (item_tag)
                item_tag = ""
                continue

            if (line.find ('<item>')!=-1):
                begin_item = True

            if (begin_item == True):
                item_tag+=line

    def askQuestion (self, index):
        print (str(self.current_question) + ". " + self.listItems[index].question)

        for i in range (len(self.listItems[index].possibleAnswers)):
            print (str((i+1)) + ") " + self.listItems[index].possibleAnswers[i])

        val = input("Your answer: ")
        if (val == self.listItems[index].answer):
            print ("Corret!")
            self.correct_answers+=1
        else:
            print ("Not correct! The correct answer is " + self.listItems[index].answer)
        self.current_question+=1


triva = Trivia ()

listRandomIndexes = random.sample(range(0,triva.total), triva.total)
print ("Total questions: " + str(len(listRandomIndexes)))

for i in range (len(listRandomIndexes)):
    triva.askQuestion(listRandomIndexes[i])

print ("Your score: " + str((triva.correct_answers/triva.total*100.0)) + "%")
