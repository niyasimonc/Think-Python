from swampy.TurtleWorld import *
import math


def polygon(t,n,l):
  for i in range(n):
    fd(t,l)
    lt(t,360.0/n)
  
def circle(t,r):
  perimeter=2*math.pi*r
  n=50
  length=perimeter/n
  polygon(t,n,length)


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
  n=8
  length=50
  polygon(bob,n,length)
  pu(bob)
  fd(bob,200)
  pd(bob)
  r=50
  circle(bob,r)
  pu(bob)
  fd(bob,200)
  pd(bob)
  r=100
  angle=67
  arc(bob,r,angle)
  die(bob)
  wait_for_user()


if __name__=='__main__':
  main()
