#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - email"
        echo "2 arg - username"
  exit 1
fi

git config --global user.email "$1"
git config --global user.name "$2"
