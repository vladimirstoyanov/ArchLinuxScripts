if [ $# -ne 4 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - remote username"
        echo "2 arg - remote ip"
        echo "3 arg - remote path"
        echo "4 arg - location that you want copy the file"
  exit 1
fi

scp $1@$2:$3 $4
