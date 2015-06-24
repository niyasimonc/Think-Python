from swampy.TurtleWorld import *
 
def circle(t,r):
  for i in range(40):
    fd(t,10)
    lt(t,10)


def main():
  world=TurtleWorld()
  bob=Turtle()
  radius=10
  circle(bob,radius)
  wait_for_user()
  return




if __name__=='__main__':
  main()
