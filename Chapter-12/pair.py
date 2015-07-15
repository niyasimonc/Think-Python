from all_anagrams import *

def pair(d):
  for anagrams in d.values():
    for word1 in anagrams:
      for word2 in anagrams:
        if word1<word2 and word_distance(word1,word2)==2:
           print word1,word2
  return

def word_distance(x,y):
  x=list(x)
  y=list(y)
  c=0
  for a,b in zip(x,y):
       if a!=b:
         c+=1
  return c 


def main():
  dic=make_anagram_list()
  pair(dic)  
  return
  

if __name__=='__main__':
  main()
