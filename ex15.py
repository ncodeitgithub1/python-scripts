import datetime
myname = 'chandra'
myid = 'NCD0618H003'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script,name= argv
prompt ='#####'
print "Hi %s, I'm the %s script." %(name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % name
likes = raw_input(prompt)

print "Where do you live %s?" % name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is .
And you have a %r computer. Nice.
""" % (likes, lives, computer)
