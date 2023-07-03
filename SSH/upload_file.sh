if [ $# -ne 4 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - filename"
        echo "2 arg - remote username"
        echo "3 arg - remote ip"
        echo "4 arg - remote path"
  exit 1
fi

scp $1 $2@$3:$4
