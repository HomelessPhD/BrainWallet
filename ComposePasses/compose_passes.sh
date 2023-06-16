#!/bin/bash

for day in $(seq -f "%02g" 1 31); do
    for month in $(seq -f "%02g" 1 12); do
        for year in `seq 1980 1 2017`; do
            echo "$day-$month-$year" >> pass_list.txt
            echo "$month-$day-$year" >> pass_list.txt
            echo "$year-$month-$day" >> pass_list.txt
            
        done
    done
done
