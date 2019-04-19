#$1 -a directory that is used to find a file
#$2 -a directory that 'sha256sum.txt' will be created

cd $1
find -type f -exec md5sum '{}' \; > $2/sha256sum.txt
