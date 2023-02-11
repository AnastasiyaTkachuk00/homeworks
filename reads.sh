#!/bin/bash

if (($1 > 15 && < 45 ))
then
echo "A number greater than 15 and less than 45"
elif (($1 < -1 && $1=45))
echo "number less than -1 or equal to 45"
fi
