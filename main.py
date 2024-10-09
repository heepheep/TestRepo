import turtle
import random

#Первый фрактал

# x=0
# for i in range(100):
#     for i in range(4):
#         turtle.forward(100+x)
#         turtle.left(90)
#     x += 5
#     turtle.left(10)

#Второй факториал

x = 1
turtle.speed(1000)
for i in range(100):
   for i in range(4):
       turtle.forward(1+(1*x))
       turtle.left(90)
       turtle.forward(1+(1*x))
       turtle.right(90)
       turtle.forward(1+(1*x))
       turtle.right(90)
       turtle.forward(1+(1*x))
   turtle.left(89.6)
   turtle.forward(2+(1*x))
   x += 1

#Третий фрактал

# turtle.screensize(1500, 1500)
# turtle.bgcolor("black")
# turtle.speed(100)
# colors = ['#000','#111','#222','#333','#444','#555','#666','#777','#888','#999','#aaa','#bbb','#ccc','#ddd','#eee','#fff']
# x = 1
# colorNum = 0
# for i in range(150):
#     turtle.color(colors[colorNum])
#     turtle.circle(10+x)
#     turtle.right(15)
#     turtle.forward(5)
#     x += 1
#     colorNum += 1
#     if colorNum == len(colors):
#         colorNum = 0