import datetime
myname = 'jeethendar'
myid = 'NCD0818H007'
now = datetime.datetime.now()

print  "Script executed by %s with id %s " % (myname, myid)
print now.isoformat()
print "--------------------------------------------------------"


from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, Im the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "WHere do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind if computer do you have?"
computer = raw_input(prompt)

print """
alright, so you said %r about like me.
You live in %r, Not sre where it is.
ANd you have a %r computer. Nice
""" % (likes, lives, computer)

