#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - list file in a image (e.g. /boot/initramfs-linux.img)"
        echo "2 arg - kernel version (e.g. 5.7.12-arch1-1. You can use uname -a command.)"
  exit 1
fi

lsinitcpio $1
