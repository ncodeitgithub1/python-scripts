import datetime 
myname = 'Chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
ten_things="apple orange "
print "wait there"
stuff=ten_things.split(' ')
more_stuff=["day","night","song","cron","banaba","cat","dog","a","b","c"]
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
print "There we go: ", stuff
print "Let's do some things with stuff."
stuff[1]
stuff[- 1] 
print stuff.pop()
print ' '.join(stuff) 
print '#'.join(stuff[3:5]) 
