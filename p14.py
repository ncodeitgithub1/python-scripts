import datetime
myname = '<ravi teja>'
myid = '<ncd0918h007>'
now = datetime.datetime.now()

print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()

from sys import argv
script, user_name = argv
prompt ='>'
print " hi %s iam %s script" %(user_name, script)
print " i'd leke to ask u a few questions."
print " Do you like me %s?" % user_name
likes = raw_input(prompt)

print" where do u live %s ?" % user_name
lives = raw_input(prompt)

print" what kind of comp do u have?"
computer = raw_input(prompt)

print """alright so you said 5r about liking me.
u live in 5r not sure where that is
and u hav a %r comp nice"""