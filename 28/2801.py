'''
@Func: calculate the sum of factorials of n numbers
@Author：jlzhong0709@gmail.com
@Date:20/04/2023
'''


import math


N = int(input("输入正整数N："))
sum = 0
for i in range(1,N+1):
    sum += math.factorial(i)
print("The sum of factorials from 1 to %d is %d." %(N,sum))