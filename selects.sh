#!/bin/bash

echo "Do you want to install Python?"
read c

if [[ $c == "Yes" ]];
then
    echo "You choose to install Python"
elif [[ $c == "No" ]];
then
    echo "Go away close the door"
else 
    echo "Try again"
fi
