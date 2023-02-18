#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -Atom directory"
  exit 1
fi


cd $1
wget https://github.com/atom/atom/releases/download/v1.60.0/atom-amd64.tar.gz
tar -xvf *.tar.gz
cd atom-1.60.0-amd64
sudo ln -sf ${pwd}/atom /usr/bin/
