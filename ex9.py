import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
days = "Mon Tue Wed Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the thre double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6
"""
