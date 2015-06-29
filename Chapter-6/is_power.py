def is_power(a,b):
  if a==b:
    return True
  elif a%b==0 and is_power(a/b,b):
    return True





def main():
  a=raw_input("Enter the value of a ")
  b=raw_input("Enter the value of b ")
  b=is_power(int(a),int(b))
  if b==True or int(a)==1:
    print 'a is power of b'
  else:
    print 'a is not a power of b'
  return


if __name__=='__main__':
  main()
