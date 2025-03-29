import random
from turtledemo.sorting_animate import enable_keys

num = random.randint(1, 100)
print('我们来玩一个猜数字的游戏吧，我设置一个数字你来猜，请输入你猜的数字：')


for i in range(10):
    guess = int(input())
    if guess == num:
        print('猜对了，你真棒！！！')
        break
    elif guess > num:
        print('你猜的数字大了，重新猜！！！')
        continue
    elif guess < num:
        print('你猜的数字小了，重新猜！！！')
        continue

print(num)