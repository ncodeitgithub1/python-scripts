import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "how old are you"
age = raw_input()
print "how tall are you?"
height = raw_input()

print "so, you're %r old, %r tall " %(age,height)
