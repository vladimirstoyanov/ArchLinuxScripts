#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -Atom directory"
  exit 1
fi

cd $1
wget https://github.com/atom/atom/releases/tag/v1.63.1/atom-amd64.tar.gz

cd atom-1.63.1-amd64

sudo ln -sf ${pwd}/atom /usr/bin/
