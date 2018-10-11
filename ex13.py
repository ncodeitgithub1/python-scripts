import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first varible is :", first
print "Your second varible is :" , second
print "Your third varible is :" , third