def plusbeam():
  print ('+ '+'- '*4)*4+'+'
  return
def verbeam():
  print ('|'+' '*9)*4+'|'
  return
def verbeam4():
  verbeam()
  verbeam()
  verbeam()
  verbeam()

def one():
  plusbeam()
  verbeam4()
  
def two():
  one()
  one()

def four():
  two()
  two() 
  plusbeam()

def main():
  four()
if __name__=="__main__":
  main()
