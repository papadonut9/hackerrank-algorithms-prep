'''
Given an array of integers, find the sum of its elements.
For example, if the array arr = [1, 2, 3],  1 + 2 + 3 = 6, so return 6.

For Example:
Complete the simpleArraySum function in the editor below. It must return
the sum of the array elements as an integer.
simpleArraySum has the following parameter(s):
 - ar: an array of integers

Input Format:
The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints:
0 <= n, arr[i] <= 1000

Output Format:
Print the sum of the array's elements as a single integer.

Sample Input:
6
1 2 3 4 5 6

Sample Output:
21

Explaination:
We print the sum of array's elements:
1+2+3+4+5+6=21
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


def simpleArraySum(ar):
    sum = 0
    for i in range(0, len(ar)):
        sum += ar[i]
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
