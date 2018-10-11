import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
days = "Mon Tue Wed Thu Fri"
months = "Jan\nFeb\nMar\nApr\nMay"
print "here are the days: ", days
print months
