import datetime
myname = 'vasantha'
myid = 'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

my_name = 'vasantha'
my_age = 25
my_height = 5
my_weight = 50
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'
print "let's talk about %s." % my_name
print "she's %d feet tall." % my_height
print "she's %d kgs heavy." % my_weight
print "actually that's not too heavy."
print "she's got %s eyes and %s hair." % (my_eyes, my_hair)
print "her teeth are actually %s depending upon the coffee." % my_teeth
print "If I add %d, %d and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)