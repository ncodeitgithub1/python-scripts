import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "u hav %d cheeses" %cheese_count
    print "u hav %d boxes of crackers" %boxes_of_crackers
    print "man thats enough for party"
    print "get bla blanket.\n"
print "we can just give directly"
cheese_and_crackers(20,30)
print "OR,we can use variable from script"
amount_of_cheese=10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print "we can even do math"
cheese_and_crackers(10+20,5+6)
print "and we can combine thw two, variables and math"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
