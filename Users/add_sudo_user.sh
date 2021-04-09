#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - username"
  exit 1
fi

mkdir /home/$1
useradd -m /home/$1
passwd $1

#ToDo check if sudo package is installed
pacman -S sudo

echo 'Adding $1 ALL=(ALL) ALL in /etc/sudoers'
sed '/root ALL=(ALL) ALL/a $1 ALL=(ALL) ALL' /etc/sudoers 

echo '$1 ALL=(ALL) ALL'
