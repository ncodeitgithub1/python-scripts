import datetime

myname = 'SRAVAN'
myid = 'NCD0918H002'
now = datetime.datetime.now()

print " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "You enter a dark room with two doors. Do you go through door #1 or door #2>?"
door = raw_input("> ")
if door == "1":
    print "Ther's is a giant bear here eating a cheese cake. what do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off. Good Job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at cthlhu's retina."
    print "1.Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolves yelling melodies."

    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good Job!."
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
else:
    print "You stumbe around and fall on a knife and die. Good Job1//"
    