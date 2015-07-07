import time

def make1():
  l=[]
  f=open("words.txt",'r')
  for line in f:
   word=line.strip()
   l.append(word)
  return l

def make2():
  l=[]
  f=open("words.txt",'r')
  for line in f: 
    word=line.strip()
    l=l+[word]
  return l
  


def main():
  s1=time.time()
  l1=make1()
  f1=time.time()
  print "Time for list creation using append is ",f1-s1
  s2=time.time()
  l2=make2()
  f2=time.time()
  print "Time for creation of list using '+' is ",f2-s2


if __name__=='__main__':
  main()
