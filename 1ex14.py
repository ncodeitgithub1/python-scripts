import datetime
myname = 'Chaithanya'
myid = 'NCD0818H008'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "where do you live %s?" % user_name
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about linking me. 
you live in %r. not sure where that is. 
and you have a %r computer. Nice. 
""" % (likes, lives, computer)