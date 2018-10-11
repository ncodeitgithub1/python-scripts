x = "there are %d typrs of people" %10
binary = "binary"
do_not = "don't"
y = "those who knows %s and those who %s" % (binary, do_not)
print x
print y
print "i said: %r" % x
print "i also said: '%s'" % y
hilarious = False
joke_evaluation = "is not joke so funny?! %r"
print joke_evaluation % hilarious
w = "this is the left side of..."
e = "a string witha aright side."
print w + e