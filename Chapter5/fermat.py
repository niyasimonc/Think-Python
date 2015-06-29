def checkfermat(a,b,c,n):
  x=(a**n)+(b**n)
  if not n>2:
    print "'n' must be > 2"
  else:
    if x==(c**n):
      print "Holy smokes, Fermat was wrong!"
    else:
      print "No, that doesn't work"
  




def main():
  a=raw_input("Enter value of a ")
  b=raw_input("Enter value of b ")
  c=raw_input("Enter value of c ")
  n=raw_input("Enter value of n ")
  checkfermat(int(a),int(b),int(c),int(n))





if __name__=='__main__':
  main()
