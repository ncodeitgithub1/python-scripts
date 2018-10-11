import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()


def print_two(*args):
    arg1, arg2 = args
    print "ar-g1: %r, arg2: %r" % (arg1,arg2)
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)
def print_one(arg1):
    print "arg1: %r" % arg1
def print_none():
    print "I got nothing."
print_two_again("sravan","kumar")
print_two_again("sravan","kumar")
print_one("sarvan")
print_none()