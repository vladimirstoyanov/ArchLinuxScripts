import os
import sys


class MountPartitionFstab:
    def __init__ (self, partition, mountDirectory):
        self.partition = partition
        self.mountDirectory = mountDirectory
        self.mount ()

    def __getUuid (self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        os.system("blkid > " + dir_path + "/list.txt")
        f = open (dir_path + "/list.txt", "r")

        for line in f.readlines():
            if (-1 != line.find(self.partition)):
                l_split = line.split(' ')
                l_split_id = l_split[1].split('=')
                uuid = l_split_id[1]
                uuid = uuid.replace("\"", '')
                f.close()
                os.system('rm ' + dir_path + '/list.txt')
                return uuid

        f.close()

        os.system('rm ' + dir_path + '/list.txt')
        return ""

    def mount (self):
        uuid = self.__getUuid ()
        if ("" == uuid):
            print ("Can't get UUID of partition " + self.partition)
            sys.exit()
        print ("UUID: " + uuid)

        fstabString = "UUID=" + uuid + '\t' + self.mountDirectory + "\t\text4\t\trw,relatime\t0 2"

        print ("Adding " + fstabString)
        os.system ("echo \"" + fstabString + "\" >> /etc/fstab")

if __name__ == '__main__':
    partition = input("Partition (e.g. /dev/sda1): ")
    mountDir = input ("Mount directory (e.g. /home/user): ")

    mountPartitionFstab = MountPartitionFstab (partition, mountDir)
