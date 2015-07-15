import urllib
import re


def open_url(zip_code):
  url='http://www.uszip.com/zip/'+zip_code
  ufile=urllib.urlopen(url)
  fil=file("url.txt","w")
  for line in ufile:
    fil.write(line)

    match=re.search(r'<title>(.*) zip code</title>',line)
    
    if match:
       print 'zip code is for',match.group(1)
    match=re.search(r'population</dt><dd>(.*)<span class(.*)>Housing units<',line)
    if match:
        print "population is",match.group(1)
        break


def main():
  zip_=raw_input("Enter the zip code ")
  open_url(zip_)




if __name__=='__main__':
  main()
