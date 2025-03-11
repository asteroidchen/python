'''
CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇
两粒骰子获得点数进行游戏。简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；玩家
第一次如果摇出 2 点、3 点或 12 点，庄家胜；玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果
玩家摇出了 7 点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜
负。为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，每局游戏开始之前，玩家先下注，
如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，玩家就会输掉自己下注的金额。游戏结束的条件
是玩家破产（输光所有的赌注）。
'''

import random
from math import trunc

print('这是一个骰子游戏，你有1000的资本，不要输完了哦！！！')
money = 1000
print('那么开始这局游戏吧，请下注：')
while money > 0:
    bett = int(input())
    point = random.randint(1,7) + random.randint(1,7)
    print(point)
    if point == 7 or point == 11:
        print('玩家胜，恭喜你，这局你赢了，继续下注吧0.0')
        money += bett
        print(money)
        continue
    elif point == 2 or point == 3 or point ==12:
        print('庄家胜，运气不好哦，你输了！！！继续下注吧')
        money -= bett
        print(money)
        continue
    else:
        while True:
            second_point = random.randint(1,7) + random.randint(1,7)
            print(second_point)
            if second_point == 7:
                print('这局是庄家胜了，加油哦！')
                money -= bett
                print(money)
                break
            elif point == second_point:
                print('玩家胜，你赢了！')
                money += bett
                print(money)
                break
            else:
                print('游戏继续，重新摇骰子')
                print(money)
                continue


print(money)
print('你的筹码输完了，游戏结束了！！！')