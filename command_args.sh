 #/bin/bash 
if [[ $# -eq 0 ]] ; then
    echo 'Please enter the arguments'
    exit 0
fi
echo "List of $# arguments given"
for i in $@; do 
   echo $i 
 done

