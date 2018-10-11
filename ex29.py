import datetime
myname = 'Divya bharathi'
myid = 'NCD0318H021'
now = datetime.datetime.now()

print " Script executed by %s with id %s" % (myname, myid)
print now.isoformat()
print "you enter a dark room with two doors"

door = raw_input("> ")

if door == "1":
    print "There's a gaint bear here eating a cheese cake. What do you do? "
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear run" % bear

elif door == "2":
       print "you stare into the endless abyss at cbhb's rgh"
       print "1. Blueberries"
       print "2. Yellow jackers clothespins"
       print "3. UNderstanding revolvers yelling melodies"

      insanity = raw_input("> ")
      if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job"

    else:
        print "The insanity rots yur eyes into a pool of muck. Good job"

    else:
        print "you stumle around and fall on a knife and die. GOOD JOB"
