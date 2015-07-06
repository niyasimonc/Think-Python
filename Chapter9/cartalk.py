

def cartalk():
    f=open('words.txt','r')
    content=f.read()
    wordslist=content.split()


    for s in wordslist:
      l=len(s)
      i=0
      c=0
      
      while i <l-1:
#        print i,l
        if s[i]==s[i+1]:
           c=c+1
           if c==3:
             print s
           i=i+2
        else:
          c=0
          i=i+1
      
     



def main():
  cartalk()





if __name__=='__main__':
  main()
