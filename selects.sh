#!/bin/bash

PS3 "Do you want to install Python?"
echo
select variant in "Yes"     
do
    echo "You choose to install Python" &&break
select variant in "No"
do
    echo "Go away close the door" &&break 
done
    
exit 0
