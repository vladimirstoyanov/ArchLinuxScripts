#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
  exit 1
fi

mkdir /home/$1
chmod 755 /home/$1
useradd -m $1
passwd $1
chown $1 /home/$1

#ToDo check if sudo package is installed
pacman --noconfirm -S sudo

echo "Adding $1 ALL=(ALL:ALL) ALL in /etc/sudoers"
chmod +w /etc/sudoers
VAR='/root ALL=(ALL:ALL) ALL/a '
VAR2="$1 ALL=(ALL:ALL) ALL"
sed -i "$VAR$VAR2" /etc/sudoers
chmod -w /etc/sudoers
echo "$1 ALL=(ALL:ALL) ALL"
