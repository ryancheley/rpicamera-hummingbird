#!/bin/bash
(array=($(ls /home/pi/Documents/python_projects/*.jpg)); for index in ${!array[@]}; do if [ "$index" -eq 0 ]; then echo -n " -add ${array[index]}"; else echo -n " -cat ${array[index]}"; fi; done;)
