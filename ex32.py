import datetime
myname = 'MD SABAIR'
myid = 'NCD0318H018'
now = datetime.datetime.now()
the_count=[1,2,3,4,5]
fruit=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3]
for number in the_count:
    print "this is clount %d" %number
for fruit in fruit:
    print "a fruit of type: %s" %fruit
for i in change:
    print "i got %r" %i
elements=[]
for i in range(0,6):
    print "adding %d to list" %i
    elements.append(i)
for i in elements:
    print "elements was: %d" %i

