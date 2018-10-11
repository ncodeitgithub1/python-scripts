import datetime
myname = 'Avinash'
myid = 'NCD0318H022'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


i = 0
numbers = []
limit = 6

while i < limit:

	print "at the top i is %d" % i
	numbers.append(i)
	i = i + 1

print "number now:", numbers
print "at the bottom i is %d" % i

print "the numbers:"
for num in numbers:
	print num
