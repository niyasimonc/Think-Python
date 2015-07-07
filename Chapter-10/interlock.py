from bisection import *


def interlock(word_list, word):
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
        print word,inter
    return True
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print word, word[::2], word[1::2]

         if interlock_general(word_list, word):
           print 
            


