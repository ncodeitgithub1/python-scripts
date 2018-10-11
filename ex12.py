import datetime
myname = 'Avinash'
myid = 'NCD0318H022'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()



age = raw_input("how old are you?")

height = raw_input("how tall are you?")
weight = raw_input ("How much do you weigh?")

print "So, you're %r old, %r tall and %r heavy" %(age, height, weight)
