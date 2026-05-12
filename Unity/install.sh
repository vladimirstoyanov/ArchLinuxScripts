#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - unity directory (e.g. /home/user/unity)"
  exit 1
fi

mkdir -p $1
cd $1
git clone https://aur.archlinux.org/unityhub.git
cd unityhub
makepkg -si
