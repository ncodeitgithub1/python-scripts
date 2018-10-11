import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "i will now count my chickens:"
print "Hens", 25+30/6
print "rosters", 100-25*3%4
print "how i will count eggs:"
print 3+2+1-5+4%2-1/+6


