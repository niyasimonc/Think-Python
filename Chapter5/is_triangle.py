def is_triangle(a,b,c):
  if c>=a+b or b>=a+c or a>=c+b:
     print "It can't form a triangle"
  else:
     print "it can form a triangle"

def main():
  a=raw_input("Enter the value of first side")
  b=raw_input("Enter the value of second side")
  c=raw_input("Enter the value of third side")
  is_triangle(int(a),int(b),int(c))





if __name__=='__main__':
  main()
