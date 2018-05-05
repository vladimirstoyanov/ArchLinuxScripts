import os
import sys

image = 'Resources/scitickart.png'
current_dir = os.getcwd()
current_dir+='/'

f = open ('./Resources/plasma-org.kde.plasma.desktop-appletsrc', 'r')
f1 = open ('./Resources/plasma-org.kde.plasma.desktop-appletsrc_tmp', 'w')

for str1 in f.readlines():
	if (str1.find('Image=')!=-1):
		f1.write('Image=' + current_dir + image + '\n')
		continue
	f1.write(str1)

f.close()
f1.close()

#Replaceing the temporary file with the original one
os.system("mv Resources/plasma-org.kde.plasma.desktop-appletsrc_tmp Resources/plasma-org.kde.plasma.desktop-appletsrc")
os.system('chmod 777 Resources/plasma-org.kde.plasma.desktop-appletsrc')

f = open('Resources/plasmarc', 'r')
f1 = open('Resources/plasmarc_tmp', 'w')

for str1 in f.readlines():
	if (str1.find('usersWallpapers=')!=-1):
		f1.write('usersWallpapers=' + current_dir + image + '\n')
		continue
	f1.write(str1)

f.close()
f1.close()

#Replacing the temorary file with the original one
os.system('mv Resources/plasmarc_tmp Resources/plasmarc')
os.system('chmod 777 Resources/plasmarc')
