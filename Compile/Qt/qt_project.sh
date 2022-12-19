#!/bin/sh
#"C:\Qt\5.12.3\msvc2017_64\bin\qtenv2.bat"
if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - project directory"
        echo "2 arg - name of .pro file"
  exit 1
fi

cd $1
mkdir build
cd build

qmake -o Makefile ../$2
make 
