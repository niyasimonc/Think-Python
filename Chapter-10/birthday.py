import random

def has_duplicate(l):
  length=len(l)
  i=0
  new=sorted(l)
  while i<length-1:
    if new[i]==new[i+1]:
      return False
    else:
      i+=1
  return True


def random_birthday(n):
  l=[]
  for i in range(n):
    l.append(random.randint(1,365))
  return l

 

def birthday(ns,nt):
  c=0
  for i in range(nt) :
     t=random_birthday(ns)
     if has_duplicate(t):
       c=c+1    
  return c
  
def main():
  num_students=23
  num_test=1000
  count=birthday(num_students,num_test)
  print "The count is",count


if __name__=='__main__':
  main()
