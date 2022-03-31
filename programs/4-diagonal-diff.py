'''
Given a square matrix, calculate the absolute difference between the sums 
of its diagonals.
For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9  

The left-to-right diagonal = 1+5+9=15. The right to left diagonal = 
3+5+9=17. Their absolute difference is |15-17|=2.

Function description
Complete the diagonalDifference function below
diagonalDifference takes the following parameter:
 - int arr[m][n]: an array of integers

Return
 - int: the absolute diagonal difference

Input Format
The first line contains a single integer, n, the number of rows and columns 
in the square matrix arr.
Each of the next n lines describes a row, arr[i], and consists of n 
space-separated integers arr[i][j].

Constraints
-100 <= arr[i][j] <= 100

Output format
Return the absolute difference between the sums of the matrix's diagonals 
as a single integer.

Sample input
3
11 2 4
4 5 6
10 8 -12

Output
15

Explaination
the primary diagonal is
11
  5
   -12
sum across the primary diagonal 11+5-12=4
Secondary diagonal is
   4
  5
10
sum across the secondary diagonal 4+5+10=19
Difference |4-19|=15
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    difference = 0
    num0 = 0; num1=0
    for i in range (0, len(arr)):
        # j = i
        num0 += arr[i][i]
        num1 += arr[i][len(arr) - 1 - i]
    # for i in reversed(range(0, len(arr))):
    #     for j in reversed(range(0, len(arr))):
    #         if(i == j):
    #         #   num1 += arr[i][i]
    #             pass
    return abs(num0 - num1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
