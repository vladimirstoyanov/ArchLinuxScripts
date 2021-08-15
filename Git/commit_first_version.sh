#!/bin/sh
#$1 - local project directory
#$2 - remote username
#$3 - remote ip
#$4 - remote directory

if [ $# -ne 4 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - local project directory"
        echo "2 arg - remote username"
        echo "3 arg - remote ip"
        echo "4 arg - remote directory"
  exit 1
fi


cd $1
git init
git add .
git commit -m 'Initial commit'
git remote add origin $2@$3:$4
git push origin master
