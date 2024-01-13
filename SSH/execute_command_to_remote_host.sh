if [ $# -ne 3 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - remote username"
        echo "2 arg - remote ip"
        echo "3 arg - remote command"
  exit 1
fi

ssh $1@$2 "$3"
