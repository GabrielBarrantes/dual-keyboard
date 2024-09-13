#!/bin/bash

# $evtest # to find where is the keyboard
EV_NUMBER=6
source env/bin/activate
sudo python3 main.py $EV_NUMBER
