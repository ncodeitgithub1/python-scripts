import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("how much do you weight")
print "so, you are %r old, %r tall and %r heavy" % (age, height, weight)

