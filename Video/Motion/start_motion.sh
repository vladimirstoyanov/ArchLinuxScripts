if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - time before execute in seconds"
  exit 1
fi

sleep $
motion -n -c $2
