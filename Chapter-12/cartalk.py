
def make_word_list():
    dic={}
    f=open("words.txt","r")
    for line in f:
        word=line.strip().lower()
        if word not in dic:
            dic[word]=word
    dic['']=''
    dic['i']='i'
    dic['a']='a'
    return dic


def children(word,dic):
    t=[]
    for i in range(len(word)):
       child=word[:i]+word[i+1:]
       if child in dic:
          t.append(child)
    return t




def reducible(word,dic):
    if children(word,dic)==['']or children(word,dic)==['i'] or children(word,dic)==['a']:
       return True
    for child in children(word,dic):       
       if reducible(child,dic):
           return True
    return False




def reducible_words(dic):
    t=[]
    for word in dic:
      if reducible(word,dic):
        t.append(word)
    return t



def print_longest(dic):
        words=reducible_words(dic)
        l=len(words[0])
        for word in words:
            if len(word)>=l:
                l=len(word)
        print "length of longest word is",l
        for word in words:
            if len(word)==l:
                print "word is",'"',word,'"' 




def main():
    dic=make_word_list()
    print_longest(dic)   




if __name__=='__main__':
    main()
