import datetime
myname = 'shiva'
myid = 'NCD0518H028'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

print "i will now count my chikens:"
print "Hens", 25 + 30 / 6
print "Rossters", 100 - 25 * 3 % 4

print "how i will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6 

print "is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "what is 3 + 2?", 3 + 2

print "what is 5 -7?", 5 - 7

print "oh, that's why it's False."

print "how about some more."

print "is it greater?", 5 > -2
print "is it grater or equal", 5 >= -2
print "is it less or equal?", 5 <= -2
