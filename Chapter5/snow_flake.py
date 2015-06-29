from swampy.TurtleWorld import *

def koch(t,x):
  if x >3:  
    koch(t,x/3)
    lt(t,60)
    koch(t,x/3)
    rt(t,120)
    koch(t,x/3)
    lt(t,60)
    koch(t,x/3)
  else:
    fd(t,x)
    return
 
def snowflake(t,l):
  for i in range(3):
     koch(t,l)
     rt(t,120)
  


def main():
  world=TurtleWorld()
  bob=Turtle()
  bob.delay=0.001
  l=raw_input("Enter the length ")
  length=int(l)
  snowflake(bob,length)
  die(bob)
  wait_for_user()




if __name__=='__main__':
  main()
