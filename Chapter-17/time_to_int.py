class Time(object):
  """attri:hour,minute,second"""
  def print_time(self):
    print '%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)
  def time_to_int(self):
    minutes=self.hour*60+self.minute
    second=minutes*60+self.second
    return second



def main():
  time=Time()
  time.hour=1
  time.minute=2
  time.second=2
  time.print_time()
  print time.time_to_int()




if __name__=='__main__':
  main()
