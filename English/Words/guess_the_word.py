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
        l1[0] = u''.join(l1[0]).encode('utf-8').strip()
        #print "l1: " + str(l1[0])
        l21 = []
        for i in range (len(l2)):
            #d = l2[i].decode ('cp1251')
            l2[i] = l2[i].replace('\n','')
            l2[i] = l2[i].replace('\r','')
            #l2[i] = u''.join(l2[i]).encode('utf-8').strip()
            l21.append(l2[i])
            
        l3 = []
        l3.append(l1[0])
        l3.append(l21)
        #print l3
        l_words.append(l3)

    f.close()
    return l_words

def input_unicode ():
    text= raw_input()
    return text


l_words = read_file ()    

total = len (l_words)
print (total)
all_questions = total * 2
i = 0
correct_answers = 0
my_randoms = random.sample(xrange(total), total)


for i in range (len(my_randoms)):
        word = ""
        print (l_words[my_randoms[i]][0])
        print ("Your answer: ")
        input_string = input_unicode ()
        
        answered = 0
        for j in range (len(l_words[my_randoms[i]][1])):
                word = u''.join(l_words[my_randoms[i]][1][j]).encode('utf-8').strip()
                if (input_string == word):
                        print ("=====That's right!")
                        correct_answers+=1
                        answered = 1
                        break
        if (answered == 0):
                print ("=====Wrong answer! The correct one is: " + word)
        
        current_percentage = (correct_answers/((i+1)*1.0)) *100
        print ("Question " + str (i+1) + "/" + str(all_questions) + ", current score: " + str(round(current_percentage,2)) + "%") 



for i in range (len(my_randoms)):
        word = ""
        for j in range (len(l_words[my_randoms[i]][1])):
                word = u''.join(l_words[my_randoms[i]][1][j]).encode('utf-8').strip()
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
