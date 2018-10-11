import datetime
myname = 'SAIKUMAR'
myid = 'NCD0518024'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


x = "there are %d types of people" % 10
binary ="binary"
do_not = "dont"
y="those who know %s and those who %s" % (binary, do_not)

print x
print y

print "i said: %r." % x
print "i also said: '%s'." %y

hilarious = False
joke_evaluation = "is'nt that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of ...."
e = "a string with a right side"

print w + e
