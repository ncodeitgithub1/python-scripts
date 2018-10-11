import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()





from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Yoru first variable is :", first
print "Your second variable is:", second
print "Your third variable is :", third
