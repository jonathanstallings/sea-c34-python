#!/bin/sh

flake8 *.py | tee flake8.log
pep8 *.py | tee pep8.log

echo "1" | ./mailroom.py | tee mailroom-1.log

