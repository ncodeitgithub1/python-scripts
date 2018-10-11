import datetime
myname = '<kavya>'
myid = '<NCD0918H006>'
now = datetime.datetime.now()

print" script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "you enter a dark room with two doors. do you go through door #1 or door #2 "
door = raw_input("> ")
if door == "1":
    print "there's a giant bear here eating a cheese cake. what do you do?"
    print "1. take the cake"
    print "2. scream at the bear"
    bear = raw_input("> ")
    if bear == "1":
        print "the bear eats your face off good job"
    elif bear == "2":
        print "the bear eats your legs off good job"
    else:
        print "well, doing %s is probably better. bear run away" % bear
elif door == "2":
    print "you stare into the endless abyss at cthulhu's retina"
    print "1. blueberries"
    print "2. yellow"
    print "3. understanding"
    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
        print "your body survives"
    else:
        print "the insanity rot"
else:
    print "you stumble around"
