from datetime import *
import datetime


def current_date():
  today= datetime.date.today()
  print today
  print today.strftime('%A')
  return



def next_birthday():
  birthday=datetime.date(1989,05,16)
  print "Days untill Birthday"
  today=date.today()
  next_birthday=datetime.date(today.year,birthday.month,birthday.day)
  if today>next_birthday:
     next_birthday=datetime.date(today.year+1,birthday.month,birthday.day)
  delta=next_birthday-today
  print delta.days



def double_day(b1,b2):
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day



def main():
  current_date()
  next_birthday()
  print "Double day"
  b1 = datetime.date(2006, 12, 26)
  b2 = datetime.date(2003, 10, 11)
  print  double_day(b1,b2)



if __name__=='__main__':
