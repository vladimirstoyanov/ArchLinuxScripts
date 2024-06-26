#!/bin/sh

if [ $# -ne 2 ]
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

cd /home
git clone https://github.com/vladimirstoyanov/ArchLinuxScripts.git
cd ArchLinuxScripts

echo "Creating a user $1"
sh ./Users/add_sudo_user.sh $1

sh install.sh
sh config.sh $2
exit
