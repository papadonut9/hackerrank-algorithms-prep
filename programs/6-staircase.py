'''
Staircase detail

This is a staircase of size n=4:
   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and 
spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.

Function Description
Complete the staircase function below.
staircase has the following parameter(s):
 - int n: an integer

Print
Print a staircase as described above.

Input Format
A single integer, , denoting the size of the staircase.

Constraints
0 < n <= 100

Output Format
Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces in it.

Sample Input
6

Sample output
     #
    ##
   ###
  ####
 #####
######

Explaination
The staircase is right-aligned, composed of # symbols and spaces, and has a 
height and width of n=6
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(0, n):
        # print(' '*(n-1-i))
        # print('#'*(i+1))
        for j in range(0, n):
            if i+j >= n-1:
                print('#', end='')
            else:
                print(' ', end='')
        print('\r')

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
