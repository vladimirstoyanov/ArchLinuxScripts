import sys
import locale
import io
import codecs
import time
import random

def read_file ():
    f = codecs.open('words', encoding ='utf-8', mode = 'r')

    l_words = []
    for str1 in f.readlines ():
        l1 = str1.split (' - ')
        if (len(l1) <2):
                continue

        l2 = l1[1].split (', ')
        l21 = []
        for i in range (len(l2)):
            l2[i] = l2[i].replace('\n','')
            l2[i] = l2[i].replace('\r','')
            l21.append(l2[i])

        l3 = []
        l3.append(str(l1[0]))
        l3.append(l21)
        l_words.append(l3)

    f.close()
    return l_words

def input_unicode ():
    text= input()
    return text


l_words = read_file ()

total = len (l_words)
print (total)
all_questions = total * 2
i = 0
correct_answers = 0
my_randoms = random.sample(range(total), total)


for i in range (len(my_randoms)):
        word = ""
        print (l_words[my_randoms[i]][0])
        print ("Your answer: ")
        input_string = input_unicode ()

        answered = 0
        for j in range (len(l_words[my_randoms[i]][1])):
                word = l_words[my_randoms[i]][1][j]
                if (input_string == word):
                        print ("=====That's right!")
                        correct_answers+=1
                        answered = 1
                        break
        if (answered == 0):
                print ("=====Wrong answer! The correct one is: " + str(word))

        current_percentage = (correct_answers/((i+1)*1.0)) *100
        print ("Question " + str (i+1) + "/" + str(all_questions) + ", current score: " + str(round(current_percentage,2)) + "%")



for i in range (len(my_randoms)):
        word = ""
        for j in range (len(l_words[my_randoms[i]][1])):
                word = l_words[my_randoms[i]][1][j]
                print (word)
        print ("Your answer: ")
        input_string = input_unicode ()
        #compare
        if (input_string == l_words[my_randoms[i]][0]):
            print ("=====That's right!")
            correct_answers+=1
        else:
            print ("=====Wrong answer! The correct one is: " + l_words[my_randoms[i]][0])

        current_percentage = (correct_answers/((total + i+1)*1.0)) *100
        print ("Question " + str (total + i+1) + "/" + str(all_questions) + ", current score: " + str(round(current_percentage,2)) + "%")

print ("====Test finsihsed. Result:")
total*=2
percentage = (correct_answers/(total*1.0)) * 100
print (str(percentage) + '%')
if(percentage < 95 ):
    print ("Didn't pass")
else:
    print ("Pass")
