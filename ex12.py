import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
age=raw_input("how old r u")
height=raw_input("how tall are u")
weight=raw_input("how much do u weigh")
print "so u r %r old, %r tall and %r heavy" %(age,height,weight)
