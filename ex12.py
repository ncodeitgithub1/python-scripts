import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"


age = raw_input("How old are you: ")
height = raw_input("How tall are you: ")
weight = raw_input("How much do you weight:")

print "So you are %r young, %r tall and %r heavy." %(age, height, weight)
