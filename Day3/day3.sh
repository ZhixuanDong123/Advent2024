#!/bin/bash

echo $(( $(grep -o '[m][u][l][(][0-9]*[,][0-9]*[)]' input.txt | sed 's/mul//g' | sed -z 's/\n/+/g' | sed 's/$/0/g' | sed 's/,/*/g') ))

