import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
my_name = 'sravan kunar'
my_age = 24
my_height = 168
my_weight = 68
my_eyes ='Black'
my_hair = 'Black'
my_teeth = 'White'

print "Lets talk about %s." % my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes,my_hair)
print "his teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d, and %d i get %d." % (my_age,my_height,my_weight,my_age+my_height+my_weight)