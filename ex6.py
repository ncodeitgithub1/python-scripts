import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
x = "there are %d type of people" %10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s" % (binary,do_not)

print x
print y

print "i said: %r." %x
print "i said: '%s'." %y
