#!/bin/sh

if [ $# -ne 4 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - remote user name"
	echo "2 arg - remote ip"
	echo "3 arg - remote path of the project"
  echo "4 arg - local directory"
  exit 1
fi

cd $4 #my repo
rm -rf .git


git init
git add .
git commit -m "Removed history"

git remote add origin $1@$2:$3
git push -u --force origin master
