'''
双色球是由中国福利彩票发行管理中心发售的乐透型彩票，每注投注号码由`6`个红色球和`1`个蓝色球组成。
红色球号码从`1`到`33`中选择，蓝色球号码从`1`到`16`中选择。每注需要选择`6`个红色球号码和`1`个蓝色球号码
'''
import random
#
# #随机一注彩票
# ticket = [random.randint(1,34) for _ in range(6)]+[random.randint(1,17)]
# print(ticket)



n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_balls = random.sample(red_balls, 6)
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    # 从蓝色球列表中随机抽出1个蓝色球
    blue_ball = random.choice(blue_balls)
    # 输出选中的蓝色球
    print(f'\033[034m{blue_ball:0>2d}\033[0m')
'''
**说明**：上面代码中`print(f'\033[0m...\033[0m')`是为了控制输出内容的颜色，红色球输出成红色，蓝色球输出成蓝色。
其中省略号代表我们要输出的内容，`\033[0m`是一个控制码，表示关闭所有属性，也就是说之前的控制码将会失效，你也可以将其简
单的理解为一个定界符，`m`前面的`0`表示控制台的显示方式为默认值，`0`可以省略，`1`表示高亮，`5`表示闪烁，`7`表示反显等。
在`0`和`m`的中间，我们可以写上代表颜色的数字，比如`30`代表黑色，`31`代表红色，`32`代表绿色，`33`代表黄色，`34`代表蓝色等。
'''