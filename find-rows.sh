#!/bin/bash

for file in ./data/set/*
do
wc -l $file | awk ' BEGIN {OFS = ","} {print $2,$1}' >> ./rows.csv
done