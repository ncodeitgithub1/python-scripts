import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"


print "How old are you?"
age = raw_input()
print "How tall are you"
height = raw_input()
print "How much do you weigh"
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
