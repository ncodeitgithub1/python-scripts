import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

from sys import argv
script, first, second, third = argv
print "the script is called:", script
print "your first is called:", first
print "your second is called:", second
print "your third is called:", third