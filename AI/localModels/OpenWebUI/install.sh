#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - aur repository (e.g. https://aur.archlinux.org/open-webui.git)"
        echo "2 arg - project directory (e.g. /home/user/OpenWebUI)"
  exit 1
fi

cd ../../../AUR/
pwd

sh install_aur_package.sh $1 $2
