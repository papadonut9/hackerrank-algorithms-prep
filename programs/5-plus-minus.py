'''
Given an array of integers, calculate the ratios of its elements that are 
positive, negative, and zero. Print the decimal value of each fraction on a 
new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are 
scaled to six decimal places, though answers with absolute error of up to 
10**-4 are acceptable.

Example
arr=[1, 1, 0, -1, -1]
There are n=5 elements, two positive, two negative and one zero. Their 
ratios are 2/5=0.400000, 2/5=0.400000 and 1/5=0.200000. Results are printed 
as:
0.400000
0.400000
0.200000

Function Description
Complete the plusMinus function below.
plusMinus has the following parameter(s):
 - int arr[n]: an array of integers

Print
Print the ratios of positive, negative and zero values in the array. Each 
value should be printed on a separate line with 6 digits after the decimal. 
The function should not return a value.

Input Format
The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n].

Constraints
0<=n <= 100
-100 <= arr[i] <= 100

Output format
Print the following 3 lines, each to 6 decimals:
 - proportion of positive values
 - proportion of negative values
 - proportion of zeros

Sample input
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample output
0.500000
0.333333
0.166667
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0 
    zero = 0
    den = len(arr)
    for i in range(0, len(arr)):
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positive += 1
        elif arr[i] == 0: 
            zero += 1
        # print(f'{i} \n{positive} {negative} {zero}')
    print(f'{round(positive/den,6)}\n{round(negative/den, 6)}\n{round(zero/den, 6)}')
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
