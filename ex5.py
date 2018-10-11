import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
my_name = 'Zed A. Shaw'
my_age = 25
my_height = 155
my_weight = 46
my_eyes = 'black'
my_teeth = 'white'

print "lets talk about %s" % my_name
print "He's %d inches tall" % my_height
print "He is %d pounds heavy" % my_weight
print "Actually that's not too heavy"

print "if I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "this is %r nothing new %r in my line of %r work" % (my_age, my_height, my_weight)
