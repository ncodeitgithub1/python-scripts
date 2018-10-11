import datetime
myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

age = raw_input("how old r u?")
height = raw_input("how tall r u?")
weight = raw_input(" how much do you weight?")

print " so, you're %r old %r tall and %r heavy" %(age, height, weight)