#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - user"
  echo "2 arg - group"
  exit 1
fi

cd /opt
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R $1:$2 ./yay-git
cd yay-git
makepkg -si
