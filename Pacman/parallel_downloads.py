import os
pacmanConfFile = "/etc/pacman.conf"

f = open (pacmanConfFile, "r")
f1 = open (pacmanConfFile + "_new", "w")

for line in f.readlines ():
    if (line.find ("ParallelDownloads")!=-1):
        line = line.replace("#", "") #remove the comment 

    f1.write (line)

f.close()
f1.close()

os.system ("cp " + pacmanConfFile + " " + pacmanConfFile +"_backup")
os.system ("mv " + pacmanConfFile + "_new " + pacmanConfFile)
