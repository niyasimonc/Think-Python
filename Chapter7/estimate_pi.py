import math

def fact(n):
  if(n==0):
    return 1
  else:
    return n*fact(n-1)


def originalpi():
  pi=math.pi
  print "value of pi from math.pi is",pi

def estimatepi():
  factor = 2 * math.sqrt(2) / 9801
  k=0
  total=0
  while True:
      num = fact(4*k) * (1103 + 26390*k)
      den = fact(k)**4 * 396**(4*k)
      term=factor*num/den
      total+=term
      if (abs(term)<1e-15):
         break
      k+=1

 
  onebypi=total
  pi=1/onebypi
  print "Calculated value of pi is ",pi
   

def main():
  originalpi()
  estimatepi()
  





if __name__=='__main__':
   main()
