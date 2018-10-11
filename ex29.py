import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
people = 20
cats = 30
dogs = 15
if people <cats:
	print "too many cats"
if people > cats:
	print "not many cats"

if people < dogs:
        print " world is drooled on"
if people > dogs:
        print "world is dry"
dogs +=5
if people >dogs:
	print "people are greater than or equal to dogs"
if people <=dogs:
        print "people are less than or equal to dogs"
if people == dogs:
        print "people are dogs"


