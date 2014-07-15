from swampy.TurtleWorld import*
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polygon(t, n, length):
    angle = 360.0/n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int( circumference / 3 ) + 1
    length = circumference / n
    polygon(t,n,length)

circle(bob, 100)
wait_for_user()
