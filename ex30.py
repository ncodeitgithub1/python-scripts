import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()
people=30
cars=40
buses=15
if cars>people:
   print "we should take cars"
elif cars<people:
   print "we should not take cars"
else:
   print "we cant decide"
if buses>cars:
   print "'thats too many buses"
elif buses>cars:
   print "that too many buses"
elif buses < cars:
   print "thhat too many buses"
else:
   print "we still cant decide"
if people>buses:
   print "alryt lets just take  buses"
else:
   print "fine, lets stay home " 
