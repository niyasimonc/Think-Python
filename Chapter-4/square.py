from swampy.TurtleWorld import *

def square(t):
  for i in range(4):
    fd(t,50)
    lt(t)
  return

def main():
  world=TurtleWorld()
  bob=Turtle()
  square(bob)
  wait_for_user()
  return

if __name__=="__main__":
  main()
