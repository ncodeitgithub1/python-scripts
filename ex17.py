import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, filename =argv
myfile = open(filename)
print myfile.read()
myfile.close()
