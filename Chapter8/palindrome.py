def palindrom(s):
  l=len(s)
  srev=s[::-1]
  for i in range(l):
    if s[i]==srev[i]:
       i+=1
    else:
      return False  
  return True



def main():
  s=raw_input()
  b=palindrom(s)
  if b==True:
    print "Palindrom"
  else:
    print "not Palindrom"




if __name__=='__main__':
  main()
