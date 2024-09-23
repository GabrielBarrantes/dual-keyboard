#!/bin/bash

# $evtest # to find where is the keyboard
EV_NUMBER=3
source env/bin/activate
PYTHON3_VENV_PATH=$(which python3)
sudo $PYTHON3_VENV_PATH main.py $EV_NUMBER
