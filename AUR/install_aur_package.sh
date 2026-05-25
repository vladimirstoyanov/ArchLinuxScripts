#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - aur repository (e.g. https://aur.archlinux.org/open-webui.git)"
        echo "2 arg - project directory (e.g. /home/user/OpenWebUI)"
  exit 1
fi

DIR_NAME=$(basename "$1" .git)


if [ -d "$2" ]; then
    echo "Directory exists"
else
    mkdir $2
fi

cd $2

echo "Cloning into: $DIR_NAME"
git clone $1
cd $DIR_NAME

makepkg -si
