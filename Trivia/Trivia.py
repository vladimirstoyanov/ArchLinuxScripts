"""
Format:
<item>
<question>a question</question>
<answer>the answer of the question</answer>
<option1> a possible answer </option1>
<option2> a possible answer </option2>
<option3> a possible answer </option3>
<option4> a possible answer </option4>
</item>
"""
import random
import re

class Item:
    def __init__ (self, question, answer, option1, option2, option3, option4):
        self.question = question
        self.answer = answer
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4


class Trivia:
    def __init__ (self):
        self.listItems = []
        self.correct_answers = 0
        self.readQuestions()
        self.total = len(self.listItems)

    def parseItem (self, item):
        #remove item tag
        question = re.search(r'<question>(.*?)<\/question>', item).group(1)
        answer = re.search(r'<answer>(.*?)<\/answer>', item).group(1)
        option1 = re.search(r'<option1>(.*?)<\/option1>', item).group(1)
        option2 = re.search(r'<option2>(.*?)<\/option2>', item).group(1)
        option3 = re.search(r'<option3>(.*?)<\/option3>', item).group(1)
        option4 = re.search(r'<option4>(.*?)<\/option4>', item).group(1)

        item = Item(question, answer, option1, option2, option3, option4)
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
        print (self.listItems[index].question)
        print ("1) " + self.listItems[index].option1)
        print ("2) " + self.listItems[index].option2)
        print ("3) " + self.listItems[index].option3)
        print ("4) " + self.listItems[index].option4)

        val = input("Your answer: ")
        if (val == self.listItems[index].answer):
            print ("Corret!")
            self.correct_answers+=1
        else:
            print ("Not correct! The correct answer is " + self.listItems[index].answer)


triva = Trivia ()

listRandomIndexes = random.sample(range(0,triva.total), triva.total)

for i in range (len(listRandomIndexes)):
    triva.askQuestion(listRandomIndexes[i])

print ("Your score: " + str((triva.correct_answers/triva.total*100.0) + "%"))
