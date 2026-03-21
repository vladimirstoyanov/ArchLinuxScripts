if [ $# -ne 1 ]
then
  echo "Wrong input! please use the following input: "
        echo "arg1 -AI model name"
  exit 1
fi


ollama show $1
