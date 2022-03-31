# Complete the function solveMeFirst to compute the sum of two integers.
'''
Example:
a=7 b=3
Return 10

Function Description:
Complete the function solveMeFirst to compute the sum of two integers.
Solvemefirst has the following parameters
 - int a: the first value
 - int b: the second value

Returns:
 - int: the sum of a and b

Constraints:
1 <= a, b <= 10000

Sample input:
a = 5   b = 2

Output:
7

Explaination: 
5 + 2 = 7
'''



def solveMeFirst(a,b):
	return a+b

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
