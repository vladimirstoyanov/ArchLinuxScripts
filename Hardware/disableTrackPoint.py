import os

os.system("xinput list > list.txt")

f = open ("list.txt", "r")

for str1 in f.readlines():
	if (-1 != str1.find('TrackPoint')):
		l_split = str1.split('\t')
		#print (l_split)
		l_split_id = l_split[1].split('=')
		#print(l_split_id[1])
		os.system ('xinput --disable ' + l_split_id[1])
f.close()

os.system('rm list.txt')
