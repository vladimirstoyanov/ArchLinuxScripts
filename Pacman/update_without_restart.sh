#!/bin/sh

UPDATE_FILE=/tmp/updateLog.txt

#update the system
echo "==============Trying to update the system..." >> $UPDATE_FILE
pacman -Suy --noconfirm >> $UPDATE_FILE
echo "==============Update finished..." >>$UPDATE_FILE
