#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - arg 1 - path to a directory to download the Crsytal Dock's repository"
  exit 1
fi

cd $1
git clone https://github.com/dangvd/crystal-dock.git

cmake -S src -B build -DCMAKE_INSTALL_PREFIX=/usr
cmake --build build --parallel
sudo cmake --install build

crystal-dock
