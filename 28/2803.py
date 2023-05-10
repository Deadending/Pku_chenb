'''
@Func: 给定字符串s和数字n,打印把字符串s向右移动n位的新字符串
@Author：jlzhong0709@gmail.com
@Date:20/04/2023
'''


def right_rotate_string(s,n):
    # 计算字符串长度
    length = len(s)
    # 计算实际需要移动的位数
    n = n % length
    # 把字符串分成两部分并交换位置
    s = s[length - n:] + s[:length - n]

    return s


s = input("输入字符串：")
n = int(input("输入移动的位数："))
new_string = right_rotate_string(s,n)
print(new_string)