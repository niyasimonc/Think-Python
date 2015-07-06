def palindrom(n,s,l):
  s1=str(n)
  s2=s1[s:s+l]
  if s2==s2[::-1]:
    return True
  else:
    return False
  






def check(num):
  a=palindrom(num,2,4)
  b=palindrom(num+1,1,5)
  c=palindrom(num+2,1,4)
  d=palindrom(num+3,0,6)
  if a and b and c and d:
     return True
  else:
     return False
  


def main():
  i=19888
  print "Here are the possible numbers "
  while i<=999996:
    if check(i):
       print i    
    i+=1  



if __name__=='__main__':
   main()
