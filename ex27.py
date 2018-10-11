import datetime
myname = 'SAIKUMAR'
myid = 'NCD0518H024'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


people = 30
cars = 40
trucks = 15

if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars"
else:
    print "We cant decide"

if trucks > cars:
    print "That's too many tructs"
elif trucks < cars:
    print "may we could take the trucks"
else:
    print "We still cant decide"

if people > trucks:
    print "Alright, let's just take the trucks"
else:
    print "Fine, let's stay home then."

