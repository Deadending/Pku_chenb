'''
@Func: Determine which day of the year the input date is
@Author：jlzhong0709@gmail.com
@Date:12/04/2023
'''
import datetime


dtstr = input("Enter the datetime:")
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
another_dtstr = dtstr[:4] + '0101'
another_dt = datetime.datetime.strptime(another_dtstr, "%Y%m%d")
print(int((dt - another_dt).days) + 1)