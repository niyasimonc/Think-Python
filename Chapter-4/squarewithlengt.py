rom swampy.TurtleWorld import *
 
def squre(t,length):
  for i in range(4):
    fd(t,length)
    lt(t)


def main():
  world=TurtleWorld()
  bob=Turtle()
  leng=100
  squre(bob,leng)
  wait_for_user()
  return




if __name__=='__main__':
  main()
