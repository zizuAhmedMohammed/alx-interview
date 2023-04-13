#!/usr/bin/env python3

import sys
import signal

"""Initialize variables"""
total_size = 0
status_code_dict = {}

def print_stats():
    """Define function to print statistics"""
    global total_size
    global status_code_dict
    
    """Print total file size"""
    print(f'Total file size: {total_size}')
    
    """Sort and print number of lines by status code"""
    sorted_status_codes = sorted(status_code_dict.keys())
    for status_code in sorted_status_codes:
        if status_code in status_code_dict:
            print(f'{status_code}: {status_code_dict[status_code]}')


def process_line(line):
    """Define function to process a line of input"""
    global total_size
    global status_code_dict
    
    line = line.strip()
    
    try:
        _, _, request, status_code_str, file_size_str, _ = line.split(' ')
        if 'GET /projects/260 HTTP/1.1' in request:
            """If the request contains the specified string, update metrics"""
            status_code = int(status_code_str)
            file_size = int(file_size_str)
            total_size += file_size
            
            if status_code not in status_code_dict:
                status_code_dict[status_code] = 1
            else:
                status_code_dict[status_code] += 1
    except ValueError:
        """If the line doesn't match the input format, skip it"""
        pass

def signal_handler(signal, frame):
    """Define a signal handler to print statistics when interrupted"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_num = 0

for line in sys.stdin:
    process_line(line)
    
    line_num += 1
    if line_num % 10 == 0:
        """Print statistics every 10 lines"""
        print_stats()
