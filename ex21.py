import datetime
myname = 'SAIKUMAR'
myid = 'NCD0518H024'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


def add(a, b):

print "ADDING %d + %d" % (a, b)
return a + b

def subtract(a, b):
print "SUBRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTYPLYING %d * %d" % (a, b)
    return a * b

def divide (a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "age: %d, Height: %d, weight: %d, IQ: %d"

%(age, height, weigjht, iq)

print "here is a puzzle."

print "that become:", what, "cana you do it by hand?"
