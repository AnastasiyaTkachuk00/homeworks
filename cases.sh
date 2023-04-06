#!/bin/bash

echo "enter"
read c

if [[ $c == [A-Z] ]];
then
    echo "upper"
elif [[ $c == [a-z] ]];
then
    echo "lower"
else 
    echo "Digit or symbols!"
fi
