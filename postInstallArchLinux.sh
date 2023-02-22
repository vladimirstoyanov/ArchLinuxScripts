#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
  exit 1
fi

hwclock --systohc
locale-gen
echo "127.0.0.1	localhost">> /etc/hostname
echo "::1		localhost" >>/etc/hostname
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
sh config.sh
exit
