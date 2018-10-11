import datetime
myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
def cheese_and_crackers(cheese_count,box_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % box_of_crackers
    print "Man that's enough for a party1"
    print "Get a blanket. \n"

print "We can just give the function numbers directlty:"
cheese_and_crackers(20,30)

print "OR , we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print "we can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
print "And we can combine the two, varibles and math:"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)