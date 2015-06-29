def ack(m,n):
  if m==0:
    r= n+1
    return r
  if m>0 and n==0:
    r=ack(m-1,1)
    return r
  if m>0 and n>0:
    r=ack(m-1,ack(m,n-1))
    return r

  




def main():
  m=raw_input("Enter value for m ")
  n=raw_input("Enter value for n ")
  r=ack(int(m),int(n))
  print r





if __name__=='__main__':
  main()
