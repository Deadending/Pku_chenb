'''
@Func:返回两个字符串字符集合的并集
@Author：jlzhong0709@gmail.com
@Date:10/05/2023
'''

def string_union(str1,str2):
    set1 = set(str1)
    set2 = set(str2)
    return set1.union(set2)


str1 = input("输入第一个字符串：")
str2 = input("输入第二个字符串：")
result = string_union(str1,str2)
print(result)