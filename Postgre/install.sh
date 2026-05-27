#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
	echo "1 arg  - arg 1 - username"
  exit 1
fi

sudo pacman -S postgresql
echo "1. Switch to the postgres user"
sudo -i -u postgres

echo "2. Initialize the database storage"

echo "Exit the postgres user session to go back to your normal user"
initdb -D /var/lib/postgres/data

exit

echo "Start the server right now"
sudo systemctl start postgresql

echo "Enable it to start automatically on boot"
sudo systemctl enable postgresql

sudo -i -u postgres

createuser --interactive --pwprompt $1
createdb $1
