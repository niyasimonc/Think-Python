from rotate import rotate


def make_word_list():
    f=open("words.txt","r")
    di={}
    for line in f:
       word=line.strip()
       di[word]=word
    return di

def rotate_word(word,dic):
    for i in range(1,14):
        rotated=rotate(word,i)
        if rotated in dic:
          print word,i,rotated


def main():
   dic=make_word_list()
   for word in dic:
       rotate_word(word,dic)
 






if __name__=='__main__':
     main()
