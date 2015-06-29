from swampy.TurtleWorld import *
import math


def move(t, length):
  pu(t)
  fd(t, length)
  pd(t)

def polygon(t,n,l):
  for i in range(n):
    fd(t,l)
    lt(t,360.0/n)
  
def circle(t,r):
  perimeter=2*math.pi*r
  n=50
  length=perimeter/n
  polygon(t,n,length)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)



def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)

def arc(t,r,a):
  arclength=2*math.pi*r*a/360.0
  n=int(arclength/3)+1
  steplength=arclength/n
  stepangle=float(a)/n
  for i in range(n):
    fd(t,steplength)
    lt(t,stepangle)



def main():	
  world=TurtleWorld()
  bob=Turtle()
  bob.delay=0.001
  flower(bob, 7, 40.0, 60.0)
  move(bob, 200)
  flower(bob, 10, 90.0, 80.0)
  move(bob, 200)
  flower(bob, 20, 140.0, 20.0)
  die(bob)
  wait_for_user()


if __name__=='__main__':
  main()
