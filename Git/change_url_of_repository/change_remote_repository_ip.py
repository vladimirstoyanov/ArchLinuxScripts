import subprocess
import os
import sys
class ChangeRemoteRepositoryIp:
        def __init__ (self):
            self.newUrl = ""
            self.remoteRepositoryPath=""
            self.checkInput()
            self.changeUrl ()

        def checkInput (self):
            if (len (sys.argv)!=3):
                print ("Wrong input! Please use the following input:")
                print ("arg 1 - new IP address of the repository")
                print ("arg 2 - the path of the repository")

                sys.exit()
            self.newUrl = sys.argv[1]
            self.remoteRepositoryPath = sys.argv[2]

        def changeUrl (self):
            arguments = [self.remoteRepositoryPath]
            command = ["bash", "print_remote_repository_url.sh"] + arguments
            output = subprocess.check_output(command, text=True)

            splitted = output.split ('(fetch)')
            oldUrl = splitted[0].strip()

            ip = oldUrl.split('@')[1]
            oldIp = ip.split(':')[0]

            newUrl = oldUrl.replace(oldIp, self.newUrl)

            print (newUrl)
            command = "sh change_remote_repository_url.sh " + newUrl + " " + self.remoteRepositoryPath
            print (command)
            os.system(command)


if __name__ == "__main__":
    changeRemoteRepositoryIp = ChangeRemoteRepositoryIp ()
