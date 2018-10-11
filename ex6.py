import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those  who know %s and those %s." % (binary,do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
w= "This is the left side of..."
e= "a string with a right side"

print w+e