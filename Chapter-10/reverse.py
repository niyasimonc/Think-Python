from bisect import bisect_left


def make_word_list():
    fin = open('words.txt')
    content=fin.read()
    words=content.split()
    return words

def in_bisect(word_list, word):
   i = bisect_left(word_list, word)
   if  i<len(word_list) and word_list[i] == word:
        return True
   else:
        return False




def reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print word, word[::-1]

