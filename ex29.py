import datetime
myname = '<Venkatesh M>'
myid = '<NCD0518H025>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()








print "you enter a dark room with two doors. do u go through door #1 or door#2?"
door = raw_input(">")

if door == "1":
   print "there is a gaint bear eating cake.what do u do?"
   print "1. Take cake"
   print "2. scream at bear"
   bear = raw_input(">")

   if bear == "1":
    print "the bear eats your face off.good job"
   elif bear == "2":
     print "The bear eats your legs off. good job"
   else:
     print "well,doing %s is probably better ,bear run" %bear

elif door == "2":
   print "you stare into endless abyss at cthylhu's retina"
   print "1. Blueberries"
   print "2. Yellow jackt clothespins"
   print "3. understanding revolvers yelling melodies"

   insanity = raw_input(">")

if insanity == "1" or insanity == "2":
    print "your body survives powered by a mind of jelllo.good job"

else:
   print "you stumble around and fall on knife and die .good job"
