import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i+1
    print "Numbers now:", numbers
    print "At the bottom i is %d " % i
print "The numbers:"

for num in numbers:
    print num
