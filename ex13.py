import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, first, second, third = argv
print "the script is called", script
print "ur first variable is", first
print "ur second variable is", second
print "ur third variabe is", third

