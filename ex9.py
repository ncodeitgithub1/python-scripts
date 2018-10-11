import datetime
myname = 'Avinash'
myid = 'NCD0318H022'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

days ="mon tue wed thu fri sat sun"

months = "jan\nfeb\nmar\napr\nmay\njun\njuly\aug"

print "here are the days:", days
print "here are the months:", months

print """

there's something going on here 
with the there double-quotes.
we'll be able to type as much as we like.
even 4 lines if we want, or 5, or 6.
"""
