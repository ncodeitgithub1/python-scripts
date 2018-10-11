import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

days ="mon tue wed thu fri sat sun"
months = "jan\nfeb\nmar\napr\nmay\njun\njul\naug"

print """
There is something going on there.
With the three double quotes.
we'll be able to type as much as you like.
even 4 lines if you want. or 5, or 6.
"""