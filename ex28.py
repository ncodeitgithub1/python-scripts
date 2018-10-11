import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
people = 30
cars = 40
trucks = 15

if cars > people:
    print "we should take the cars"
elif cars < people:
    print "we should not take the cars"
else:
    print "We cant decide"

if trucks > cars:
    print "That's too many tructs"
elif trucks < cars:
    print "may we could take the trucks"
else:
    print "we still cant decide"

if people > trucks:
    print "Alright, let's just take the trucks"
else:
    print "Fine, lets's stay home then"
