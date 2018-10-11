import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


print "how old are you",
age = raw_input()
print "how tall are you?",

height =raw_input()

print "How much do you weigh",
weight = raw_input()

print "so , you're %r old, %r tall and %r heavy" %(age,height,weight)
