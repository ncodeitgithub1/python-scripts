import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)
def print_one(arg1):
    print "arg1: %r" % arg1
def print_none():
    print "i got nothing"
#print_two("chandra","shekhar")
print_two_again("chandra","shekhar")
print_one("first!")
print_none()
