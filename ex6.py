import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()



x = "there are %d types of people" %10
binary= "binary"
do_not="don't"
y="those who know %s and those who %s" %(binary,do_not)

print x
print y

print "i said %r" %x
print "i also said '%s'" %y

hilarious = False
joke_evaluation = "isn't that joke so funny  %r"

print joke_evaluation % hilarious

w="This is left side of...."
e= "a string with a right side"

print w+e
