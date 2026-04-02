#!/bin/bash

# activate virtual environment
source venv/Scripts/activate

# run tests
pytest

# check result
if [ $? -eq 0 ]; then
  echo "Tests passed"
  exit 0
else
  echo "Tests failed"
  exit 1
fi