#!/bin/sh
if [ $# -ne 2 ]
then
	echo "Put a comment as first argment and a path as second argument."
	exit 1
fi
cd $2

echo "git add --all"
git add --all

echo "git commit -m $1"
git commit -m "$1"

echo "git push origin"
git push origin
