'''
@Func: 水仙花数判定
@Author：jlzhong0709@gmail.com
@Date:10/05/2023
'''


def Is_Daffodilnumber(n):
    length = len(str(n))    #获取数字位数
    temp_num = n
    sum = 0
    while temp_num > 0:
        num = temp_num % 10
        sum += num ** length
        temp_num = temp_num // 10
    if sum == n:
        return True
    else:
        return False
    

def num_range(max):
    daffodi = []
    for i in range(10,max):
        if(Is_Daffodilnumber(i)):
            daffodi.append(i)
    return daffodi
            
        

max = int(input("输入一个任意范围内的整数："))
print(num_range(max))
