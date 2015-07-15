import urllib


def main():
  ufile=urllib.urlopen('http://thinkpython.com/secret.html')
  for line in ufile:
     print line.strip()




if __name__=='__main__':
  main()
