if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - time before execute in seconds"
        echo "2 arg - path to motion.conf"
  exit 1
fi

sleep 300
motion -n -c motion.conf
