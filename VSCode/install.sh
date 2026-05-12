

#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - unity directory (e.g. /home/user/vscode)"
  exit 1
fi

mkdir -p $1
cd $1
git clone https://aur.archlinux.org/visual-studio-code-bin.git
cd visual-studio-code-bin
makepkg -si
