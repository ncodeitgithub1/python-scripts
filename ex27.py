import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
people = 20
cats = 30
dogs = 15

if people < cats:
      print "too many cats! the world is doomed!"

if people > cats:
      print "Not many cats! The word is saved"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people > dogs:
    print "People are greated than or equal to dogs."
if people <= dogs:
    print "people are less than or equal to dogs"

if people == dogs:
   print "people are dogs"
