#!/bin/sh
if [ $# -ne 2 ]
then
        echo "1 arg - a package"
	echo "2 arg = package path"
        exit 1
fi



sudo pacman -S $1 --overwrite $2
