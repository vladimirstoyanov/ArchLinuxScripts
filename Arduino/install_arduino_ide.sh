#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - arduino ide directory (e.g. /home/user/arduino_ide)"
  exit 1
fi

if [ -d "$1" ]; then
    echo "Directory exists"
else
    mkdir $1
fi

cd $1

git clone https://aur.archlinux.org/arduino-ide-bin.git
cd arduino-ide-bin

makepkg -si
