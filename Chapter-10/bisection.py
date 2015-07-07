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


def main():
   words=make_word_list()
   for word in ['aal', 'aaal']:
        print word, 'in list', in_bisect(words, word)



if __name__ == '__main__':
   main()


