#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - auracle git directory. If there aren't such directory, pleace create it!"
  exit 1
fi

sudo pacman -S meson --noconfirm
sudo pacman -S fakechroot --noconfirm
sudo pacman -S gtest --noconfirm

cd $1
wget https://aur.archlinux.org/cgit/aur.git/snapshot/auracle-git.tar.gz
tar -xzf auracle-git.tar.gz
cd auracle-git
makepkg PKGBUILD --skippgpcheck --noconfirm
sudo pacman -U auracle-git-*
