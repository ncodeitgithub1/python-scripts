import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
def add(a,b):
	print "adding %d +%d" % (a,b)
	return a+b
def sub(a,b):
        print "subtracting %d - %d" % (a,b)
        return a-b
def multi(a,b):
        print "multi %d * %d" % (a,b)
        return a*b
def div(a,b):
        print "div %d / %d" % (a,b)
        return a/b
print "Let's do some math with just functions"

age = add(30, 5)
height = sub(78, 4)
weight = multi(90, 2)
iq = div(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the exra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, sub(height, multi(weight, div(iq, 2))))

print "That becomes: ", what, "Cana you do it by hand?"
