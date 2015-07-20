class Time(object):
  """Attributes:hour,minute,second)"""

def print_time(time):
  print '%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second)


def make_time(time,h,m,s):
  time.hour=h
  time.minute=m
  time.second=s
  return time




def valid(time):
  if time.hour>=12 or time.minute>=60 or time.second>=60:
    return False
  elif time.hour<0 or time.minute<0 or time.second<0:
     return False
  return True

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds




def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time





  
def mul_time(time,n):
   if valid(time):
       time_in_int=time_to_int(time)
       new=time_in_int*n
       time=int_to_time(new)
       return time



 
def main():
  time=Time()
  time=make_time(time,1,39,0)
  print_time(time)
  time=mul_time(time,2)
  print_time(time)


if __name__=='__main__':
  main()
