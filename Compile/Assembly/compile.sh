#$1 executable file
#$2 source file

if [ $# -ne 2 ]
then
  echo "Wrong input! please use the following input: "
        echo "1 arg - executable file name"
        echo "2 arg - source file name"
  exit 1
fi


nasm -f elf64 -o $1.o $2
ld $1.o -o $1
