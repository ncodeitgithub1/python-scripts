import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
people = 30
cars = 40
buses = 15
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars ."
else:
    print "We can't decide."
if buses > cars:
    print "That's too many buses"
else:
    print "We still can't decide."
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
