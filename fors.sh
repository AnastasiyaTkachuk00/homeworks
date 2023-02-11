#!/bin/bash
INDEX=0
while [ $INDEX -lt 11 ]
do
  REMAINDER=$(( $INDEX % 2 ))
  if [ $REMAINDER -eq 0 ]
  then
    echo $INDEX
  fi
  INDEX=$(($INDEX+1))
Done
