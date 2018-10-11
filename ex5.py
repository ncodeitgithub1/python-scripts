import datetime
myname = 'shiva'
myid = 'NCD0518H028'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

my_name = 'zed A. shaw'
my_age = 35 
my_height = 74
my_weight = 180
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounts heavy" % my_weight
print "Actully that's not too heavy"
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "if I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "this is %r nothing new %r in my line of %r work" % (my_age, my_height, my_weight)
