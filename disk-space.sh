#!/bin/bash

ls -l data/set | awk ' BEGIN {OFS = ","} {print $9,$5}' > ./file-size.csv