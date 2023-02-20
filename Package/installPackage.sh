#!/bin/sh

if [ $# -ne 1 ]
then
	echo "1 arg - a package."
	exit 1
fi

pacman --noconfirm -S $1
