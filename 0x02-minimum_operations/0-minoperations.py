#!/usr/bin/env python3
""" Python minimum operations challenge"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n == 1:
        return 0
    operations = 0
    current = 1
    clipboard = 0
    
    while current < n:
        if (n - current) % current == 0 and clipboard == current // 2:
            clipboard = current
            current += clipboard
            operations += 2
        else:
            current += clipboard
            operations += 1
    
    return operations
