import os

def printText (text):
    #print (text)
    os.system('echo "' + text + '">/dev/usb/lp0')


text = '''
CNN reports:
Knowing you have higher than normal blood pressure — and taking medications daily to treat it — may be one key to avoiding dementia in later life, a new study found.

Scientists already know that having high blood pressure, particularly between ages 40 and 65, increases the risk of developing dementia in later life, said study coauthor Ruth Peters, an associate professor at the University of New South Wales in Australia, via email. But she added that research has been less clear on whether lowering blood pressure in older adults would reduce that risk. "What is so exciting about our study is that the data shows that those people who were taking the blood pressure lowering medication had a lower risk of a dementia diagnosis than those taking a matching placebo," said Peters, who is also a senior research scientist at Neuroscience Research Australia, a nonprofit research organization....

The study, published this week in the European Heart Journal, combined data from five large randomized, double-blinded clinical trials of more than 28,000 older adults with an average age of 69 from 20 countries. All had a history of hypertension. Each of the clinical trials compared people taking blood pressure medications with people taking a matching placebo pill and followed them for an average of 4.3 years.

Pooling the data, Peters and her team found that a drop of about 10 mm/Hg on the systolic and 4 mm/Hg on the diastolic blood pressure readings at 12 months significantly lowered the risk of a dementia diagnosis. In addition, there was a broad linear relationship: As blood pressure dropped, so did cognitive risk, which held true until at least 100 mm/Hg systolic and 70 mm/Hg diastolic, the study said. There was also no sign that blood pressure medications may harm blood flow into the brain at later ages.
'''
text = text.replace ('"', "'")
splitted = text.split('\n')
for i in range (len(splitted)):
    printText(splitted[i])
