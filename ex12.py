import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

age = raw_input("how old are you? ")
height = raw_input("how tall are you? ")
weight = raw_input("how much do you weigh? ")
print "so, you're %r old. %r tall and %r heavy." % (
    age, height, weight)

