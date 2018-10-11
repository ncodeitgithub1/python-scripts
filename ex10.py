import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
while True:
   for i in ["/","-","|"]:
      print "%s\r" %i,

