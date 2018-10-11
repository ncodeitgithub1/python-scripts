import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
x="there are %d types of people" %10
binary="binary"
do_not="dont"
y="those who know %s and those who %s" %(binary,do_not)
print x
print y
print "i said: %r" %x
print "i also said: '%s'" %y
hilarious=False
joke_evaluation="Isnt that joke so funny %r"
print joke_evaluation %hilarious
w="this is the left side"
e="this is thr ryt side"
print w+e
