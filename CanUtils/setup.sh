#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg  - can-utils directory"
  exit 1
fi

#$1 - SocketCan directory
cd $1

git clone https://github.com/linux-can/can-utils
cd can-utils
make
sudo make install
