import os 
import sys

if (len(sys.argv)!=3):
	print "user input:"
	print "1 arg - directory"
	print "2 arg - md5sum"
	sys.exit()


directory = sys.argv[1]
sha256sum = sys.argv[2]

#check is directory exist
print(os.path.isdir(directory))

if (os.path.isdir(directory)==False):
	print "Directory: " + directory + " doesn't exist!"
	sys.exit()


current_directory = os.path.dirname(os.path.realpath(__file__))
os.system('sh helper.sh ' + directory + ' ' + current_directory)

f = open ('sha256sum.txt', 'r')

for str1 in f.readlines():
  if (str1.find(sha256sum) !=-1):
    print 'File has been found: '
    print str1
    f.close()
    sys.exit()

print "File hasn't been found."
os.system ('rm sha256sum.txt')

f.close()
