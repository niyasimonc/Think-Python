from swampy.TurtleWorld import *
import math

def drawpie(t,n,size): 
  pd(t)
  for i  in range(n):
    triangle(t,size,n)
    rt(t,270.0-(180.0/n))
    fd(t,size)
    lt(t,360.0/n)
  pu(t)
  fd(t,4*size)
  return



def triangle(t,size,n):
      fd(t,size)
      a1=(((n*180.0-180.0)/n)-90.0)+(360.0/n)
      lt(t,a1)
      fd(t,size/(2*math.sin(math.pi/n)))
      lt(t,180.0-(2.0*180.0/n))
      fd(t,size/(2.0*math.sin(math.pi/n)))
      return




def main():
  world=TurtleWorld()
  bob=Turtle()
  size=50
  drawpie(bob,5,size)
  drawpie(bob,6,size)
  drawpie(bob,7,size)
  drawpie(bob,8,size)
  die(bob)
  wait_for_user() 
  return



if __name__=='__main__':
  main()
