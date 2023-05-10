'''
@Func: Given y and m, calculate the number of days in y year m month
@Author：jlzhong0709@gmail.com
@Date:20/04/2023
'''


y = int(input("输入年份："))
m = int(input("输入月份："))
days_of_commom_year = {1:31, 2:28, 3:31,4:30, 5:31, 6:30,
                       7:31, 8:31, 9:30,10:31, 11:30, 12:31}
days_of_leap_year   = {1:31, 2:29, 3:31,4:30, 5:31, 6:30,
                       7:31, 8:31, 9:30,10:31, 11:30, 12:31}
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
    print("%d年%d月有%d天." %(y,m,days_of_leap_year[m]))
else:
    print("%d年%d月有%d天." %(y,m,days_of_commom_year[m]))