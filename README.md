# Scripts
- generate-data.py - This generates multiple .csv files in the directory data/set (in the .gitignore).  The csv files consist of columns of different types (int, float, string) populated with randomly generated data.  In the 1st instance, it will generate 30 csvs with 1-100 rows, 30 with 101-1000 rows, 30 with 1001-10000 rows and 30 with 10001-100000 rows.  The script can be altered to change different parameters (e.g. number, type and size of columns; number of files in each category for number of rows)
- performance-script.py - This script takes 1 argument - the filename.  It runs process (in the 1st instance it is pd.read_csv) on the file given as an argument.
- loop-python.sh - this bash script calls the performance-script.py and runs it on every file in the data/set directory.  It outputs the results as output.csv (appends to this file).
- disk-space.sh - this bash script generates file-size.csv with the filename and the file size (as determined by linux ls -l command).

# Instructions
- clone this repo
- create a directory called data in the root of the repo.  Create a subdirectory of data called set.
- in the root of the directory run generate-data.py:
> python generate-data.py
- in the root of the directory run loop-python.sh:
> ./loop-python.sh
- in the root of the directory run disk-space.sh:
> ./disk-space.sh

Now there should be 2 .csv's outputted: file-size.csv and output.csv.  These can be analyzed.

If you need to repeat a run of .loop-python.sh, then please delete output.csv first (because lines are appended rather than the file being generated anew).  
