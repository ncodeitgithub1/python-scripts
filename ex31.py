import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "you enter a dark room with two doors #1 or #2?"
door = raw_input(">")
if door =="1":
	print "there a gaint bera hera eating a cheese cake"
	print "1.take the cake"
	print "2.screamthe bear"
	bear = raw_input(">")
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear run" % bear


elif door == "2":
    print "You stare into the endless abyss at Cthylhu's retina"
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job"

    else:
        print "The insanity rots yur eyes into a pool of muck. Good job"

else:
    print "You stumble around and fall on a knife and die. Good job"

