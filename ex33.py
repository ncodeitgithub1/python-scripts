import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
i=0
number =[]
limit = 6
while i<limit:
	print "at the top i is %d" % i
	number.append(i)

        i=i+1
	print "number now:", number
	print "at the bottom i is %d" % i

print "the number:"
for num in number:
	print num

