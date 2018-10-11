import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
the_count = [1,2,3,4,5,6,]
fruits = ['apple','orange','pears','apricots']
change = [1,'pennies',2,'domes',3,'quarters']
for number in the_count:
	print "this is count%d" % number
for fruit in fruits:
    print "A fruit of type: %s" % fruits

# also we can go through mixes lists too
# notice we have to use %r since we dont know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists; first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i

    # append is a function that lists Understand
    elements.append(i)

# now we can print them out too

for i in elements:
    print "Element was: %d" %i

