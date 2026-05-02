#!/bin/bash
#$1 - directory
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - install directory"
  exit 1
fi

sudo pacman -S --needed gcc git make flex bison gperf python python-pip cmake ninja ccache
mkdir -p $1
cd $1
git clone --recursive https://github.com/espressif/esp-idf.git
cd esp-idf
./install.sh all
alias get_esp="source $1/esp-idf/export.sh"
