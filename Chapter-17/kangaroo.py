class kangaroo(object):
  """attri:pouch_contents"""
  
  def __init__(self,pouch_contents=[]):
       self.pouch_contents=pouch_contents

  
 
  def __str__(self):
      t=[object.__str__(self)+'with contents ']
      for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
      return '\n'.join(t)




  def put_in_pouch(self,item):
       self.pouch_contents.append(item)
       
  





def main():
   kanga=kangaroo()
   roo=kangaroo()
   kanga.put_in_pouch('car_key')
   kanga.put_in_pouch('niya')
   print kanga
   kanga.put_in_pouch(roo)
   print kanga



if __name__=='__main__':
  main()
