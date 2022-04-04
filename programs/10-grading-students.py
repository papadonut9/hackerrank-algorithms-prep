'''
HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's  
according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, 
round grade up to the next multiple of 5.
If the value of  is less than , no rounding occurs as the result will still be 
a failing grade.

Examples
 -  grade 84 = round to  (85 - 84 is less than 3)
 -  grade 29 = do not round (result is less than 40)
 -  grade 57 = do not round (60 - 57 is 3 or higher)
Given the initial value of  for each of Sam's n students, write code to automate the rounding process.

Function Description
Complete the function gradingStudents.

gradingStudents has the following parameter(s):
 - int grades[n]: the grades before rounding

Returns
 - int[n]: the grades after rounding as appropriate

Input Format
The first line contains a single integer, n, the number of students.
Each line i of the n subsequent lines contains a single integer, grades[i].

Constraints
1 <= n <= 60
0 <= grades[i] <= 100

Sample Input 0
4
73
67
38
33

Sample output
75
67
40
33

Explaination
Student 1 received 73 and next multiple from 73 is 75 and difference is 2 
which is less than 3, so the grade is rounded off to 5

Student 2 received 67 and next multiple from 67 is 70 and the difference is 3
which is not less than 3, so no rounding occurs

Student 3 received 38 and next multiple from 38 is 40 and the difference is 2
which is less than 3, so the grade is rounded off to 40

Student 4 received 33, which is less than 38. So no rounding off occurs
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    new_grades = []
    diff = 0
    for grade in grades:
        if grade >= 38:     # If grade is less than 38, no rounding occurs
            diff = grade % 5

            if diff >= 3:   # If difference < 3 then round off to next multiple of 5
                grade += 5-diff
        new_grades.append(grade)
    return new_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
