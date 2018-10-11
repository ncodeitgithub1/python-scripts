import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "how old are you?",
age = raw_input()
print "How tall are you?"
height = raw_input()
print "how much do you weight?"
weight = raw_input()
print "so, you're %r old, %r tall "