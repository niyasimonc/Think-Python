 def anagram(x,y):
  
  xl=len(x)
  yl=len(y)
  if xl==yl:
    for i in range(xl):
      if x[i] in y:
        i+=1
      else:
        return False
    return True



def main():
  a=raw_input("Enter the first word:")
  b=raw_input("Enter the second word:")
  v=anagram(a,b)
  if v==True:
    print "Anagram"
  else:
    print "Not anagram"
 



if __name__=='__main__':
   main()
