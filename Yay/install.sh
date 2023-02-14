#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - yay directory"
  exit 1
fi


cd $1
git clone https://aur.archlinux.org/pacaur.git
cd yay
makepkg -si
