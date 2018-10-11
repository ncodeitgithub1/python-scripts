import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()



while True:

   for i in ["/","-","|","\\","|"]:
      print "%s\r" %i,
