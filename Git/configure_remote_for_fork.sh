#!/bin/sh

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - Fork path"
        echo "2 arg - remote repository (e.g. https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git)"
        echo "3 arg - branch name (e.g. develop)"
  exit 1
fi

cd $1
git remote add upstream $2
git checkout -b $3
