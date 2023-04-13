#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics."""


import sys

cache_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
              '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
count = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])
            if status_code in cache_dict.keys():
                cache_dict[status_code] += 1
            total_file_size += file_size
            count += 1
        
        if count == 10:
            count = 0
            print('Total File size: {}'.format(total_file_size))
            for key, value in sorted(cache_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as e:
    pass

finally:
    print('Total File size: {}'.format(total_file_size))
    for key, value in sorted(cache_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
