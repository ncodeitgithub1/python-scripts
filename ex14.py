
import datetime
myname='sai sadhana'
myid='NCD0418H001'
now= datetime.datetime.now()
print  " script executed by %s with id %s " % (myname, myid)
print now.isoformat()
from sys import argv
script, user_name =argv
prompt='>'
print "hi %s, am the %s script" %(user_name,script)
print "i would like to ask u few que"
print "do u like this %s" %user_name
likes=raw_input(prompt)
print "wer do u live %s" %user_name
lives=raw_input(prompt)
print "wat kind of computer u hav" 
computer=raw_input(prompt)
print """
alryt so u said %r about likn me.
u live in %r.
and you hav %r computer
""" %(likes,lives,computer)
