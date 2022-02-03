#!/bin/sh

export FLASK_APP=./cashman/index.py
#Defines the main script to be executed

source $(pipenv --venv)/bin/activate
#Activates the virtual environment

flask run -h 0.0.0.0
#Run flask
