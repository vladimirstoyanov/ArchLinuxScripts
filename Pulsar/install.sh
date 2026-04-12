#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -Atom directory"
  exit 1
fi


cd $1

https://github.com/pulsar-edit/pulsar/releases/pulsar-edit/pulsar/releases/download/v1.131.3/Linux.Pulsar-1.131.3.AppImage

wget https://github.com/pulsar-edit/pulsar/releases/pulsar-edit/pulsar/releases/download/v1.131.3/Linux.Pulsar-1.131.3.AppImage
chmod +x Linux.Pulsar-1.131.3.AppImage
sudo ln -sf Linux.Pulsar-1.131.3.AppImage /usr/bin/  
