import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()







people = 20
cats = 30
dogs = 15

if people < cats:
   print "Too many cats.worls is doomed"

if people > cats:
   print "Not many ctas.world is saves"

if people < dogs :
   print "world is drooled on"

if people > dogs:
   print "world is dry"

dogs += 5

if people > dogs:
   print "people are less than or equal to dogs"

if people <= dogs:
   print "people are less tha or equal to dogs"

if people  == dogs:
   print "people are dogs"  
