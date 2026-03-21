#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -repository path"
  exit 1
fi

cd $1
git checkout --orphan clean-branch
git add .
git commit -m "Initial clean commit"
git branch -D master
git branch -m master
git push --force --set-upstream origin master
