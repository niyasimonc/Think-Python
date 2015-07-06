def reverse(n):
  str1=str(n).zfill(2)
  return str1[::-1].zfill(2)

def instances(diff):
    daughter=1
    c=0
    mother=daughter+diff
    while  daughter<90 and mother<=100:
      mother=daughter+diff
      if str(daughter).zfill(2)==reverse(mother):
        c=c+1
      daughter+=1
    return c


def pri(d):
  daughter=1
  mother=daughter+d
  while mother<100 and daughter<90:
     if str(daughter).zfill(2)==reverse(mother):
       print daughter,'               ',mother
     daughter+=1
     mother=daughter+d
  return



def main():
  diff=9
  while diff<82:
    c=instances(diff)
    if c==8:
      print 
      print "The age differnce is ",diff
      print
      print "daughter",'       ',"mother"
      pri(diff)
    diff+=1
  return


if __name__=='__main__':
  main()
