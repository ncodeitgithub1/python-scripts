import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" %i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At teh bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
