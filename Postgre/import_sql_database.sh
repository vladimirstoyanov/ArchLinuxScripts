#!/bin/sh
if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
  echo "1 arg - postgre database"
  echo "2 arg - sql database (e.g. dump.sql)"
  exit 1
fi

psql -U postgres -d $1 -f $2
