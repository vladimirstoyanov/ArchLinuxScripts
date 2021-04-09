#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - partition (e.g. /dev/sda)"
  exit 1
fi

sudo pacman --noconfirm -S grub
sudo grub-install --target=i386-pc $1
sudo sh regenerate_grub.sh
