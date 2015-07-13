def has_duplicate(l):
    dict={}
    for i in l:
       if i in dict:
          dict[i]=dict[i]+1
       else:
          dict[i]=1
    l=dict.values()
    if 2 in set(l):
      print 'Has duplicates'
    else:
      print 'no duplicates'


def main():
    t=[1,2,3]
    has_duplicate(t)
    t=[3,3,4,5]
    has_duplicate(t)
    t=[3,6,6,7]
    has_duplicate(t)



if __name__=='__main__':
    main()
