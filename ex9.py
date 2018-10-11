import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days:",days
print "Here are the months:",months

print """
There's something going on here.
with the three double-quotes.
we'll be able to type as much as we like.
Even 4 lines if we want , or 5, or 6."""