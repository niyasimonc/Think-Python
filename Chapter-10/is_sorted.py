def is_sorted(lis):
  l=len(lis)
  i=0
  while i<l-1  :
    if lis[i]<=lis[i+1]:
       i+=1
    else:
       return False
  return True

def main():
  l=['b','a']
  b=is_sorted(l)
  if b==True:
    print "Is sorted in ascending order"
  else:
    print "Not in ascending order"



if __name__=='__main__':
  main()
