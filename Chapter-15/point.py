class point(object):
  """Represent a point in 2d space"""

class rectangle(object):
   """attributes:width,height,corner"""


def print_point(point):
  print point.x
  print point.y


def find_center(polygon):
  p=point()
  p.x=polygon.corner.x+polygon.width/2.0
  p.y=polygon.corner.y+polygon.height/2.0
  return p



def grow_rectangle(box,dwidth,dheight):
  box.width=box.width+dwidth
  box.height=box.height+dheight


def main():
  blank=point()
  blank.x=3
  blank.y=4
  print 'blank'
  print_point(blank)  
   
  box=rectangle()
  box.width=100.0
  box.height=200.0
  box.corner=point()
  box.corner.x=0.0
  box.corner.y=0.0


  center=find_center(box)
  print 'center'
  print_point(center)
  

  
  print box.height
  print box.width
  print 'grow'
  grow_rectangle(box,50,100)
  print box.height
  print box.width




if __name__=='__main__':
  main()
