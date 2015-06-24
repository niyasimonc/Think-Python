rom swampy.TurtleWorld import *
 
def arc(t,r,a):
  for i in range(15):
    fd(t,r)
    lt(t,a)


def main():
  world=TurtleWorld()
  bob=Turtle()
  radius=12.5
  angle=360
  angl=370-360
  arc(bob,radius,angl)
  wait_for_user()
  return




if __name__=='__main__':
  main()
