import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"



from sys import argv

script, first, second, third = argv

print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
