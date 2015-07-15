

def signature(w):
  t=list(w)
  t.sort()
  t=''.join(t)
  return t

def make_anagram_list():
    f=open("words.txt","r")
    d={}
    for line in f:
        word=line.strip()
        t=signature(word)
        if t not in d:
           d[t]=[word]
        else:
          d[t].append(word)
    return d

def filter_dic(dic,n):
   ana={}
   for i in dic.keys():
       if len(i)==n:
           ana[i]=dic[i]
   return  ana


def print_ana(d):
   t = []
   for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

   t.sort()
   for x in t:
        print x


def main():
    dic=make_anagram_list()
    eight_letter_anagrams=filter_dic(dic,8)
    print_ana(eight_letter_anagrams)

if __name__=='__main__':
    main()
