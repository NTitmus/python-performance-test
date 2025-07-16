#!/bin/bash

echo "filename,time(s),memory(MB)" >> output.txt

for file in ./data/set/*
do
python performance-script.py $file >> output.csv
done