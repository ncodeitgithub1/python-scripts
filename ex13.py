import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
age = raw_input("how old are you? ")
height = raw_input("How tall are you?")
weight = raw_input("HOw much do you weight?")

print "So, you're %r old, %r tall and %r heavy" %(age,height,weight)
