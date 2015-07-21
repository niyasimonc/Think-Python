class point(object):
  """attri:x,y"""
  def __init__(self,x=0,y=0):
   self.x=x
   self.y=y

  def __str__(self):
    return '(%d,%d)'%(self.x,self.y)

  def __add__(self,other):
    if type(other)==point:
      result=point()
      result.x=self.x+other.x
      result.y=self.y+other.y
      return result
    else:
      self.add_tuple(other)
  
  def add_tuple(self,x):
      result=point()
      result.x=self.x+x[0]
      result.y=self.y+x[1]
      print result
      return

  
  def __radd__(self,other):
     return self.__add__(other)


def main():
  blank=point(6,7)
  print blank
  nex=point(1,2)
  print nex
  print blank+nex
  print "first"
  ((2,2)+blank)
  print "second"
  (blank+(2,2))
  

if __name__=='__main__':
   main()
