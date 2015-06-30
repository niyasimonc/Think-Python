
def rotate(s,i):
   l=len(s)
   snew=''
   for j in range(l):
     num=ord(s[j])
     b=s[j].islower()
     if b== True:
       if (num+i)>122:
         n=97
         m=(num+i)-122
         n=n+(m-1)
       else :
         n=num+i
     else:
       if (num+i)>90:
         n=65
         m=(num+i)-90
         n=n+(m-1)
       else :
         n=num+i
     snew=snew+chr(n)
   return snew
 



def main():
  s=raw_input("Enter the string ")
  i=raw_input("Enter the number to be shifted ")
  sr=rotate(s,int(i))
  print s,'  ',sr






if __name__=='__main__':
  main()
