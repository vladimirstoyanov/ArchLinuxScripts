#!/bin/sh

if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -Pulsar directory"
  exit 1
fi


cd $1

wget https://github.com/pulsar-edit/pulsar/releases/pulsar/releases/download/v1.131.3/Linux.Pulsar-1.131.3.AppImage
chmod +x Linux.Pulsar-1.131.3.AppImage
sudo ln -sf Linux.Pulsar-1.131.3.AppImage /usr/bin/

#copy some settings (disabled auto bracket module, some key mappings)
cp config.cson $HOME/.pulsar/
cp keymap.cson $HOME/.pulsar/
