import csv
import random
import string
import sys

# 1000000 and 52 == roughly 1GB (WARNING TAKES a while, 30s+)
#rows = 100
columns = 10
string_cols = 10
text_cols = 5

def generate_random_row(i):
    a = []
    l = [i]
    for j in range(columns):
        l.append(random.random())
    for k in range(string_cols):
        N = random.choice(range(20))
        l.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=N)))
    for m in range(text_cols):
        N = random.choice(range(200, 500))
        l.append(''.join(random.choices(string.ascii_letters + string.digits + " ", k=N)))
    a.append(l)
    return a

def generate_file(name, num_rows):
    filename = './data/set/' + name
    f = open(filename, 'w')
    w = csv.writer(f, lineterminator='\n')
    for i in range(num_rows):
        w.writerows(generate_random_row(i))
    f.close()

def generate_batch_files(file_counter, files_in_batch, row_range):
    for s in range(files_in_batch):
        file_counter += 1
        filename = "data" + str(file_counter) + ".csv"
        (range_start, range_end) = row_range
        num_rows = random.randint(range_start,range_end)
        generate_file(filename, num_rows)
    return file_counter

if __name__ == '__main__':
    file_counter = 0
    files_in_batch = 30
    #0-100 rows
    file_counter = generate_batch_files(file_counter, files_in_batch, (1, 100))

    #100-1000 rows
    file_counter = generate_batch_files(file_counter, files_in_batch, (101, 1000))

    #1000-10000 rows
    file_counter = generate_batch_files(file_counter, files_in_batch, (1001, 10000))

    #10000-100000 rows
    file_counter = generate_batch_files(file_counter, files_in_batch, (10001, 100000))
    