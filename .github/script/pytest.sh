#!/bin/sh

if ! [ -x "$(command -v pytest)" ]; then
  echo 'Error: pytest is not installed.' >&2
  echo 'Installing pytest'
  pip install pytest
  echo 'pytest installed.'
fi


pytest