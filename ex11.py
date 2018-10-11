import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "how old r u",
age=raw_input()
print "how tall r u",
height=raw_input()
print "how much do u weigh",
weight=raw_input()
print "so u r %r old,%r tall and %r heavy" %(age,height,weight)
