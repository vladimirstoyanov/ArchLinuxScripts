#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg - path to metadata.desktop file to your project"
  exit 1
fi
plasmoidviewer --applet $1
