'''
@Func: 给定一个英文数字字符串，打印相应阿拉伯数字字符串
@Author：jlzhong0709@gmail.com
@Date:20/04/2023
'''


def convert_number(string):
    numbers = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
               'six':'6','seven':'7','eight':'8','nine':'9','ten':'10'}
    result = ''
    for num in string.split('-'):
        result += numbers[num]
    return result

string = input("输入字符串：")
result = convert_number(string)
print(result)