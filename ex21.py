import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
def add(a,b):
    print "adding %d+%d" %(a,b)
    return a+b
def subtract(a,b):
    print "subtracting %d-%d" %(a,b)
    return a-b
def multiply(a,b):
    print "multiplying %d*%d" %(a,b)
    return a*b
def divide(a,b):
    print "dividing %d/%d" %(a,b)
    return a/b
print "lets do some math vth just funcns"
age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)
print "age: %d,height: %d, weight: %d, iq: %d" %(age,height,weight,iq)
print "here is puzzle"
what=add(age,subtract(height,multiply(weight,divide(iq,2))))
print "that becomes:",what,"can u do "
