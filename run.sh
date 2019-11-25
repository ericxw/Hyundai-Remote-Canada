#!/bin/bash

re='^[0-9]+$'

if ! [[ $1 =~ $re ]];
then
  echo "Please specify port."
  echo "Example: ./run.sh 8080"
  exit 1
fi

docker run --name hyundai-remote-canada -d -p $1:5000 hyundai-remote-canada
