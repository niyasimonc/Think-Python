from swampy.TurtleWorld import *
 
def polygon(t,length,n):
  for i in range(n):
    fd(t,length)
    lt(t,360/n)


def main():
  world=TurtleWorld()
  bob=Turtle()
  leng=50
  n=12
  polygon(bob,leng,n)
  wait_for_user()
  return




if __name__=='__main__':
  main()
