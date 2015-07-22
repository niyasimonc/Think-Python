class time(object):
  """ attri:hour,minute,second"""
  def __init__(self,hour=0,minute=0,second=0):
      self.hour=hour
      self.minute=minute
      self.second=second

  def __str__(self):
      return '%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)
  
  def __cmp__(self,other):
    t1=self.hour,self.minute,self.second
    t2=other.hour,other.minute,other.second
    return cmp(t1,t2)




def main():
  noon=time(12)
  print noon
  morning=time(4)
  print morning
  t=noon>morning
  if t>0:
    print noon
  else:
    print morning







if __name__=='__main__':
  main()
