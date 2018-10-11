import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
from sys import argv

script, filename = argv

myfile = open(filename)

print myfile.read()

myfile.close()
