import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()
from sys import exit
def gold_room():
    print "this rum is full of gold"
    next=raw_input(">")
    if "0" in next or "1" in next:
       how_much=int(next)
    else:
       dead("man leaen to type")
    if how_much<50:
       print "nice, u r not ready"
       exit(0)
    else:
       dead("u r greedy")
def bear_room():
      print "there is a bear here"
      print "the bear has a bunch of honey"
      print "the fact bear is in front of another door"
      bear_moved=False
      while True:
          next=raw_input(">")
	  if next=="take honey": 
	     dead("the bear looks at you then slaps ur face off")
          elif next=="taunt bear" and not bear_moved:
            print "the bear has moved from door"
            dead("the bear gets piissed off")
          elif next=="open door" and bear_moved:
            gold_room()
          else:
             print "i got no idea"
def cthulhu_room():
    print "here u c the great evil cthulu"
    print "he it whatever stares at u and u go insane"
    print "do u file flee for ur "
    next=raw_input(">")
    if "flee" in  next:
       start()
    elif "head" in next:
        dead("well that was tasty")
    else:
      cthulhu_room()
def dead(why):
    print why, "good job"
    exit(0)
def start():
    print "u are in dark rum"
    print "ther is dooor"
    next=raw_input(">")
    if next=="left":
      bear_room()
    elif next=="ryt":
      cthulhu_room()
    else:
      dead("u stumble around")
start()

