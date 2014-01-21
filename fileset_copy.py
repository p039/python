#!python
import csv
import re
import os

from tempfile import mkstemp
from shutil import move
from os import remove, close
import shutil

CSVFILE = "c:\\file.csv"
CSVSOURCE = csv.reader(open(CSVFILE, "rU"),  delimiter=';')

SRC = "c:\\A"
DST = "c:\\B"

def get_prefix(csv_read):
    try:
        L = []

        for row in csv_read:
            tc_id = row[0].lstrip("0")

            if re.match('[0-9]', tc_id):
                L.append(tc_id)
        return sorted(L)
    except OSError, e:
            if e.errno != errno.ENOENT:
                raise


def copy_files(prefix, path):
    try:
        file_to_copy = 'contact_' + prefix + '.txt'

        for root, dirs, files in os.walk(path):
            if file_to_copy in files:
                file_path = os.path.join(root, file_to_copy)

                shutil.copy(file_path, DST)
    except OSError, e:
        if e.errno != errno.ENOENT:
            raise

if __name__ == '__main__':

    prefix_set = get_prefix(CSVSOURCE)

    for i in prefix_set:
        copy_files(i, SRC)


'''
file.csv ->
1
2
3

folder A -> contact_1.txt, contact_2.txt, contact_3.txt
folder B -> empty

Result: files from A copied into B
'''