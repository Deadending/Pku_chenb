'''
@Func: guess the number
@Author：jlzhong0709@gmail.com
@Date:12/04/2023
'''
import random


secret = random.randint(1,100)
guess_num = int(input("输入一共可以猜的次数："))
print("猜数游戏！我想了一个1~100之间的整数，你最多可以猜%d次，看看能猜出来吗？" %(guess_num))
tries = 1
while tries <= guess_num:
    guess = int(input("1~100之间的整数，第%d次猜，请输入："%(tries)))
    if guess == secret:
        print("恭喜猜对了！你只猜了%d次！\n就是这个：%d！" %(tries,secret))
        break
    elif guess > secret:
        print("不好意思，你的数大了一点儿，你还有%d次机会！" %(guess_num - tries))
    else:
        print("不好意思，你的数小了一点儿，你还有%d次机会！" %(guess_num - tries))
    tries += 1
else:
    print("Game Over！You Loss!")