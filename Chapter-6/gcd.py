def gcd(a,b):
  if b==0:
    return a
  else:
    r=a%b
    return gcd(b,r)


def main():
  a=raw_input("Enter the value of a ")
  b=raw_input("Enter the value of b ")
  g=gcd(int(a),int(b))
  print g


if __name__=='__main__':
   main()
