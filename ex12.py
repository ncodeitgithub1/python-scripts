import datetime
myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)