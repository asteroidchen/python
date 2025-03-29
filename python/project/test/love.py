import turtle

# 初始化设置
turtle.speed(5)
turtle.bgcolor('black')
turtle.color('red')
turtle.begin_fill()

# 绘制心形曲线
turtle.left(140)
turtle.forward(180)
turtle.circle(-90, 200)  # 左半圆弧

# 画右侧曲线
turtle.left(120)
turtle.circle(-90, 200)
turtle.forward(180)

turtle.end_fill()
turtle.hideturtle()
turtle.done()