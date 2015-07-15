def most_frequent(s):
    length=len(s)
    dic={}
    for i in range(length):     
        if dic.get(s[i])==None:
           dic[s[i]]=1
        else:
            dic[s[i]]=dic[s[i]]+1
    return dic

def main():
    string=raw_input("Enter the string ")
    dic=most_frequent(string)
    lis=sorted(dic,key=dic.get,reverse=True)
    print lis
       


if __name__=='__main__':
    main()
