print "you ente a dark room with two doors. Do you go through door #1 or Door #2?"
door = raw_input("> ")
if door == "1":
    print "There's a gaint bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "well doing %s is probably better. Bear runs away." % bear
    elif door == "2":
        print "You stare into the endless abyss at Cthulthu's retina."
        print "1. Blueberries."
        print "2. Yellow jacket clothespins."
        print "3. Understanding revovers yelling melodies."
        insanity = raw_input("> ")
        if insanity == "1" or insanity == "2":
            print "your body survives powered by a mind of jello. Good job!"
        else:
            print "The stumble around and fall on a knife and die. Good job!"
