import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
print "i'll now count my tests:"
print "python", 25 + 30 / 6
print "Bash", 100 -25 * 3 % 4
print "How i ll count the test:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 -7


print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal? ", 5 >= -2 
print "Id it less or equal?", 5 <= -2
