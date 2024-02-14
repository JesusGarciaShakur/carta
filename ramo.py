from turtle import *

bgcolor('black')
speed(0)

color=['yellow']

for i in range(150):
    pencolor(color[i%1])
    circle(190-i/2,90)
    left(90)
    circle(190-i/3,90)
    left(60)

done()