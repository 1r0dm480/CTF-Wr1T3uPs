#! /bin/bash

cat 01_forense.txt | awk '/Body:/{getline;print}' | base64 -d | awk '/o]PCm/{getline;print}' | base64 -d > flag
