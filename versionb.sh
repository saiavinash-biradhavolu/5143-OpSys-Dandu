#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo 'Please enter the argument'
    exit 0
fi

fullfilename=$@
filename=$(basename "$fullfilename")
fname="${filename%.*}"
extension="${filename##*.}"
date1=$(date +"%Y-%m-%d")
cp $filename "$fname"_"$date1"."$extension"
echo "Copy of the given file with date as prefix is $fname"_"$date1"."$extension"
