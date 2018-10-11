import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % (True, False, True, False)

