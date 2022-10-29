import os

def printText (text):
    #print (text)
    os.system('echo "' + text + '">/dev/usb/lp0')


text = '''
- sign documents with a notary for the hours on Friday - 10000pt
- read the book about diabetes type 2 - 10000pt
- find a free VPN; -5000pt
- Fix the amplifier - 20000pt
- Research neuron network for understanding a text; - 10000pt
- flasher - 30000pt
- flash a MQB dashboard with AES troj - 10000pt
- leak the MQB dashboard key - 10000pt
'''
text = text.replace ('"', "'")
splitted = text.split('\n')
for i in range (len(splitted)):
    printText(splitted[i])
