import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
age= raw_input("how old are you?")
height = raw_input("how tall are you ? ")
print "so, tou are %r old and %r tall" %(age,height)

