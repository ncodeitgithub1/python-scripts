import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
def print_one(arg1):
    print "arg1: %r" %arg1
def print_none():
    print "i hot nothing'."
    print_two("nani", "abhi")
    print_two_again("nani", "abhi")
    print_one("First!")
    print_none()