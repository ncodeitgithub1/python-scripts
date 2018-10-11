import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()




people = 30
cars = 40
trucks = 15

if cars > people:
   print "we should take cars"

elif cars < people:
   print "we should not take cars"

else:
   print "we cant decide"

if trucks > cars:
  print "that too many trucks"
elif trucks < cars:
    print "may we could take trucks"
else:
   print "we still cant decide"
if people > trucks:
   print "Alright, let's just take trucks"
else:
   print "Fine, lets stay home then"
