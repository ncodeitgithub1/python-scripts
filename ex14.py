import datetime
myname = 'vasantha'
myid =  'NCD0918H003'
now = datetime.datetime.now()
print " script executed by %s with id %s." % (myname, myid)
print now.isoformat()

from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s. I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "do you like me %s?" % user_name
likes = raw_input(prompt)
print "where do you live %s?" % user_name
lives = raw_input(prompt)
print "what kind of computer do you have %s?" % user_name
computer = raw_input(prompt)
print """
Alright. So, you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. nice.
""" % (likes, lives, computer)
