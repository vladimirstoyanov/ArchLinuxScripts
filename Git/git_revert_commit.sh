#!/bin/sh
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - hash of a commit (check git log)"
	echo "2 arg - a comment"
  exit 1
fi

git revert $1
git -m commit "$2"
git push -u origin master
