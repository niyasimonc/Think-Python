def palindrom(s):
  if s=='':
    print "True"
    return
  if s[0]!=s[-1]:
    print "False"
  else :
    palindrom(s[1:-1])  





def main():
  string=raw_input("Enter your string ")
  palindrom(string)



if __name__=='__main__':
  main()
