import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_one(arg1):
    print "arg1: %r" % arg1
def print_none():
    print "I got nothing."
print_two("vasantha", "kavya")
print_two_again("vasantha", "kavya")
print_one("First!")
print_none()



