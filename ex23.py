import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply (a, b):
    print "MULTYPLYING %d * %d" % (a, b)
    return a * b

def divide (a, b):
    print "Divideing %d / %d" % (a,b)
    return a / b

print "Let's do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "THat become: ", what, "cana you do it by hand?"
