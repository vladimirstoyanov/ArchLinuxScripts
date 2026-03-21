#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -repository path"
  exit 1
fi

git checkout --orphan clean-branch
git add .
git commit -m "Initial clean commit"
git branch -D main
git branch -m main
git push origin --force
