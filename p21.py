import datetime
myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

def add(a, b):
    print"ADDING %d + %d" %(a, b)
    return a + b
def subtract(a, b):
    print "subtractng %d -%d " %(a, b)
def multiply(a, b):
    print "multiplying %d * %d" %(a, b)


print " lets do some math with just functns"

age = add(30, 5)
height = subtract(78, 3)
weight = multiply(40, 2)

print "age: %d, height: %d, Weight: %d" % (age, height, weight)

print " here is a puzzle"
what = add(age , subtract(height, multiply(weight,2)))
print " that becomes what can u do it by hand"