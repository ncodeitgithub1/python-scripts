import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()






i = 0
numbers = []

limit = 6
while i < limit:
   print "At the top i is %d" %i
   numbers.append(i)

   i=i+1
print "Numbers now:",numbers
print "At bottom i is %d" % i
print "The numbers:"

for num in numbers:
 print num
