import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricats']
change = [1, 'pennies', 2, 'domes', 3, 'quarters']

for number in the_count:
      print "this is count %d " % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit
for i in change:
    print "i got %r" % i

elements = []

for i in range(0, 6):
    print "adding %d to the list" % i

for i in elements:
    print "elements was : %d" %i
