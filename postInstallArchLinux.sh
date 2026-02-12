#!/bin/sh

if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
        echo "2 arg - boot partition (e.g. /dev/sda)"
        echo "3 arg - computer name"
  exit 1
fi

hwclock --systohc
locale-gen
echo $3 >> /etc/hostname
mkinitcpio -P

echo "Enter root password"
passwd

pacman --noconfirm -S git

echo "Creating a user $1"
useradd -m $1
passwd $1
chmod 755 /home/$1

echo "Changing the user to $1"
su $1

cd /home
git clone https://github.com/vladimirstoyanov/ArchLinuxScripts.git
cd ArchLinuxScripts

su root
cd /home/ArchLinuxScripts

pacman --noconfirm -S sudo
pacman --noconfirm -S python
python ./Users/add_sudo_user.py

sh install.sh $1

su root

sh config.sh $2
