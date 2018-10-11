import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

people = 30
cars = 40
buses = 15
if cars > people:
    print "we should take cars."
elif cars < people:
    print "we should not take cars."
else:
    print "we can't decide."
if buses > cars:
    print "that's too many buses."
elif buses < cars:
    print "maybe we could take the buses."
else:
    print "we still can't decide."
if people > buses:
    print "Alright. let's just take the buses."
else:
    print "fine let's stay home then."
