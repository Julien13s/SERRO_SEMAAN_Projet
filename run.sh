#!/bin/bash


if [[ ! -d ".v" ]]
then
	pip3 install virtualenv --force-reinstall
	python3 -m venv .v
	pip freeze > requirements.txt
	pip install -r requirements.txt
	echo "virtualenv has been installed"
fi

if [[ -d ".v" ]]
then
	source .v/bin/activate
	echo "virtualenv has been activated"
fi

chmod +x main.py
./main.py

