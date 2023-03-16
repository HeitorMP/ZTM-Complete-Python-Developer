#!/usr/bin/env python3
import sys
import PyPDF2
from os import path


def warning_message(msg_code, file=None):
    if msg_code == 0:
        print('\nUsage: python3 -o output_name -f file1.pdf file2.pdf...\n ')
        exit(1)
    elif msg_code == 1:
        print(f'{file} is not a valid pdf file!')
    elif msg_code == 2:
        print(f'{file} not found!')


def check_params(args):
    if len(args) < 6:
        warning_message(0)

    if args.count('-o') != 1 or args.count('-f') != 1:
        warning_message(0)

    if args.index('-o') != 1 and args.index('-f') != 3:
        warning_message(0)

    file_list = args[4:]
    for file in file_list:
        if not file.endswith('.pdf'):
            warning_message(1, file)


args = sys.argv
check_params(args)
# add .pdf if new name not ends with .pdf
if not args[2].endswith('.pdf'):
    output_name = args[2] + '.pdf'
input_list = args[4:]


merger = PyPDF2.PdfFileMerger()

for file in input_list:
    if path.isfile(file):
        merger.append(file)
    else:
        warning_message(2, file)

merger.write(output_name)
merger.close()
