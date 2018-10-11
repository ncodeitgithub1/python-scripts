import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

print "I will now count my chickens:"
print "hens", 25 + 30 / 6
print "roosters", 100 - 25 * 3 % 4
print "now I will count eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "It is true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
print "what is 3 + 2?", 3 + 2
print "what is 5 - 7?", 5 - 7
print "Oh. tht's why it's false."
print "how about some more."
print "It is greater?", 5 > -2
print "It is greater or equal?", 5 <= -2
print "It is less or equal?", 5 <=2
