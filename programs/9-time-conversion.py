'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s='12:01:00PM'
Return '12:01:00'.

s='12:01:00AM'
Return '00:01:00'.

Function Description
Complete the timeConversion function below. It should return a new string 
representing the input time in 24 hour format.
timeConversion has the following parameter(s):
 - string s: a time in  hour format

Returns
 - string: the time in  hour format

Input Format
A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Constraints
All input times are valid.

Sample inputs
07:05:45PM

Output
19:05:45
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
# 07:45:00PM
def timeConversion(s):
    conv = ''
    hour = int(s[0:2])
    pos = s[-2:]
    
    if hour == 12 and pos == 'AM':
        conv = '00' + s[2:-2]
    elif hour == 12 and pos == 'PM':
        conv = s[:-2]
    elif pos == 'PM':
        hour += 12
        conv = f'{hour}{s[2:-2]}'
    elif hour < 10:
        conv = f'0{hour}{s[2:-2]}'
    print(hour)
    return conv
    
    # if s[:2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
