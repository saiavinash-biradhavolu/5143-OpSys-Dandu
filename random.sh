#!/bin/bash

file_name=/usr/share/dict/words

num_words=`wc -w < $file_name`

rand_word=`expr "$RANDOM" % $num_words + 1`

cat $file_name | tr "\n" " " | awk -v randword=$rand_word '{print $randword}'
