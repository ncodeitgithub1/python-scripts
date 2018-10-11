import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
scripts, first, second = argv
print "the script is called:", scripts
print "your first vatiable is:", first
print "your second variabe is:", second

